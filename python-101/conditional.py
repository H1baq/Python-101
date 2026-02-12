"""
CONDITIONAL STATEMENTS & LOGICAL OPERATORS
==========================================

Conditionals let your program make decisions.

They run certain code only if a condition is True.
"""

# ==========================
# COMPARISON OPERATORS
# ==========================

"""
Comparison operators compare values and return True or False.
"""

print(3 > 4)   # False
print(3 < 4)   # True
print(3 == 4)  # False
print(4 == 4)  # True
print(3 != 4)  # True
print(3 >= 4)  # False
print(3 <= 4)  # True


# ==========================
# IF STATEMENT
# ==========================

"""
Basic syntax:

if condition:
    code to run
"""

age = 18

if age >= 18:
    print("You are an adult")


# IMPORTANT:
# Python uses indentation (usually 4 spaces) to define code blocks.


# ==========================
# IF...ELSE
# ==========================

age = 12

if age >= 18:
    print("You are an adult")
else:
    print("You are not an adult yet")


# ==========================
# IF...ELIF...ELSE
# ==========================

age = 15

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")


# You can use multiple elif statements:

age = 2

if age >= 65:
    print("Senior citizen")
elif age >= 30:
    print("Adult in your prime")
elif age >= 18:
    print("Young adult")
elif age >= 13:
    print("Teenager")
elif age >= 3:
    print("Young child")
else:
    print("Toddler or infant")


# ==========================
# TRUTHY & FALSY VALUES
# ==========================

"""
Every value in Python has a boolean meaning.

Falsy values:
- None
- False
- 0
- 0.0
- ""
- Empty collections ([], {}, ())

Everything else is usually truthy.
"""

print(bool(False))  # False
print(bool(0))      # False
print(bool(""))     # False

print(bool(True))   # True
print(bool(1))      # True
print(bool("Hi"))   # True


# ==========================
# LOGICAL OPERATORS
# ==========================

"""
Python has 3 logical operators:

and
or
not
"""


# --------------------------
# AND
# --------------------------

"""
Returns True only if BOTH conditions are True.
Stops early if first condition is False (short-circuiting).
"""

is_citizen = True
age = 25

if is_citizen and age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")


# Example of how 'and' works:

print(True and 5)   # 5
print(False and 5)  # False


# --------------------------
# OR
# --------------------------

"""
Returns True if AT LEAST ONE condition is True.
Stops early if first condition is True.
"""

age = 19
is_student = True

if age < 18 or is_student:
    print("You are eligible for a student discount")
else:
    print("You are not eligible for a discount")


# Example of how 'or' works:

print(19 or False)   # 19
print(0 or "Hello")  # "Hello"


# --------------------------
# NOT
# --------------------------

"""
Reverses (inverts) a boolean value.
"""

print(not True)     # False
print(not False)    # True
print(not 0)        # True
print(not "Hello")  # False


is_admin = False

if not is_admin:
    print("Access denied.")
else:
    print("Welcome, Admin!")


# ==========================
# SHORT-CIRCUITING
# ==========================

"""
Short-circuiting means Python stops evaluating
as soon as the result is determined.

AND:
- Stops if it finds False.

OR:
- Stops if it finds True.
"""


# ==========================
# SUMMARY
# ==========================

"""
- Comparison operators return True or False.
- if / elif / else control program flow.
- Indentation defines code blocks.
- Truthy values behave like True.
- Falsy values behave like False.
- and, or, not combine conditions.
- Python evaluates logical expressions left to right.
"""