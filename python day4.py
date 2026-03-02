"""
Python Basics - Session 4: Tuples, Sets, Dictionaries & Functions
Topic: Tuples, Sets, Dictionaries, Dictionary Comprehensions, Shallow/Deep Copy, Functions, Prime Number Check
Student: Chaitanya Y
Date: Session 4
"""

# ============================================================================
# 1) TUPLES
# ============================================================================
# Tuples are similar to lists, but the MAJOR DIFFERENCE is:
#   - Tuple is IMMUTABLE (cannot be changed after creation)
#   - Ordered collection (keeps order)
#   - Can contain mixed object types

# When to use tuples:
#   - When data should not change (e.g., days of week, coordinates, employee_id)
#   - When you want data integrity (safe from accidental changes)

print("--- BASIC TUPLE ---")
t = (1, 2, 3)
print(f"Basic tuple: {t}")
print(f"Type: {type(t)}")


# 1.1 Constructing tuples
print("\n--- CONSTRUCTING TUPLES ---")

# Tuple with mixed types
t = ("one", 2, "one")
print(f"Mixed tuple: {t}")
print(f"Type: {type(t)}")


# Single-item tuple (important!)
a = (5,)
b = (5)
print(f"\na = (5,) is tuple: {type(a)}")
print(f"b = (5) is NOT tuple: {type(b)}")  # This is just an int!


# Convert list to tuple
lst = [1, 2, 3]
t = tuple(lst)
print(f"\nList converted to tuple: {t}")


# 1.2 Indexing and slicing (same as lists)
print("\n--- TUPLE INDEXING AND SLICING ---")
t = ("one", 2, "one", 99)
print(f"t[1]: {t[1]}")           # indexing
print(f"t[1:3]: {t[1:3]}")       # slicing
print(f"t[::-1]: {t[::-1]}")     # reverse


# 1.3 Basic tuple methods
print("\n--- TUPLE METHODS ---")
t = ("one", 2, "one", 99)
print(f"t.index(2): {t.index(2)}")
print(f"t.count('one'): {t.count('one')}")


# 1.4 Immutability (cannot modify)
print("\n--- TUPLE IMMUTABILITY ---")
t = (10, 20, 30)
try:
    t[0] = 99
except TypeError as e:
    print(f"Error: TypeError - {e}")


# Example: Employee record (tuple for safety)
print("\n--- EMPLOYEE RECORD EXAMPLE ---")
employee = ("E1023", "Ruchik", "Engineering")
print(f"Employee ID: {employee[0]}")

try:
    employee[0] = "E9999"
except TypeError as e:
    print(f"Cannot change employee_id: TypeError - Cannot modify tuple")


# Workaround: Convert to list, modify, convert back
print("\n--- WORKAROUND: CONVERT TO LIST, MODIFY, CONVERT BACK ---")
x = (1, 2, 3)
print(f"Original tuple: {x}")
temp_list = list(x)
temp_list.append(4)
x = tuple(temp_list)
print(f"Modified tuple: {x}")


# ============================================================================
# 2) SETS
# ============================================================================
# A SET is:
#   - Unordered collection
#   - Stores UNIQUE elements (no duplicates)
#   - Great for removing duplicates, membership testing, set operations

print("\n--- BASIC SET ---")
x = set()
print(f"Empty set: {x}, Type: {type(x)}")

y = {1, 2, 3}
print(f"Set with values: {y}, Type: {type(y)}")

empty_dict = {}
print(f"Empty dict: {empty_dict}, Type: {type(empty_dict)}")  # This is a dict!


# 2.2 Adding elements: add()
print("\n--- ADDING ELEMENTS TO SET ---")
x = set()
x.add(3)
x.add(2)
x.add(3)  # duplicate, will not be added again
print(f"After adding 3, 2, 3: {x}")


# 2.3 Sets remove duplicates automatically
print("\n--- REMOVE DUPLICATES WITH SET ---")
l = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
print(f"Original list: {l}")
print(f"Unique values: {set(l)}")


# 2.4 Safe removal: discard() vs remove()
# - discard(x) does nothing if x not present
# - remove(x) raises KeyError if x not present
print("\n--- DISCARD() VS REMOVE() ---")
s = {1, 2, 3}
s.discard(5)  # safe
print(f"After discard(5): {s}")

try:
    s.remove(5)
except KeyError as e:
    print(f"remove(5) error: KeyError - {e}")


# 2.5 pop() and clear()
# - pop() removes and returns an ARBITRARY element
# - clear() removes everything
print("\n--- POP() AND CLEAR() ---")
s = {1, 2, 3, 5, 6, 7}
removed = s.pop()
print(f"Removed by pop(): {removed}")
print(f"Now: {s}")

s.clear()
print(f"After clear(): {s}")


# ============================================================================
# 3) DICTIONARIES
# ============================================================================
# A dictionary (dict) stores data as KEY -> VALUE pairs

# Key properties:
#   - Keys must be UNIQUE
#   - Keys must be HASHABLE (immutable types like str, int, tuple)
#   - Values can be anything (numbers, lists, dicts, objects)

print("\n--- BASIC DICTIONARY ---")
my_dict = {"key1": 123, "key2": [12, 23, 33], "key3": ["item0", "item1", "item2"]}
print(f"Dictionary: {my_dict}")


# Accessing values by key
print("\n--- ACCESSING VALUES ---")
print(f"my_dict['key1']: {my_dict['key1']}")
print(f"my_dict['key3'][0]: {my_dict['key3'][0]}")
print(f"my_dict['key3'][0].upper(): {my_dict['key3'][0].upper()}")


# Duplicate keys overwrite
print("\n--- DUPLICATE KEYS OVERWRITE ---")
d = {"key": "first", "key": "second"}
print(f"Dictionary with duplicate keys: {d}")


