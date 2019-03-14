#to create a list
thislist = ["a","b","c"]
print(thislist)

#will print the second item of the list
print(thislist[1])

#to change the second item
thislist[1] = "d"
print(thislist)

#to loop through the list items by using for loop; each item will be shown line by line
thislist = ["apple","banana","cherry"]
for x in thislist:
    print(thislist)

#to check if a specified item is present in a list
thislist = ["a","b","c"]
if "a" in thislist:
    print("Yes")

#improvement to check specified item
thislist = ["a","b","c"]
x = input("Type a letter below \n")
if x in thislist:
    print("Yes, you got lucky!")
else:
    print("Nope")

#to determine how many items a list contains
print(len(thislist))

#to add 1 item to the end of the list with .attend
thislist.append("d")
print(thislist)

#to add another list at the end of the current list - any iterable (list, set, tuple, etc.)
firstlist = ["a","b","c"]
secondlist = ["d","e","f"]
firstlist.extend(secondlist)
print(firstlist)

#to add an item at a specific position
thislist.insert(0,"z")
print(thislist)

#to remove an item; .remove is used when you have the name of the item
# .pop remove a specified index or the last one if empty like 'del' keyword
thislist.remove("z")
thislist.pop()
del thislist[0]
print(thislist)

#'del' is also used to delete a list the list like clear()
x = ["bla","bli","bloup"]
del x #cannot be print !!!
y = ["bla","bloubloup"]
y.clear()
print(y)

#to create a list with list() constructor
thislist = list(("bla","bli","bloup"))
print(thislist)

#to create a copy of thislist
x = thislist.copy()
print(x)

#to return the number of time the value "x" appears in the list
thislist = list(("a","b","c","x"))
count = thislist.count("x")
print(count)

#to return the first occurence of the value "x"
thislist = list(("a","b","c","x"))
index = thislist.index("x")
print(index)

#reverse the order of the thislist
thislist = list(("bla","bli","bloup"))
thislist.reverse()
print(thislist)

#to sort the list
thislist.sort()
print(thislist)
