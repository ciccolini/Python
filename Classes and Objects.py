#Python is an object oriented programming language.
#Almost everything in Python is an object, with its properties and methods.
#A Class is like an object constructor, or a "blueprint" for creating objects.

#to create a class
class MyClass:
    x = 5

#to create an object
class MyClass:
    x = 5

Obj = MyClass()
print(Obj.x)

#to create a class using _init_() function
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

name = input("Enter your name\n")
age = input("Enter your age\n")

print(f"Your name is {name} and you are age is {age}")

p1 = Person(name, age)
print(p1.name, p1.age)

#to insert a function
#option 1
class Country:
    def __init__(country, name, unhabitant):
        country.name = name
        country.unhabitant = unhabitant

    def myfunction(country):
        print("You are coming from " + c1.name)

c1 = Country("France", 6000000) #cannot print nummbers, only string
c1.myfunction()
#NOTE:  The country parameter is a reference to the current instance of the class,
#and is used to access variables that belongs to the class.

#option 2
class Country2:
    def __init__(country, name, unhabitant):
        country.name = name
        country.unhabitant = unhabitant

    def myfunction2(country):
        print("You are coming from " + c2.name + " and you are " + c2.unhabitant)

name = input("Where do you come from? \n")
unhabitant = input("How many are you in your country? \n")

c2 = Country2(name, unhabitant)
c2.myfunction2()

#option 3; to demonstrate that we can use different parameter name
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()

#to modify object properties
p1.age = 40
print(p1.name, p1.age)

#to delete object properties
del p1.age

#to delete an object
del p1
exit()
