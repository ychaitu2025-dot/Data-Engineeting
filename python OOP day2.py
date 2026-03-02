"""
Python OOP - Session 2: Advanced OOP Concepts
Topic: Encapsulation, Composition, Decorator Pattern, Polymorphism/Duck Typing, Class vs Instance Variables, @classmethod/@staticmethod, Dataclasses, SRP
Student: Chaitanya Y
Date: OOP Session 2
"""

from dataclasses import dataclass

print("=" * 70)
print("OOP SESSION 2: ADVANCED OOP CONCEPTS")
print("=" * 70)


# ============================================================================
# 1) ENCAPSULATION - CONTROLLING DATA ACCESS
# ============================================================================
# Encapsulation bundles DATA (attributes) and BEHAVIOR (methods) inside a class
# and controls how data is accessed/updated

print("\n--- ENCAPSULATION: PROTECTING PRIVATE DATA ---")

class BankAccount:
    """Bank account with encapsulated balance"""
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private-ish with name mangling

    def deposit(self, amount):
        """Safely deposit money with validation"""
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        print(f"Deposited {amount}. New balance: {self.__balance}")

    def withdraw(self, amount):
        """Safely withdraw money with validation"""
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        print(f"Withdrew {amount}. New balance: {self.__balance}")

    def get_balance(self):
        """Safe read access to balance"""
        return self.__balance


acct = BankAccount("Ritesh", 100)
acct.deposit(50)
acct.withdraw(30)
print(f"Final balance: {acct.get_balance()}")

# Direct access is blocked by name mangling
try:
    print(acct.__balance)
except AttributeError as e:
    print(f"Cannot access __balance directly (name mangling protects it)")

# Technically accessible via mangled name (not recommended)
print(f"Mangled name access: {acct._BankAccount__balance}")


# ============================================================================
# 2) COMPOSITION - "HAS-A" RELATIONSHIP
# ============================================================================
# Composition means a class CONTAINS another object and uses it
#
# Inheritance = "is-a" (Dog is an Animal)
# Composition = "has-a" (Car has an Engine)

print("\n--- COMPOSITION: HAS-A RELATIONSHIP ---")

class Engine:
    """Simple engine class"""
    def start(self):
        return "Engine started"

    def stop(self):
        return "Engine stopped"

class Car:
    """Car that CONTAINS an Engine (composition)"""
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()  # composition: car HAS an engine

    def start_car(self):
        return f"{self.brand}: {self.engine.start()}"

    def stop_car(self):
        return f"{self.brand}: {self.engine.stop()}"

car = Car("Toyota")
print(car.start_car())
print(car.stop_car())


# ============================================================================
# 3) DECORATOR PATTERN - DYNAMIC EXTENSION WITH render()
# ============================================================================
# The Decorator Pattern (OOP pattern):
#   - Wrap an object
#   - Forward calls to wrapped object
#   - Add extra behavior
#
# This is NOT the same as @decorator syntax!

print("\n--- DECORATOR PATTERN: WRAPPING WITH render() ---")

class Text:
    """Base text class"""
    def render(self):
        return "Hello"

class BoldWrapper:
    """Wrapper that adds bold formatting"""
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def render(self):
        return f"<b>{self.wrapped.render()}</b>"

class ItalicWrapper:
    """Wrapper that adds italic formatting"""
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def render(self):
        return f"<i>{self.wrapped.render()}</i>"

class UnderlineWrapper:
    """Wrapper that adds underline formatting"""
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def render(self):
        return f"<u>{self.wrapped.render()}</u>"

# Create text
simple = Text()
print(f"Simple: {simple.render()}")

# Wrap with bold
bold = BoldWrapper(simple)
print(f"Bold: {bold.render()}")

# Wrap with italic
italic = ItalicWrapper(simple)
print(f"Italic: {italic.render()}")

# Chain multiple wrappers
italic_bold = ItalicWrapper(BoldWrapper(Text()))
print(f"Italic + Bold: {italic_bold.render()}")

# Triple wrap
triple = UnderlineWrapper(ItalicWrapper(BoldWrapper(Text())))
print(f"Bold + Italic + Underline: {triple.render()}")


# ============================================================================
# 4) POLYMORPHISM AND DUCK TYPING
# ============================================================================
# Polymorphism: same method name, different behavior
# Duck typing: we care about behavior, not exact type
# "If it walks like a duck and quacks like a duck, it's a duck"

print("\n--- POLYMORPHISM: SAME METHOD, DIFFERENT BEHAVIOR ---")

class Dog:
    def speak(self):
        return "Woof"

class Cat:
    def speak(self):
        return "Meow"

class Bird:
    def speak(self):
        return "Chirp"

def make_speak(animal):
    """Function that works with ANY object that has speak() method"""
    print(f"Animal says: {animal.speak()}")

