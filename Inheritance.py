#Parent class is the class being inherited from, also called base class.
#Child class is the class that inherits from another class, also called derived class.

#to create a Parent Class
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("Joe", "Kool")
x.printname()

#to create a child class that inherits the functionality from parent class
#using pass keyword when you do not want to add any other properties or methods
class Student(Person):
    pass
#using _init_() function
class Student2(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)

x.printname()

#to create an object in child class
x = Student("Lilo", "Stitch")
x.printname()

#to add properties
class Student(Person):
    def __init__(self, fname, lname, gradY):
        Person.__init__(self, fname, lname)
        self.graduationyear = gradY

x = Student("Lilo", "Glub", 2019)

#to add methods
#option 1
class Student(Person):
    def __init__(self, fname, lname, gradY):
        Person.__init__(self, fname, lname)
        self.graduationyear = gradY

    def welcome(self):
        self.printname()
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

x = Student("Flip", "Goul", 1523)
x.welcome()
#option 2
class Student(Person):
    def __init__(self, fname, lname, gradY):
        Person.__init__(self, fname, lname)
        self.graduationyear = gradY

    def welcome(self):
        self.printname()
        print("to the class of", self.graduationyear)

x = Student("Lilo", "Glub", 2019)
x.welcome()
exit()
