"""
Python Basics - Session 5: Iterators, Generators, and Functional Tools
Topic: Iterables vs Iterators, iter() and next(), Generators with yield, map(), lambda, filter(), reduce()
Student: Chaitanya Y
Date: Session 5
"""

# ============================================================================
# KEY DEFINITIONS
# ============================================================================
# Iterable: something you can loop over (like a list/string)
# Iterator: the object that produces items one-by-one using __next__()
# Generator: an easy way to create an iterator using yield

print("=" * 70)
print("SESSION 5: ITERATORS, GENERATORS, AND FUNCTIONAL TOOLS")
print("=" * 70)


# ============================================================================
# 1) ITERABLES vs ITERATORS
# ============================================================================
# An ITERABLE is anything you can loop over using a for loop
# Examples: list, tuple, string, dict, set

# An ITERATOR is an object that:
#   - has __iter__() (returns itself)
#   - has __next__() (returns the next item)

# Important: An iterable is not always an iterator
# But you can GET an iterator from an iterable using iter()

print("\n--- ITERABLES EXAMPLE ---")
nums = [10, 20, 30]
for x in nums:
    print(x, end=" ")
print()

# String is also iterable
print("\nString is iterable:")
for ch in "hello":
    print(ch, end=" ")
print()


# ============================================================================
# 2) ITER() AND NEXT()
# ============================================================================
# iter(iterable) returns an ITERATOR
# next(iterator) returns the next item
# When there is nothing left, Python raises StopIteration

# Why don't we see StopIteration inside a for loop?
# Because for loops automatically catch StopIteration and stop cleanly

print("\n--- ITER() AND NEXT() ---")
nums = [1, 2, 3]
it = nums.__iter__()  # turn iterable into iterator

print(f"next(it): {next(it)}")   # 1
print(f"next(it): {next(it)}")   # 2
print(f"next(it): {next(it)}")   # 3

# Uncomment to see StopIteration
# print(next(it))  # would raise StopIteration


print("\n--- STRING IS ITERABLE BUT NOT ITERATOR ---")
s = "hello"
# next(s)  # would fail because s is not an iterator

it_s = iter(s)
print(f"next(it_s): {next(it_s)}")
print(f"next(it_s): {next(it_s)}")
print(f"next(it_s): {next(it_s)}")


# ============================================================================
# 3) GENERATORS AND YIELD
# ============================================================================
# A GENERATOR is a special type of iterator written like a function but uses yield

# Difference:
#   - return ends the function
#   - yield pauses the function and REMEMBERS STATE, so it can continue later

# Generators are used to PRODUCE VALUES ON THE FLY (memory efficient)

print("\n--- GENERATOR: CUBES (POWER OF 3) ---")

def gencubes(n):
    """Generate cubes of numbers from 0 to n-1"""
    for num in range(n):
        yield num**3

g = gencubes(5)
print(f"Generator object: {g}")

print("\nConsuming generator with for-loop:")
for x in gencubes(9):
    print(x, end=" ")
print()


# ============================================================================
# 4) FIBONACCI GENERATOR
# ============================================================================
print("\n--- FIBONACCI GENERATOR ---")

def genfibon(n):
    """Generate Fibonacci sequence up to n terms"""
    a, b = 1, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("First 12 Fibonacci numbers:")
for num in genfibon(12):
    print(num, end=" ")
print()


# Normal function that returns a list
print("\n--- FIBONACCI AS LIST FUNCTION ---")

def fibon_list(n):
    """Return Fibonacci sequence as a list"""
    a, b = 1, 1
    output = []
    for _ in range(n):
        output.append(a)
        a, b = b, a + b
    return output

print(f"First 10 Fibonacci numbers: {fibon_list(10)}")


# ============================================================================
# 5) USING NEXT() WITH A GENERATOR
# ============================================================================
# A generator is an iterator, so you can manually pull values using next()

print("\n--- USING NEXT() WITH GENERATOR ---")

def simple_gen():
    for x in range(3, 9):
        yield x

