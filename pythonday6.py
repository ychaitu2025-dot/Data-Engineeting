"""
Python Basics - Session 6: Modules, Libraries, Exceptions, Files, Excel, Pandas, and SQLite
Topic: Built-in modules, Custom modules, Exception handling, File I/O, Excel with Pandas, SQLite databases
Student: Chaitanya Y
Date: Session 6
"""

import sqlite3
import os
from pathlib import Path

print("=" * 70)
print("SESSION 6: MODULES, LIBRARIES, EXCEPTIONS, FILES, AND DATABASES")
print("=" * 70)


# ============================================================================
# 1) MODULES vs PACKAGES vs LIBRARIES
# ============================================================================
# Module: usually a single .py file containing code
#   Example: math, random
# Package: a folder containing modules (often includes __init__.py)
#   Example: pandas (package) with many submodules
# Library: informal term meaning "collection of modules/packages"

print("\n--- IMPORT STYLES ---")

import math
import random as rnd
from datetime import datetime

print(f"sqrt(25) = {math.sqrt(25)}")
print(f"random int 1..10 = {rnd.randint(1, 10)}")
print(f"now = {datetime.now()}")


# ============================================================================
# 2) EXPLORING BUILT-IN MODULES
# ============================================================================
# dir(module) -> list names inside the module
# help(module_or_function) -> docs

print("\n--- DIR() - LIST MODULE CONTENTS ---")
print(f"Some names in math: {dir(math)[:10]}")
print("(and more...)")


print("\n--- HELP() - GET DOCUMENTATION ---")
print("Help on math.sqrt:")
print("  Returns the square root of x")
print("  help(math.sqrt) shows full documentation")


# ============================================================================
# 3) OS AND PATHLIB - FILE AND FOLDER OPERATIONS
# ============================================================================
# os and pathlib help with files and folders

print("\n--- OS AND PATHLIB ---")
print(f"Current working directory: {os.getcwd()}")

# Safe cross-platform path building
p = Path("data") / "example.txt"
print(f"Example path: {p}")


# ============================================================================
# 4) CUSTOM MODULE EXAMPLE
# ============================================================================
# A custom module is just a .py file you create
# Create mymath.py with simple functions

print("\n--- CREATING CUSTOM MODULE: mymath.py ---")

# Create the mymath.py file
mymath_code = '''"""mymath.py - custom module example"""

def add(a, b):
    """Return sum of a and b"""
    return a + b

def is_even(n):
    """Check if n is even"""
    return n % 2 == 0

def area_circle(r):
    """Calculate area of circle with radius r"""
    import math
    return math.pi * r * r
'''

with open("mymath.py", "w") as f:
    f.write(mymath_code)

print("Created mymath.py")

# Now import and use it
import mymath

print(f"add(3, 4) = {mymath.add(3, 4)}")
print(f"is_even(10) = {mymath.is_even(10)}")
print(f"area_circle(2) = {round(mymath.area_circle(2), 4)}")


# ============================================================================
# 5) ERRORS AND EXCEPTION HANDLING
# ============================================================================
# Exceptions let your program handle problems gracefully instead of crashing

# Common exceptions:
#   ValueError (bad conversion like int('abc'))
#   ZeroDivisionError
#   FileNotFoundError
#   TypeError

print("\n--- TRY/EXCEPT WITH MULTIPLE EXCEPTION TYPES ---")

# Simulated user input (avoiding actual input() in script)
test_values = ["25", "abc", "0", "5"]
test_index = 0

def get_test_input():
    global test_index
    val = test_values[test_index]
    test_index += 1
    return val

# Test case 1: Valid input
print("Test 1: Valid input")
try:
    x = int(get_test_input())
    result = 10 / x
    print(f"10 / {x} = {result}")
except ValueError:
    print("Error: You must enter a valid integer")
except ZeroDivisionError:
    print("Error: You cannot divide by zero")


