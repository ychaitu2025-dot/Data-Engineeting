"""
Python Basics - Session 3: String & List Objects
Topic: Indexing/Slicing, String Methods, List Methods, Nested Lists, List Comprehensions, Strings vs Lists
Student: Chaitanya Y
"""

# ============================================================================
# 1) STRING AND LIST OBJECTS
# ============================================================================
# Strings (str) store text (characters)
# Lists (list) store a collection of items (numbers, strings, mixed types, even other lists)

# Both support:
#   - len()
#   - indexing ([ ])
#   - slicing ([:])
#   - looping

# Key differences:
#   - Strings are IMMUTABLE (cannot be changed in place)
#   - Lists are MUTABLE (can be changed in place)

print("--- STRING AND LIST OBJECTS ---")
s = "python"
lst = [1, 2, 3, 4]
print(f"String: {s}, List: {lst}")


# ============================================================================
# 2) LEN() - LENGTH
# ============================================================================
# len() returns the number of elements:
# - number of characters in a string
# - number of items in a list

print("\n--- LEN() FUNCTION ---")
s = "python"
lst = [10, 20, 30, 40]

print(f"Length of string: {len(s)}")   # 6
print(f"Length of list: {len(lst)}")   # 4


# ============================================================================
# 3) INDEXING - ACCESS SPECIFIC ELEMENT
# ============================================================================
# Python uses 0-based indexing:
# - first element is index 0
# - last element is index -1

print("\n--- INDEXING ---")
s = "chandler"
print(f"First char s[0]: {s[0]}")      # 'c'
print(f"Last char s[-1]: {s[-1]}")     # 'r'

lst = ["a", "b", "c", "d"]
print(f"List[1]: {lst[1]}")            # 'b'
print(f"List[-2]: {lst[-2]}")          # 'c'


# Common Exception: IndexError
print("\n--- INDEX ERROR EXAMPLE ---")
s = "hi"
try:
    print(s[5])
except IndexError as e:
    print(f"Error: IndexError - {e}")


# ============================================================================
# 4) SLICING - GET A PORTION
# ============================================================================
# Slicing format: sequence[start : stop : step]
# - start is included
# - stop is NOT included
# - step controls jump (default 1)

print("\n--- SLICING EXAMPLES ---")
s = "abcdefgh"

print(f"s[0:4]: {s[0:4]}")      # abcd
print(f"s[2:6]: {s[2:6]}")      # cdef
print(f"s[:3]: {s[:3]}")        # abc
print(f"s[3:]: {s[3:]}")        # defgh
print(f"s[::2]: {s[::2]}")      # aceg
print(f"s[::-1]: {s[::-1]}")    # reverse


# Slicing never throws IndexError - even if stop is bigger than length
print("\n--- SAFE SLICING ---")
s = "abc"
print(f"s[0:100]: {s[0:100]}")  # 'abc' (safe)


# ============================================================================
# 5) STRING IMMUTABILITY
# ============================================================================
# Once a string is created, you cannot change its characters in place

print("\n--- STRING IMMUTABILITY ---")
s = "hello"
try:
    s[0] = "H"
except TypeError as e:
    print(f"Error: TypeError - {e}")


# Correct way: create a new string
print("\n--- CORRECT WAY TO MODIFY STRING ---")
s = "hello"
s2 = "H" + s[1:]
print(f"Original: hello, New: {s2}")


# ============================================================================
# 6) USEFUL STRING METHODS
# ============================================================================

# 6.1 split() - break string into a list
print("\n--- SPLIT() METHOD ---")
msg = "I love python"
print(f"msg.split(): {msg.split()}")      # ['I', 'love', 'python']

csv = "a,b,c,d"
print(f"csv.split(','): {csv.split(',')}")  # ['a', 'b', 'c', 'd']


# 6.2 partition() - split into 3 parts (first separator only)
# Returns: (before, separator, after)
print("\n--- PARTITION() METHOD ---")
email = "user@gmail.com"
print(f"email.partition('@'): {email.partition('@')}")

path = "home/user/docs"
print(f"path.partition('/'): {path.partition('/')}")


# ============================================================================
# 7) STRING CHECKING METHODS (Boolean Methods)
# ============================================================================
# These return True or False