make_speak(Dog())
make_speak(Cat())
make_speak(Bird())


print("\n--- DUCK TYPING: ANYTHING WITH render() WORKS ---")

class CustomMessage:
    """Custom class with render() method"""
    def __init__(self, msg):
        self.msg = msg

    def render(self):
        return self.msg

# This works with our wrappers even though it's not Text!
msg = CustomMessage("Hi from duck typing")
print(f"Custom + Bold: {BoldWrapper(msg).render()}")

# Any object with render() can be wrapped
class HTMLTemplate:
    def render(self):
        return "<h1>Header</h1>"

html = HTMLTemplate()
print(f"HTML + Italic: {ItalicWrapper(html).render()}")


# ============================================================================
# 5) CLASS VARIABLES vs INSTANCE VARIABLES
# ============================================================================
# Instance variable: belongs to a specific object (self.value)
# Class variable: shared across all instances (MyClass.count)

print("\n--- CLASS VARIABLES vs INSTANCE VARIABLES ---")

class Student:
    total_students = 0  # CLASS variable (shared by all instances)

    def __init__(self, name):
        self.name = name  # INSTANCE variable (belongs to this object)
        Student.total_students += 1

    def get_info(self):
        return f"{self.name} (Total: {Student.total_students})"

s1 = Student("Ritesh")
s2 = Student("Nikhil")
s3 = Student("Phenome")

print(f"Student 1: {s1.get_info()}")
print(f"Student 2: {s2.get_info()}")
print(f"Student 3: {s3.get_info()}")
print(f"Class variable: {Student.total_students}")


print("\n--- COMMON BUG: SHADOWING CLASS VARIABLE ---")

class Counter:
    count = 0  # CLASS variable

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(f"Shared class variable: {Counter.count}")

# CAREFUL: This creates an INSTANCE variable, not modifying class variable!
c1.count = 999  # creates instance attribute
print(f"c1.count (instance shadow): {c1.count}")
print(f"Counter.count (real shared): {Counter.count}")
print(f"c2.count (still sees class variable): {c2.count}")


# ============================================================================
# 6) INSTANCE vs CLASS vs STATIC METHODS
# ============================================================================
# Instance method: uses self (instance data)
# Class method (@classmethod): uses cls (class data)
# Static method (@staticmethod): utility function in class namespace

print("\n--- INSTANCE, CLASS, AND STATIC METHODS ---")

class User:
    user_count = 0  # Class variable

    def __init__(self, name):
        self.name = name
        User.user_count += 1

    # Instance method
    def greet(self):
        """Instance method: uses self"""
        return f"Hello, I'm {self.name}"

    # Class method
    @classmethod
    def get_user_count(cls):
        """Class method: uses cls (class-level data)"""
        return cls.user_count

    # Class method as factory constructor
    @classmethod
    def from_email(cls, email):
        """Create user from email address"""
        name = email.split("@")[0]
        return cls(name)

    # Static method
    @staticmethod
    def is_valid_email(email):
        """Static method: utility function (no self, no cls)"""
        return "@" in email and "." in email

# Use instance method
u1 = User("Ritesh")
print(f"Instance method: {u1.greet()}")

# Use class method (factory pattern)
u2 = User.from_email("koya@example.com")
print(f"Created from email: {u2.greet()}")

# Use class method to access class variable
print(f"Class method: Total users = {User.get_user_count()}")

# Use static method
print(f"Static method: Is 'test@test.com' valid? {User.is_valid_email('test@test.com')}")
print(f"Static method: Is 'test' valid? {User.is_valid_email('test')}")


# ============================================================================
# 7) DATA CONVERSION - IMPLICIT vs EXPLICIT
# ============================================================================
# Implicit: Python converts automatically
# Explicit: you force conversion with int(), float(), str(), etc.

print("\n--- DATA CONVERSION ---")

# Implicit conversion
x = 5 + 2.0  # int + float -> float
print(f"5 + 2.0 = {x} (type: {type(x).__name__})")

# Explicit conversion
result = int("10") + 5
print(f"int('10') + 5 = {result}")

# Explicit conversion can fail
try:
    int("12.3")  # Can't directly convert "12.3" to int
except ValueError as e:
    print(f"Error: {e}")

# Must convert to float first, then to int
result = int(float("12.3"))
print(f"int(float('12.3')) = {result}")


# ============================================================================
# 8) DATACLASSES - AUTO-GENERATED __init__, __repr__
# ============================================================================
# @dataclass automatically generates __init__, __repr__, etc.
# Use __post_init__ for validation/normalization after __init__

print("\n--- DATACLASSES: AUTO-GENERATED METHODS ---")

@dataclass
class Person:
    """Simple dataclass"""
    name: str
    age: int

p1 = Person("Ritesh", 25)
print(f"Person: {p1}")
print(f"Name: {p1.name}, Age: {p1.age}")


