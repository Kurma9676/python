# #method:A method is a function that belongs to an object — specifically, an object created from a class.

# If you define a function inside a class, it's called a method.

# It usually acts on the object’s data (its attributes).
class Teacher:
    def action(self):
        print("teaching")
o=Teacher()
o.action()
o.action()
#calling method
