#tuple is a collection which is orderer and unchangeable
#to create a tuple; 2 options
#1
thistuple = ("a","b","c")
print(thistuple)
#2
thistuple = tuple(("a","b","c","d"))
#to show a specified item
print(thistuple[3])

#to loop through the tuple items by using a for loop
for x in thistuple:
    print(x)

#to check if a specified item is present in a tuple using in
if "a" in thistuple:
    print("Yes")

#to determine the number of items in the tuple
print(len(thistuple))

#to return the number of time a specified value occurs
x = thistuple.count("a")
print(x)

#to search the tuple for a specified value and returns the position of where it is
x = thistuple.index("a")
print(x)
exit()
