# Inheritance in Python is a fundamental concept in object-oriented programming that allows a class (child class) to inherit attributes and methods from another class (parent class). This promotes code reuse and helps in building hierarchical relationships between classes.

# Key Points of Inheritance:
# Parent Class (Base Class): The class whose properties and methods are inherited.
# Child Class (Derived Class): The class that inherits from the parent class.
# super() Function: Used to call methods of the parent class in the child class.
# Types of Inheritance:
# Single Inheritance: One child class inherits from one parent class.
# Multiple Inheritance: A child class inherits from multiple parent classes.
# Multilevel Inheritance: A child class inherits from a parent class, which itself inherits from another class.
# Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
# Hybrid Inheritance: A combination of two or more types of inheritance.
# Example 1: Single Inheritanc
class Parent:
    def greet(self):
        print("Hello from the Parent class!")

class Child(Parent):
    def greet_child(self):
        print("Hello from the Child class!")

# Usage
child = Child()
child.greet()        # Inherited method
child.greet_child()  # Child's own method

Example 2: Multiple Inheritance
Copy the code
class Parent1:
    def greet1(self):
        print("Hello from Parent1!")

class Parent2:
    def greet2(self):
        print("Hello from Parent2!")

class Child(Parent1, Parent2):
    def greet_child(self):
        print("Hello from the Child class!")

# Usage
child = Child()
child.greet1()
child.greet2()
child.greet_child()

Example 3: Using super()
Copy the code
class Parent:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Parent name: {self.name}")

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Call Parent's constructor
        self.age = age

    def show_details(self):
        print(f"Child name: {self.name}, Age: {self.age}")

# Usage
child = Child("Alice", 10)
child.show_name()
child.show_details()

# Benefits of Inheritance:
# Code Reusability: Avoids redundancy by reusing existing code.
# Extensibility: Allows adding new features to existing classes.
# Maintainability: Easier to manage and update code.

# Let me know if you'd like further clarification or examples! 😊
