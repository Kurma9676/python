# The __str__() method is a special method used to define a human-readable string representation of an object.

# It gets called when you use:

# print(object)

# str(object)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
      #f is formatting the string
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)