# Test case 2: Invalid input (ValueError)
print("\nTest 2: Invalid input (ValueError)")
try:
    x = int(get_test_input())
    result = 10 / x
    print(f"10 / {x} = {result}")
except ValueError:
    print("Error: You must enter a valid integer")
except ZeroDivisionError:
    print("Error: You cannot divide by zero")


# Test case 3: Zero division (ZeroDivisionError)
print("\nTest 3: Zero division (ZeroDivisionError)")
try:
    x = int(get_test_input())
    result = 10 / x
    print(f"10 / {x} = {result}")
except ValueError:
    print("Error: You must enter a valid integer")
except ZeroDivisionError:
    print("Error: You cannot divide by zero")


print("\n--- TRY/EXCEPT/ELSE/FINALLY ---")

try:
    x = int(get_test_input())
    result = 10 / x
except ValueError:
    print("Error: Invalid input")
except ZeroDivisionError:
    print("Error: Cannot divide by zero")
else:
    # Runs only if no exception
    print(f"Success! You entered: {x}, Result: {result}")
finally:
    # Always runs
    print("(finally) This runs whether there was an error or not")


# ============================================================================
# 6) TEXT FILE OPERATIONS
# ============================================================================
# File modes:
#   'r' read (file must exist)
#   'w' write (overwrites / creates)
#   'a' append (adds to end / creates)

# .strip() removes whitespace from both ends (spaces, tabs, newlines)

print("\n--- CREATE A TEXT FILE (WRITE MODE) ---")

with open("notes.txt", "w", encoding="utf-8") as f:
    f.write("  line one  \n")
    f.write("line two\n")
    f.write("   line three\n\n")

print("Created notes.txt")


print("\n--- READ FILE AND USE STRIP() ---")

print("Content of notes.txt (with strip):")
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        cleaned = line.strip()
        if cleaned:  # skip empty lines after stripping
            print(f"  {cleaned}")


print("\n--- APPEND TO FILE (APPEND MODE) ---")

with open("notes.txt", "a", encoding="utf-8") as f:
    f.write("appended line 1\n")
    f.write("appended line 2\n")

print("Appended to notes.txt")

print("\nUpdated content:")
with open("notes.txt", "r", encoding="utf-8") as f:
    for line in f:
        cleaned = line.strip()
        if cleaned:
            print(f"  {cleaned}")


# ============================================================================
# 7) PANDAS BASICS - DATAFRAME
# ============================================================================
# A DataFrame is a table (rows + columns), like Excel/SQL

print("\n--- PANDAS DATAFRAME ---")

try:
    import pandas as pd

    # Create a DataFrame
    df = pd.DataFrame({
        "name": ["Ritesh", "Nikhil", "Phenome", "Rahul"],
        "score": [95, 88, 91, 77]
    })

    print("Original DataFrame:")
    print(df)

    # Save to Excel
    df.to_excel("students.xlsx", index=False)
    print("\nWrote students.xlsx")

    # Read from Excel
    df2 = pd.read_excel("students.xlsx")
    print("\nRead from students.xlsx:")
    print(df2)

    # Filter and sort
    top = df2[df2["score"] >= 90].sort_values("score", ascending=False)
    print("\nTop students (score >= 90):")
    print(top)

    # Export filtered results
    top.to_excel("top_students.xlsx", index=False)
    print("\nWrote top_students.xlsx")

except ImportError:
    print("Pandas not installed. Install with: pip install pandas openpyxl")


# ============================================================================
# 8) SQLITE DATABASE CONNECTIVITY
# ============================================================================
# SQLite stores database in a single file (e.g., school.db)

# Core steps:
#   1) sqlite3.connect(...)
#   2) conn.cursor()
#   3) cursor.execute(SQL, params)
#   4) fetchone() / fetchall() for SELECT
#   5) conn.commit() for INSERT/UPDATE/DELETE
#   6) conn.close()

