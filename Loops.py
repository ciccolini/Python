#WHILE LOOP
i = 1
while i < 6:
    print(i)
    i += 1

#break statement
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#continue statement; will go to the top directly
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

#FOR LOOP
#for loop in a list
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)

#for looping through a string
for x in "banana":
    print(x)

#break statement
#example 1
for x in fruits:
    print(x)
    if x == "banana":
        break
#example 2
for x in fruits:
    if x == "banana":
        break
    print(x)

#continue statement
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range function
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.
for x in range(6):
    print(x)

#to change the starting value
for x in range(2, 6):
    print(x)

#to change the incrementation
for x in range(0, 19, 3):
    print(x)

#else in for loop
for x in range(6):
    print(x)
else:
    print("End")

#nested loop = a loop inside a loop
#The "inner loop" will be executed one time for each iteration of the "outer loop"
color = ["red","blue","yellow"]
for x in color:
    for y in fruits:
        print(x, y)
exit()