print("\n--- DATACLASS WITH __post_init__ VALIDATION ---")

@dataclass
class PersonValidated:
    """Dataclass with validation"""
    name: str
    age: int

    def __post_init__(self):
        """Called after auto-generated __init__"""
        if self.age < 0:
            raise ValueError("Age cannot be negative")
        if self.age > 150:
            raise ValueError("Age seems unrealistic")
        # Normalize name
        self.name = self.name.strip().title()

p2 = PersonValidated("  ritesh  ", 25)
print(f"Validated person: {p2}")

# Test validation
try:
    PersonValidated("test", -5)
except ValueError as e:
    print(f"Validation error: {e}")


# ============================================================================
# 9) SINGLE RESPONSIBILITY PRINCIPLE (SRP)
# ============================================================================
# A class should have ONE responsibility (one reason to change)
# If doing too many unrelated things, split into multiple classes

print("\n--- SINGLE RESPONSIBILITY PRINCIPLE ---")

# GOOD: One responsibility per class
class Report:
    """Responsibility: Generate report content"""
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def generate(self):
        """Generate the report text"""
        return f"=== {self.title} ===\n{self.content}"

class ReportSaver:
    """Responsibility: Save report to file"""
    def save_to_file(self, report, filename):
        """Save report to file"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(report.generate())
        print(f"Report saved to {filename}")

class ReportPrinter:
    """Responsibility: Print report to console"""
    def print_report(self, report):
        """Print report to console"""
        print(report.generate())

# Usage
report = Report("Weekly Update", "Completed: OOP Session 2")
ReportSaver().save_to_file(report, "report.txt")
ReportPrinter().print_report(report)


# ============================================================================
# 10) REAL-WORLD EXAMPLE: COMBINING CONCEPTS
# ============================================================================
print("\n--- REAL-WORLD EXAMPLE: E-COMMERCE SYSTEM ---")

@dataclass
class Product:
    """Product with validation"""
    name: str
    price: float
    stock: int

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("Price cannot be negative")
        if self.stock < 0:
            raise ValueError("Stock cannot be negative")

class ShoppingCart:
    """Shopping cart with composition"""
    def __init__(self):
        self.items = []  # Composition: cart contains items

    def add_item(self, product, quantity):
        """Add product to cart"""
        if quantity > product.stock:
            raise ValueError("Not enough stock")
        self.items.append({"product": product, "quantity": quantity})
        print(f"Added {quantity}x {product.name}")

    def calculate_total(self):
        """Calculate total price"""
        return sum(item["product"].price * item["quantity"] for item in self.items)

    def get_summary(self):
        """Get cart summary"""
        return f"Items: {len(self.items)}, Total: ${self.calculate_total():.2f}"

# Use the system
p1 = Product("Laptop", 999.99, 10)
p2 = Product("Mouse", 29.99, 50)

cart = ShoppingCart()
cart.add_item(p1, 1)
cart.add_item(p2, 2)
print(f"Cart summary: {cart.get_summary()}")


# ============================================================================
# SUMMARY OF KEY CONCEPTS
# ============================================================================
summary = """
SUMMARY OF OOP SESSION 2:

1. ENCAPSULATION:
   - Bundle data and behavior together
   - Use __private for name mangling
   - Provide safe methods (getters/setters)

2. COMPOSITION:
   - "has-a" relationship (Car has Engine)
   - Include another object as attribute
   - Reuse code without inheritance

3. DECORATOR PATTERN:
   - Wrap objects to add behavior
   - Forward calls to wrapped object
   - Chain multiple decorators

4. POLYMORPHISM & DUCK TYPING:
   - Same method name, different behavior
   - Care about behavior, not exact type
   - "If it has the method, we can use it"

5. CLASS vs INSTANCE VARIABLES:
   - Instance: self.value (per object)
   - Class: MyClass.value (shared by all)
   - Avoid shadowing class variables

6. METHODS:
   - Instance method: uses self
   - @classmethod: uses cls (factory pattern)
   - @staticmethod: utility function

7. DATACLASSES:
   - @dataclass auto-generates __init__, __repr__
   - Use __post_init__ for validation
   - Cleaner code for data-heavy classes

8. SINGLE RESPONSIBILITY PRINCIPLE:
   - One class = one responsibility
   - One reason to change = one responsibility
   - Split if doing too many things

9. IMPLICIT vs EXPLICIT CONVERSION:
   - Implicit: Python handles automatically
   - Explicit: force with int(), str(), float()

10. WHEN TO USE WHAT:
    - Inheritance: "is-a" relationship (Animal -> Dog)
    - Composition: "has-a" relationship (Car -> Engine)
    - Decorator: add behavior dynamically
"""

print("\n" + "=" * 70)
print(summary)
print("=" * 70)
print("\nOOP Session 2 examples completed successfully!")