# 3.2 Creating keys by assignment
print("\n--- CREATING KEYS BY ASSIGNMENT ---")
d = {}
d["animal"] = "joey"
d["answer"] = 42
print(f"Dictionary: {d}")


# 3.3 Nesting dictionaries
print("\n--- NESTED DICTIONARIES ---")
nested = {"key1": {"nestkey": {"subnestkey": 123}}}
print(f"Nested access: {nested['key1']['nestkey']['subnestkey']}")


# 3.4 Dictionary methods: keys(), values(), items()
print("\n--- DICTIONARY METHODS ---")
d = {"key1": 1, "key2": 2, "key3": 3}
print(f"keys: {list(d.keys())}")
print(f"values: {list(d.values())}")
print(f"items: {list(d.items())}")


# ============================================================================
# 4) DICTIONARY COMPREHENSIONS
# ============================================================================
# Just like list comprehensions, you can build dictionaries quickly

print("\n--- DICTIONARY COMPREHENSION ---")
squares = {x: x**2 for x in range(1, 11)}
print(f"Squares (1-10): {squares}")


# ============================================================================
# 5) SHALLOW COPY vs DEEP COPY
# ============================================================================
# Copying matters when you have nested structures

import copy

print("\n--- SHALLOW COPY ON FLAT LIST ---")
original = [1, 2, 3, 4]
shallow = copy.copy(original)
shallow[0] = 12

print(f"original: {original}")
print(f"shallow : {shallow}")


print("\n--- SHALLOW COPY WITH NESTED LIST ---")
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0][0] = 99

print(f"original: {original}")
print(f"shallow : {shallow}")
print("Notice both changed because inner list is shared!")


print("\n--- DEEP COPY WITH NESTED LIST ---")
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0][0] = 99

print(f"original: {original}")
print(f"deep    : {deep}")
print("Notice original did NOT change - inner lists are independent!")


# ============================================================================
# 6) FUNCTIONS
# ============================================================================
# A FUNCTION is reusable code

# Why functions?
#   - Avoid repeating code
#   - Make code organized and readable
#   - Makes testing and debugging easier

# Syntax:
# def function_name(arg1, arg2):
#     """docstring"""
#     # body
#     return value

print("\n--- FUNCTION: PRINT MULTIPLICATION TABLE ---")

def print_num(n):
    """Print multiples of n from 1*n to n*n."""
    for i in range(1, n + 1):
        print(i * n, end=" ")
    print()  # newline

print("Multiplication table for 5:")
print_num(5)


# 6.2 print vs return
print("\n--- PRINT VS RETURN ---")

def func_with_print():
    print("Hello")

def func_with_return():
    return "Hello"

a = func_with_print()
b = func_with_return()

print(f"a = {a}")  # None
print(f"b = {b}")  # Hello


# 6.3 Example: Add numbers (return)
print("\n--- FUNCTION: ADD NUMBERS ---")

def add_num(num1, num2):
    """Return the sum of num1 and num2."""
    return num1 + num2

result = add_num(5, 6)
print(f"result: {result}")
print(f"result + 5: {result + 5}")


# Common mistake: using print instead of return
print("\n--- COMMON MISTAKE: PRINT INSTEAD OF RETURN ---")

def add_num_print(num1, num2):
    print(num1 + num2)

x = add_num_print(5, 6)
print(f"x is: {x}")

try:
    print(x + 6)
except TypeError as e:
    print(f"Error: TypeError - {e}")


# ============================================================================
# 7) PRIME NUMBER FUNCTION EXAMPLE
# ============================================================================
# A number is PRIME if it is divisible only by 1 and itself

# Important: We use a for-else pattern:
#   - If loop finds a divisor -> break -> not prime
#   - If loop finishes without break -> else runs -> prime

print("\n--- PRIME NUMBER CHECK FUNCTION ---")

def is_prime(num):
    """Check if num is prime. Prints 'prime' or 'not prime'."""
    if num < 2:
        print("not prime")
        return

    for n in range(2, num):
        if num % n == 0:
            print("not prime")
            break
    else:
        print("prime")

print("Testing is_prime():")
print("Is 9 prime? ", end="")
is_prime(9)

print("Is 13 prime? ", end="")
is_prime(13)

print("Is 1 prime? ", end="")
is_prime(1)

print("Is 2 prime? ", end="")
is_prime(2)

print("Is 17 prime? ", end="")
is_prime(17)


# ============================================================================
# SUMMARY OF KEY CONCEPTS
# ============================================================================
"""
1. TUPLES: Immutable ordered collections
   - Use (1, 2, 3) or just 1, 2, 3
   - Single item needs trailing comma: (5,)
   - Support indexing and slicing like lists
   - Cannot be modified (immutable)
   
2. SETS: Unordered collections of unique elements
   - Use {1, 2, 3} or set() for empty
   - Automatically removes duplicates
   - Great for: removing duplicates, membership testing
   - Methods: add(), discard(), remove(), pop(), clear()
   
3. DICTIONARIES: Key -> Value pairs
   - Use {"key": value} or d[key] = value
   - Keys must be unique and hashable
   - Values can be anything
   - Methods: keys(), values(), items()
   
4. DICTIONARY COMPREHENSION: {key: value for item in iterable if condition}
   
5. COPYING:
   - Shallow copy: copy.copy() - nested objects are shared
   - Deep copy: copy.deepcopy() - nested objects are independent
   
6. FUNCTIONS:
   - def function_name(args): ... return value
   - print() shows output but returns None
   - return sends value back to caller
   
7. FOR-ELSE: else runs if loop finishes without break
   - Used in prime number checking
"""

print("\nSession 4 examples completed successfully!")
