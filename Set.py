#The major difference is that sets, unlike lists or tuples, cannot have multiple occurrences of the same element and store unordered values

#to create a set
#option 1
thisset = {"a","b","c"}
print(thisset)
#option 2
thisset = set(("a","b","c"))
print(thisset)

#to loop through all items by using for
for x in thisset:
    print(x)

#to check if an item is in the set or not; will return True or False
print("c" in thisset)
print("d" in thisset)

#not able to change an item in the set but can add more
#by using .add
thisset.add("d")
print(thisset)
#by using .update
thisset.update(["e","f","g"])
print(thisset)

#to get the length of the set
print(len(thisset))

#to remove an item
#by using .remove; if the item doesn't exist it will raise an error
thisset.remove("g")
print(thisset)
#by using .discard; will not raise any error
thisset.discard("f")
print(thisset)
#by using .pop - it will delete the last item but as the set is unordered, it will delete a random item
x = thisset.pop()
print(x)
print(thisset)

#to empty the set
thisset = {"a", "b", "c"}
thisset.clear()
print(thisset)

#to delete the set
thisset = {"a", "b", "c"}
del thisset

#to copy the set
thisset = {"a","b","c"}
copy_set = thisset.copy()
print(copy_set)

#to return the difference
#difference between at least 2 sets
thisset.add("d")
difference = thisset.difference(copy_set)
print(difference)
#symmetric difference between 2 sets
thisset.add("e")
symmetric = thisset.symmetric_difference(copy_set)
print(symmetric)

#to remove the items which are in both sets
thisset.difference_update(copy_set)
print(thisset)
#to remove the items in this set that are not present in other, specified sets
thisset = {"a", "b", "c","d","e","f"}
settest = {"a","e"}
thisset.intersection_update(copy_set, settest)
print(thisset)

#to remove the items that are present in both sets, AND insert the items that is not present in both sets
thisset = {"a", "b", "c","d"}
thisset.symmetric_difference_update(settest)
print(thisset)

#to return a set, that is the intersection of two other sets
thisset = {"a", "b", "c","d"}
intersection = thisset.intersection(copy_set)
print(intersection)

#to determine if 2 sets have an intersection; False if they have a common item
isdisjoint = thisset.isdisjoint(settest)
print(isdisjoint)
newset = {"d","e","f"}
isdisjoint = copy_set.isdisjoint(newset)
print(isdisjoint)

#to return whether another set contains this set or not; all items have to be present
#option 1
issubset = thisset.issubset(copy_set)
print(issubset)
issubset = copy_set.issubset(thisset)
print(issubset)
#option 2
issuperset = thisset.issuperset(copy_set)
print(issuperset)
issuperset = copy_set.issuperset(thisset)
print(issuperset)

#to combine at least 2 sets
thisset = {"a", "b", "c","d"}
newset = {"d","e","f"}
settest = {"a","e","g"}
result = thisset.union(newset, settest)
print(result)
exit()
