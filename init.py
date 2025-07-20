#__init__ constructor. it is always executed when the class is initialize.use this to 
#initialize the object proprties
#self:refers to the instance being created,When you define a method inside a class, Python automatically passes the object (instance) as the first argument when the method is called.
#init doesnot return anything
class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
o=Student("Kurma","22481a05n0")
print("name of the student:",o.name)
print("roll no:",o.rollno)