g = simple_gen()
print(f"next(g): {next(g)}")  # 3
print(f"next(g): {next(g)}")  # 4
print(f"next(g): {next(g)}")  # 5
print(f"next(g): {next(g)}")  # 6
print(f"next(g): {next(g)}")  # 7
print(f"next(g): {next(g)}")  # 8

# Uncomment to see StopIteration
# print(next(g))


# ============================================================================
# 6) MAP()
# ============================================================================
# map(function, iterable) applies a function to every element in an iterable

# In Python 3, map() returns a MAP OBJECT (an iterator)
# You often convert it to a list using list(map(...))

print("\n--- MAP(): TEMPERATURE CONVERSION ---")

def fahrenheit(T):
    return (float(9) / 5) * T + 32

def celsius(T):
    return (float(5) / 9) * (T - 32)

temp_f = [0, 22.5, 40, 100]

# Convert F -> C
temp_c = list(map(celsius, temp_f))
print(f"Fahrenheit: {temp_f}")
print(f"Celsius: {temp_c}")

# Convert back C -> F
temp_back = list(map(fahrenheit, temp_c))
print(f"Back to Fahrenheit: {temp_back}")


# ============================================================================
# 7) LAMBDA FUNCTIONS
# ============================================================================
# A lambda is a small one-time function

# Use it when:
#   - the function is simple
#   - you don't want to define a full def for a one-time use

# Syntax: lambda arguments: expression

print("\n--- LAMBDA WITH MAP ---")
lst = [1, 2, 3, 4, 5]
result = list(map(lambda x: x + 1, lst))
print(f"Original: {lst}")
print(f"After map(lambda x: x + 1, lst): {result}")


# ============================================================================
# 8) MAP() WITH MULTIPLE ITERABLES
# ============================================================================
# map() can take multiple iterables if your function takes multiple arguments

# Important: It stops at the shortest iterable length

print("\n--- MAP() WITH MULTIPLE ITERABLES ---")
a = [1, 2, 3, 4]
b = [5, 6, 7, 8]

result = list(map(lambda x, y: x + y, a, b))
print(f"a: {a}")
print(f"b: {b}")
print(f"map(lambda x, y: x + y, a, b): {result}")


# ============================================================================
# 9) FILTER()
# ============================================================================
# filter(function, iterable) keeps only elements where function returns True

# Like map, it returns an iterator in Python 3
# Often convert to list: list(filter(...))

print("\n--- FILTER(): EVEN NUMBERS ---")

def even_check(num):
    return num % 2 == 0

lst = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(even_check, lst))
print(f"Original: {lst}")
print(f"Even numbers: {even_numbers}")


print("\n--- FILTER() WITH LAMBDA ---")
even_numbers_lambda = list(filter(lambda x: x % 2 == 0, lst))
print(f"Even numbers (with lambda): {even_numbers_lambda}")


print("\n--- FILTER(): WORDS WITH LENGTH >= 6 ---")
words = ["ruchik", "Nikhil", "phoebee", "swapna"]
long_words = list(filter(lambda w: len(w) >= 6, words))
print(f"All words: {words}")
print(f"Words with length >= 6: {long_words}")


# ============================================================================
# 10) REDUCE()
# ============================================================================
# reduce(function, iterable) repeatedly applies a function to produce ONE FINAL VALUE

# You must import it:
# from functools import reduce

# Mental model:
# If the list is [s1, s2, s3, s4], then reduce does:
#   f(s1, s2) -> result1
#   f(result1, s3) -> result2
#   f(result2, s4) -> final

from functools import reduce

print("\n--- REDUCE(): STRING CONCATENATION ---")
names = ['kota', 'ruchik', 'joey', 'tribiani']
result = reduce(lambda a, b: a + b, names)
print(f"Names: {names}")
print(f"Concatenated: {result}")


print("\n--- REDUCE(): FIND MAXIMUM ---")
max_find = lambda a, b: a if a > b else b
lst = [47, 49, 42, 55, 56]
max_value = reduce(max_find, lst)
print(f"Numbers: {lst}")
print(f"Maximum: {max_value}")


