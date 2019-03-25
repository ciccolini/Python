#array are used to store multiple values in one variable
#to create an array
cars = ["Ford", "Volvo", "BMW"]
print(cars)

#to refer an element by its index number
x = cars[0]
print(x)

#to find the first index of a value
x = cars.index("Volvo")
print(x)

#to change an item value
cars[0] = "Toyota"

#to find the lengh of an array
x = len(cars)
print(x)

#to go through array elements
for x in cars:
    print(x)

#to add an array element
#option 1 using append; will be added at the end
cars.append("Renault")
print(cars)
#option2 using insert
cars.insert(0, "Ferrari")
print(cars)
#option 3 using extend
cars1 = ["Peugeot", "Prout"]
cars.extend(cars1)
print(cars)

#to remove an array element
#option 1 using pop()
cars.pop(1)
print(cars)
#option 2 using remove(); only removes the first occurrence of the specified value
cars.remove("Volvo")
print(cars)

#to  create a copy of an array
copy_cars = cars.copy()
print(copy_cars)

#to count the number of elements with the specified value
cars.append("Prout")
cars.extend(copy_cars)
x = cars.count("Prout")
print(x)

#to sort the list
cars.sort()
print(cars)

#to reverse the order of the list
cars.reverse()
print(cars)

#to clear the array
cars.clear()
exit()