print("\n--- ISNUMERIC() ---")
print(f"'123'.isnumeric(): {'123'.isnumeric()}")       # True
print(f"'12.3'.isnumeric(): {'12.3'.isnumeric()}")     # False
print(f"'abc'.isnumeric(): {'abc'.isnumeric()}")       # False


print("\n--- ISALNUM() ---")
print(f"'abc123'.isalnum(): {'abc123'.isalnum()}")     # True
print(f"'abc 123'.isalnum(): {'abc 123'.isalnum()}")   # False (space)


print("\n--- ISLOWER() AND ISUPPER() ---")
print(f"'hello'.islower(): {'hello'.islower()}")       # True
print(f"'Hello'.islower(): {'Hello'.islower()}")       # False
print(f"'HELLO'.isupper(): {'HELLO'.isupper()}")       # True
print(f"'123'.isupper(): {'123'.isupper()}")           # False


print("\n--- ISALPHA() - LETTERS ONLY ---")
print(f"'Python'.isalpha(): {'Python'.isalpha()}")           # True
print(f"'Python3'.isalpha(): {'Python3'.isalpha()}")         # False
print(f"'Hello World'.isalpha(): {'Hello World'.isalpha()}") # False (space)


print("\n--- ISSPACE() - SPACES/TABS/NEWLINES ONLY ---")
print(f"'   '.isspace(): {'   '.isspace()}")          # True
print(f"'\\n\\t'.isspace(): {repr('\\n\\t')}, isspace: {'\\n\\t'.isspace()}")  # True
print(f"' a '.isspace(): {' a '.isspace()}")          # False


print("\n--- ENDSWITH() - CHECK ENDING ---")
filename = "report.pdf"
print(f"filename.endswith('.pdf'): {filename.endswith('.pdf')}")   # True
print(f"filename.endswith('.docx'): {filename.endswith('.docx')}")  # False


# ============================================================================
# 8) BUILT-IN REGULAR EXPRESSIONS
# ============================================================================
# Python supports regex using the built-in 're' module

import re

print("\n--- REGEX: FIND EMAIL ADDRESSES ---")
text = "Contact me at user123@gmail.com or admin@company.org"
emails = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
print(f"Emails found: {emails}")


print("\n--- REGEX: VALIDATE PHONE NUMBER ---")
phone = "1234567890"
is_valid = bool(re.fullmatch(r"\d{10}", phone))
print(f"Is '{phone}' valid? {is_valid}")  # True

phone2 = "123-456-7890"
is_valid2 = bool(re.fullmatch(r"\d{10}", phone2))
print(f"Is '{phone2}' valid? {is_valid2}")  # False


# ============================================================================
# 9) LISTS - MUTABLE COLLECTIONS
# ============================================================================
# Lists can store anything, including mixed types and nested lists

print("\n--- LIST WITH MIXED TYPES ---")
lst = [1, "two", 3.0, True]
print(f"Mixed list: {lst}")


# ============================================================================
# 10) CORE LIST METHODS
# ============================================================================

# append() - add one item
print("\n--- APPEND() ---")
a = [1, 2, 3]
a.append(4)
print(f"After append(4): {a}")


# extend() - add many items
print("\n--- EXTEND() ---")
a = [1, 2, 3]
a.extend([4, 5, 6])
print(f"After extend([4, 5, 6]): {a}")


# append can create nesting
print("\n--- APPEND CREATES NESTING ---")
a = [1, 2, 3]
a.append([4, 5])
print(f"After append([4, 5]): {a}")


# insert() - insert at index
print("\n--- INSERT() ---")
a = [10, 20, 40]
a.insert(2, 30)
print(f"After insert(2, 30): {a}")


# index() - find first index
print("\n--- INDEX() ---")
a = ["x", "y", "z", "y"]
print(f"Index of 'y': {a.index('y')}")

try:
    print(a.index("not_here"))
except ValueError as e:
    print(f"Error: ValueError - {e}")


# pop() - remove and return (permanent)
print("\n--- POP() ---")
a = [10, 20, 30, 40]
removed = a.pop()
print(f"Removed: {removed}, Now list: {a}")

removed2 = a.pop(1)
print(f"Removed index 1: {removed2}, Now list: {a}")


# remove() - remove first matching value
print("\n--- REMOVE() ---")
a = [1, 2, 2, 3]
a.remove(2)
print(f"After remove(2): {a}")