print("\n--- REDUCE(): SUM OF NUMBERS ---")
numbers = [1, 2, 3, 4, 5]
total = reduce(lambda a, b: a + b, numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")


# ============================================================================
# 11) COMBINING MAP, FILTER, REDUCE
# ============================================================================
# You can chain these functional tools together

print("\n--- COMBINING MAP, FILTER, REDUCE ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Step 1: Square all numbers
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"After map(square): {squared}")

# Step 2: Keep only even squares
even_squared = list(filter(lambda x: x % 2 == 0, squared))
print(f"After filter(even): {even_squared}")

# Step 3: Sum them all
total = reduce(lambda a, b: a + b, even_squared)
print(f"Sum: {total}")


# ============================================================================
# 12) COMMON MISTAKES AND TIPS
# ============================================================================

print("\n--- COMMON MISTAKE 1: MAP/FILTER RETURN ITERATORS ---")
print("If you print them directly, you may see: <map object at ...>")
print("Fix: wrap with list(...) to view results")

lst = [1, 2, 3, 4, 5]
result_map = map(lambda x: x * 2, lst)
print(f"Without list(): {result_map}")
print(f"With list(): {list(result_map)}")


print("\n--- COMMON MISTAKE 2: DON'T NAME A VARIABLE 'list' ---")
print("Because it overwrites Python's built-in list() function")
print("Use names like: lst, numbers, items, etc.")


# ============================================================================
# 13) PRACTICAL EXAMPLE: DATA PROCESSING
# ============================================================================
print("\n--- PRACTICAL EXAMPLE: PROCESS TEMPERATURE DATA ---")

# Raw data: [(city, fahrenheit), ...]
temp_data = [
    ("New York", 75),
    ("Los Angeles", 85),
    ("Chicago", 60),
    ("Houston", 95),
    ("Phoenix", 105)
]

print("\nOriginal data (City, Fahrenheit):")
for city, temp in temp_data:
    print(f"  {city}: {temp}F")

# Step 1: Convert F to C using map
convert_to_c = lambda t: (5/9) * (t - 32)
temps_celsius = list(map(lambda x: (x[0], round(convert_to_c(x[1]), 2)), temp_data))

print("\nAfter conversion to Celsius:")
for city, temp in temps_celsius:
    print(f"  {city}: {temp}C")

# Step 2: Filter hot cities (> 25C)
hot_cities = list(filter(lambda x: x[1] > 25, temps_celsius))
print("\nHot cities (> 25C):")
for city, temp in hot_cities:
    print(f"  {city}: {temp}C")

# Step 3: Calculate average temperature
avg_temp = reduce(lambda a, b: a + b[1], hot_cities, 0) / len(hot_cities) if hot_cities else 0
print(f"\nAverage temperature of hot cities: {round(avg_temp, 2)}C")


# ============================================================================
# SUMMARY OF KEY CONCEPTS
# ============================================================================
"""
1. ITERABLES vs ITERATORS:
   - Iterable: anything you can loop over (list, string, dict, etc.)
   - Iterator: object with __iter__() and __next__()
   
2. ITER() AND NEXT():
   - iter(iterable) converts iterable to iterator
   - next(iterator) gets next item
   - StopIteration is raised when done
   
3. GENERATORS:
   - Special iterators using yield instead of return
   - yield pauses and remembers state
   - Memory efficient for large sequences
   
4. MAP():
   - Applies function to every element
   - Returns iterator (convert to list to view)
   - Can work with multiple iterables
   
5. LAMBDA:
   - Small one-time function
   - Syntax: lambda args: expression
   - Often used with map/filter/reduce
   
6. FILTER():
   - Keeps only elements where function returns True
   - Returns iterator (convert to list to view)
   
7. REDUCE():
   - Repeatedly applies function to produce ONE value
   - Must import from functools
   - Useful for: sum, max, concatenation, etc.
   
8. CHAINING:
   - Can combine map() -> filter() -> reduce()
   - Build complex data pipelines
"""

print("\nSession 5 examples completed successfully!")
