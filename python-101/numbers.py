"""
NUMBERS IN PYTHON (Integers & Floats)
=====================================

Python has two main numeric data types:
1. int   -> Whole numbers (no decimal point)
2. float -> Numbers with decimal points
"""

# ==========================
# INTEGERS (int)
# ==========================

# Integers are whole numbers (positive or negative)
my_int_1 = 56
my_int_2 = -4

print(type(my_int_1))  # <class 'int'>
print(type(my_int_2))  # <class 'int'>

# Basic Arithmetic with Integers

a = 56
b = 12

print("Addition:", a + b)        # 68
print("Subtraction:", a - b)     # 44
print("Multiplication:", a * b)  # 672
print("Division:", a / b)        # 4.666... (returns float)


# ==========================
# FLOATS (float)
# ==========================

# Floats are numbers with decimal points
my_float_1 = 5.4
my_float_2 = -12.0

print(type(my_float_1))  # <class 'float'>
print(type(my_float_2))  # <class 'float'>

# Basic Arithmetic with Floats

x = 5.4
y = 12.0

print("Addition:", x + y)        # 17.4
print("Subtraction:", y - x)     # 6.6
print("Multiplication:", x * y)  # 64.8 (may show small rounding error)
print("Division:", y / x)        # 2.222...


# ==========================
# MIXING INTS AND FLOATS
# ==========================

# When you mix int and float, Python returns a float

num = 56
decimal = 5.4

result = num + decimal
print(result)         # 61.4
print(type(result))   # <class 'float'>


# ==========================
# OTHER IMPORTANT OPERATORS
# ==========================

# Modulus (%) -> Returns remainder
print(56 % 12)  # 8

# Floor Division (//) -> Removes decimal part
print(56 // 12)  # 4

# Exponentiation (**) -> Power
print(2 ** 3)  # 8


# ==========================
# TYPE CONVERSION
# ==========================

# Convert int to float
num = 56
print(float(num))  # 56.0

# Convert float to int (removes decimal part)
decimal = 12.9
print(int(decimal))  # 12

# Convert string to numbers
print(int("45"))      # 45
print(float("7.8"))   # 7.8


# ==========================
# USEFUL BUILT-IN FUNCTIONS
# ==========================

# round() -> Rounds a number
print(round(4.798))     # 5
print(round(4.253, 1))  # 4.3

# abs() -> Absolute value (removes negative sign)
print(abs(-15))  # 15

# pow() -> Power function
print(pow(2, 3))     # 8
print(pow(2, 3, 5))  # (2**3) % 5 = 3


# ==========================
# AUGMENTED ASSIGNMENT
# ==========================

"""
Augmented assignment updates a variable using an operator.

Instead of:
x = x + 5

We write:
x += 5
"""

value = 10
value += 5
print(value)  # 15

value -= 3
print(value)  # 12

value *= 2
print(value)  # 24

value /= 4
print(value)  # 6.0

value //= 2
print(value)  # 3.0

value %= 2
print(value)  # 1.0

value **= 3
print(value)  # 1.0


# ==========================
# AUGMENTED ASSIGNMENT WITH STRINGS
# ==========================

greet = "Hello"
greet += " World"
print(greet)  # Hello World

greet *= 2
print(greet)  # Hello WorldHello World


# ==========================
# IMPORTANT NOTE
# ==========================

"""
Python does NOT support ++ or -- like some other languages.

Instead of:
x++

Use:
x += 1
"""