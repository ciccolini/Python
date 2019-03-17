# a dictionary is a collection which is unordered, changeable and indexed

#to create a dictionary
#option 1
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
#option 2 by using dict constructor
seconddict = dict(brand ="Fiat", model="500", year=2018)
print(seconddict)
#option 3 by using dict constr + .fromkeys method
x = ("brand", "model", "year")
y = 0 #an unique value for all key names
thirddict = dict.fromkeys(x, y)
print(thirddict)

#to access the items of the dictionary
#option 1
x = thisdict["model"]
print(x)
#option 2
x = thisdict.get("year")
print(x)

#to change the value of an item
thisdict["year"] = 2018
print(thisdict)

#to loop through a dictionary
#option 1 by using for to show the key names of the dictionary
for x in thisdict:
    print(x)
#option 2 by using for to show the values in the dictionary
for x in thisdict:
    print(thisdict[x])
#option 3 by using .values to return values of the dictionary
for x in thisdict.values():
    print(x)
#option 4 by using .items fonction to show key names and values
for x, y  in thisdict.items():
    print(x, y)

#to show the key names of the dictionary
x = thisdict.keys()
print(x)
#to show the values of the dictionary
x = thisdict.values()
print(x)

#to check if a specified key is present in the dictionary by using in
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes")
#improvement
x = input("What do you want to check? \n")
if f"{x}" in thisdict:
    print("Yes")
else:
    print("No")

#to determine how many items (key-value pairs) a dictionary has
print(len(thisdict))

#to add an new item
#option 1
thisdict["color"] = "red"
print(thisdict)
#option 2 by using .update method
thisdict.update({"motor": "diesel"})
print(thisdict)
#option 3 by using .setdefault; if the key name exist, this parameter has no effect
x = thisdict.setdefault("door", 5)
y = thisdict.setdefault("color", "white")
print(x, y)
print(thisdict)

#to remove an item
#option 1 by using .pop
thisdict.pop("color")
print(thisdict)
#option 2 by using .popitem; remove the last inserted key-value pair
thisdict.popitem()
print(thisdict)
#option 3 by using del keyword
del thisdict["brand"]
print(thisdict)

#to empty the dictionary
thisdict.clear()
print(thisdict)

#to delete a dictionary
del thirddict

#to create a copy of the dictionary
thisdict = dict(brand ="Ford", model="Mustang", year=1964)
x = thisdict.copy()
print(x)
exit()