# reverse() - reverse in place
print("\n--- REVERSE() ---")
a = [3, 1, 4, 2]
a.reverse()
print(f"After reverse(): {a}")


# sort() - sort in place
print("\n--- SORT() ---")
b = [3, 1, 4, 2]
b.sort()
print(f"After sort(): {b}")


# Common mistake: sort() returns None
print("\n--- COMMON MISTAKE: SORT() RETURNS NONE ---")
a = [3, 2, 1]
result = a.sort()
print(f"a: {a}")
print(f"result: {result}")  # None


# ============================================================================
# 11) NESTING LISTS - MATRIX
# ============================================================================
# A matrix is often represented as a list of lists

print("\n--- MATRIX ACCESS ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(f"matrix[0]: {matrix[0]}")      # First row
print(f"matrix[0][1]: {matrix[0][1]}")  # Element at row 0, col 1


# Looping through a matrix
print("\n--- LOOP THROUGH MATRIX ---")
for row in matrix:
    for value in row:
        print(value, end=" ")
print()  # newline


# ============================================================================
# 12) LIST COMPREHENSIONS
# ============================================================================
# A compact way to build lists
# Syntax: [expression for item in iterable if condition]

print("\n--- BASIC LIST COMPREHENSION ---")
squares = [x**2 for x in range(1, 6)]
print(f"Squares: {squares}")


print("\n--- LIST COMPREHENSION WITH CONDITION ---")
evens = [x for x in range(1, 21) if x % 2 == 0]
print(f"Even numbers 1-20: {evens}")


print("\n--- LIST COMPREHENSION FROM STRING ---")
chars = [ch for ch in "python"]
print(f"Characters: {chars}")


# ============================================================================
# 13) COPYING LISTS
# ============================================================================

# b = a does NOT copy a list - it points to the same list
print("\n--- WRONG WAY: ASSIGNMENT (NOT COPY) ---")
a = [1, 2, 3]
b = a
b.append(99)
print(f"a: {a}")  # [1, 2, 3, 99]
print(f"b: {b}")  # [1, 2, 3, 99]


# Correct way: use copy()
print("\n--- CORRECT WAY: USE COPY() ---")
a = [1, 2, 3]
b = a.copy()
b.append(99)
print(f"a: {a}")  # [1, 2, 3]
print(f"b: {b}")  # [1, 2, 3, 99]


# ============================================================================
# 14) STRINGS vs LISTS - KEY DIFFERENCES
# ============================================================================

print("\n--- STRINGS vs LISTS COMPARISON ---")

# Similarities
print("SIMILARITIES:")
print("  - len()")
print("  - indexing")
print("  - slicing")
print("  - looping")

# Differences
print("\nDIFFERENCES:")
print("  - String: IMMUTABLE (cannot change)")
print("  - List: MUTABLE (can change)")

# String: Cannot modify
print("\n--- IMMUTABLE STRING ---")
s = "hello"
try:
    s[0] = "H"
except TypeError as e:
    print(f"String error: TypeError - {e}")


# List: Can modify
print("\n--- MUTABLE LIST ---")
lst = ["h", "e", "l", "l", "o"]
lst[0] = "H"
print(f"Modified list: {lst}")


# ============================================================================
# SUMMARY OF KEY CONCEPTS
# ============================================================================
"""
1. STRINGS: Immutable text sequences
   - Cannot change characters in place
   - Use slicing and string methods to create new strings
   
2. LISTS: Mutable collections
   - Can add, remove, or modify items
   - Support many methods (append, extend, pop, sort, etc.)
   
3. INDEXING: 0-based, access with s[i] or lst[i]
   
4. SLICING: s[start:stop:step]
   - Safe (never throws IndexError)
   - Omitting values uses defaults
   
5. STRING METHODS: split(), partition(), isalnum(), isalpha(), endswith(), etc.
   
6. LIST METHODS: append(), extend(), insert(), pop(), remove(), sort(), reverse(), etc.
   
7. MATRIX: Nested lists - use lst[row][col] to access
   
8. LIST COMPREHENSION: [expr for item in iterable if condition]
   
9. COPYING: Use list.copy() to create independent copy
   
10. KEY DIFFERENCE: Strings are immutable, Lists are mutable
"""

print("\nSession 3 examples completed successfully!")
