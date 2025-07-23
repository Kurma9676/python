# Conditional statements in Python allow you to execute specific blocks of code based on certain conditions. They are essential for decision-making in programming. Here's a quick overview:

# 1. if Statement

# Executes a block of code if the condition is True.
x = 10
if x > 5:
    print("x is greater than 5")

# 2. if-else Statement

# Provides an alternative block of code if the condition is False.

x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# 3. if-elif-else Statement

# Allows checking multiple conditions in sequence.

x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")

# 4. Nested if Statements

# You can nest if statements for more complex conditions.


x = 15
if x > 10:
    if x % 2 == 0:
        print("x is greater than 10 and even")
    else:
        print("x is greater than 10 and odd")

# 5. Ternary Conditional Operator

# A compact way to write simple if-else statements.


x = 8
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# 6. Using Logical Operators

# Combine multiple conditions using and, or, and not.

# #
x = 12
if x > 5 and x < 20:
    print("x is between 5 and 20")


Python's conditional statements are straightforward and highly readable, making them a powerful tool for controlling program flow.
