#equals
#option 1
x = 0
y = 0.0
if x == y:
    print(f"Yes, {x} is equal to {y}")
#option 2
if x == y: print(f"Yes, {x} is equal to {y}")
#option 3
print(f" {x} and {y} are not equals") if x != y else print(f"{x} and {y} are equals")

#not equals
x = 0
y = 2
if x != y:
    print(f"Yes, {x} is not equal to {y}")

#less than
x = 0
y = 2
if x < y:
    print(f"Yes, {x} is less than {y}")

#greater than
x = 10
y = 2
if x > y:
    print(f"Yes, {x} is greater than {y}")

#elif keyword
x = 10
y = 2
if x == y:
    print(f"Yes, {x} is equal to {y}")
elif x != y:
    if x < y:
        print(f"Yes, {x} is less than {y}")
    elif x > y:
        print(f"Yes, {x} is greater than {y}")

#elif keyword combine with else keyword
x = 28
y = 25
if x == y:
    print(f"Yes, {x} is equal to {y}")
elif x != y:
    if x < y:
        print(f"Yes, {x} is less than {y}")
    else:
        print(f"Yes, {x} is greater than {y}")

#and keyword combine with or keyword
x = 1
y = 2
z = 3
if x < z or z < y and y < z:
    print(f"{z} is greater than {x} and {y}")

#with input // still doesn't work to check if it's not a number // doesn't work at all if not integral number
while True:
    try:
        x = input("Enter a number between 1 and 5 \n")
        y = input("Enter a second number between 1 and 5 \n")
        if 1 <= int(x) <= 5 and 1 <= int(y) <= 5:
            print("Both numbers are fine")
            if f"{x}" == f"{y}":
                print("These numbers are equals")
            elif f"{x}" < f"{y}":
                    print("The first number is less than the second")
            else:
                if f"{x}" > f"{y}":
                    print("The first number is greater than the second")
            break
        else:
            print("Sorry but one or both numbers are out of range")
    except NameError:
        print("It's not a number - please try again.")
