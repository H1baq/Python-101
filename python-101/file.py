"""
========================
PYTHON STRINGS – BASICS
========================

This file explains what strings are in Python,
how they work, and common operations you will use
as a beginner.
"""

# -------------------------
# 1. WHAT IS A STRING?
# -------------------------
# A string is a sequence of characters (text).
# Strings are written inside single quotes or double quotes.

my_str_1 = 'Hello'
my_str_2 = "World"

print(my_str_1)
print(my_str_2)


# -------------------------
# 2. MULTI-LINE STRINGS
# -------------------------
# Use triple quotes for strings that span multiple lines.

multi_line_str = """This is a
multi-line
string"""

print(multi_line_str)


# -------------------------
# 3. QUOTES INSIDE STRINGS
# -------------------------
# If your string contains quotes, you can:
# - Use the opposite quote type
# - Escape the quote using a backslash (\)

example_1 = "It's a sunny day"
example_2 = 'She said, "Hello!"'
example_3 = 'It\'s a sunny day'

print(example_1)
print(example_2)
print(example_3)


# -------------------------
# 4. CHECKING TEXT IN A STRING
# -------------------------
# Use the `in` keyword to check if text exists in a string.
# It returns True or False.

text = "Hello world"

print("Hello" in text)   # True
print("hi" in text)      # False
print("o" in text)       # True


# -------------------------
# 5. STRING LENGTH
# -------------------------
# len() returns the number of characters in a string.

print(len(text))  # 11


# -------------------------
# 6. STRING INDEXING
# -------------------------
# Indexing lets you access individual characters.
# Indexing starts at 0.

word = "Python"

print(word[0])   # P
print(word[3])   # h

# Negative indexing starts from the end
print(word[-1])  # n
print(word[-2])  # o


# -------------------------
# 7. STRING IMMUTABILITY
# -------------------------
# Strings are immutable, meaning they cannot be changed.
# You can reassign a variable, but you cannot change characters directly.

greeting = "hi"
greeting = "hello"  # allowed
print(greeting)

# This is NOT allowed and will cause an error:
# greeting[0] = "H"


# -------------------------
# 8. STRING CONCATENATION
# -------------------------
# Concatenation means joining strings using +.

first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
print(full_name)

# Numbers must be converted to strings before concatenation
age = 26
info = full_name + " is " + str(age) + " years old"
print(info)

# Using +=
message = "Hello"
message += " World"
print(message)


# -------------------------
# 9. STRING INTERPOLATION (F-STRINGS)
# -------------------------
# F-strings make inserting variables into strings easier.

name = "Amina"
age = 20

print(f"My name is {name} and I am {age} years old")
print(f"5 + 10 = {5 + 10}")


# -------------------------
# 10. STRING SLICING
# -------------------------
# Slicing extracts parts of a string.
# Format: string[start:stop:step]

text = "Hello world"

print(text[0:5])   # Hello
print(text[:5])    # Hello
print(text[6:])    # world
print(text[:])     # Hello world

# Step example
print(text[0:11:2])  # Hlowrd

# Reverse a string
print(text[::-1])    # dlrow olleH


# -------------------------
# 11. COMMON STRING METHODS
# -------------------------
# String methods return NEW strings.
# They do not change the original string.

sample = "  hello world  "

print(sample.upper())
print(sample.lower())
print(sample.strip())
print(sample.replace("hello", "hi"))
print(sample.split())

words = ["hello", "world"]
print(" ".join(words))

print(sample.startswith("  he"))
print(sample.endswith("  "))

print(sample.find("world"))
print(sample.count("o"))

print("hello world".capitalize())
print("hello world".title())
print("HELLO".isupper())
print("hello".islower())


# -------------------------
# KEY TAKEAWAYS
# -------------------------
# - Strings store text
# - Indexing starts at 0
# - Strings are immutable
# - Use f-strings for clean formatting
# - String methods return new strings