#an iterator is an object that contains a countable number of values.
#an iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

#iterator vs iterable
#using iter() method
#option 1; with a list
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
#option 2; with a string
mystrg = "banana"
myit = iter(mystrg)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

#looping through an iterator
mytuple = ("bla", "bli", "bloup")
for x in mytuple:
    print(x)

mystrg = "champagne"
for x in mystrg:
    print(x)

#to create an iterator
#the __iter__() method can do operations (initializing etc.) but must always return the iterator object itself.
#the __next__() method also allows you to do operations, and must return the next item in the sequence.
#option 1
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
            x = self.a
            self.a += 1
            return x

myClass = MyNumbers()
myiter = iter(myClass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

print("\n")

#StopIteration
class MyNumbers2:
    def __iter__(self):
        self.b = 1
        return self

    def __next__(self):
        if self.b <=10:
            x = self.b
            self.b += 1
            return x
        else:
            raise StopIteration

MyClass2 = MyNumbers2()
myiter = iter(MyClass2)

for x in myiter:
    print(x)