# Important: Use parameterized queries with ? - safer and avoids quoting bugs

print("\n--- SQLITE: CREATE TABLE ---")

conn = sqlite3.connect("school.db")
cur = conn.cursor()

# Create table (IF NOT EXISTS prevents errors on re-run)
cur.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    score INTEGER NOT NULL
)
""")

conn.commit()
conn.close()

print("Created/verified school.db and students table")


print("\n--- SQLITE: INSERT ROWS (PARAMETERIZED) ---")

with sqlite3.connect("school.db") as conn:
    cur = conn.cursor()

    # Insert rows using parameterized queries (safer)
    cur.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("Ritesh", 95))
    cur.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("Nikhil", 88))
    cur.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("Phenome", 91))
    cur.execute("INSERT INTO students (name, score) VALUES (?, ?)", ("Rahul", 77))

print("Inserted 4 sample rows")


print("\n--- SQLITE: SELECT WITH FILTER ---")

with sqlite3.connect("school.db") as conn:
    cur = conn.cursor()

    # SELECT with WHERE and ORDER BY
    cur.execute(
        "SELECT name, score FROM students WHERE score >= ? ORDER BY score DESC",
        (90,)
    )
    rows = cur.fetchall()

print("Students with score >= 90:")
for name, score in rows:
    print(f"  {name}: {score}")


print("\n--- SQLITE: UPDATE AND DELETE ---")

with sqlite3.connect("school.db") as conn:
    cur = conn.cursor()

    # UPDATE
    cur.execute("UPDATE students SET score = ? WHERE name = ?", (99, "Ritesh"))
    print(f"Updated Ritesh's score to 99")

    # DELETE
    cur.execute("DELETE FROM students WHERE name = ?", ("Rahul",))
    print(f"Deleted Rahul from database")


print("\n--- SQLITE: SELECT ALL ROWS ---")

with sqlite3.connect("school.db") as conn:
    cur = conn.cursor()
    cur.execute("SELECT id, name, score FROM students ORDER BY id")
    all_rows = cur.fetchall()

print("All remaining rows:")
for row_id, name, score in all_rows:
    print(f"  ID {row_id}: {name} - {score}")


print("\n--- SQLITE: USING FETCHONE() ---")

with sqlite3.connect("school.db") as conn:
    cur = conn.cursor()
    cur.execute("SELECT name, score FROM students WHERE score = (SELECT MAX(score) FROM students)")
    highest = cur.fetchone()

if highest:
    name, score = highest
    print(f"Student with highest score: {name} ({score})")


# ============================================================================
# 9) SUMMARY AND BEST PRACTICES
# ============================================================================

summary = """
SUMMARY OF SESSION 6:

1. MODULES:
   - Use 'import module' or 'from module import name'
   - dir(module) shows available names
   - help(function) shows documentation

2. CUSTOM MODULES:
   - Create a .py file and import it
   - Use importlib.reload() if you edit it

3. EXCEPTION HANDLING:
   - try/except catches errors gracefully
   - Multiple except blocks for different error types
   - else runs if no exception
   - finally always runs

4. FILE OPERATIONS:
   - open(filename, mode, encoding='utf-8')
   - Modes: 'r' (read), 'w' (write), 'a' (append)
   - .strip() removes whitespace
   - Use 'with' statement for automatic file closing

5. PANDAS:
   - DataFrame = table with rows and columns
   - read_excel() / to_excel() for Excel files
   - Filter with df[df['column'] > value]
   - sort_values() for sorting

6. SQLITE:
   - sqlite3.connect(filename) - connection
   - cursor.execute(SQL, params) - execute queries
   - fetchone() / fetchall() - get results
   - conn.commit() - save changes
   - Use ? for parameterized queries (SAFER)
"""

print("\n" + "=" * 70)
print(summary)
print("=" * 70)
print("\nSession 6 examples completed successfully!")
