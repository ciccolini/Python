print ("Bonjour")
#will return the green string
print("\n")
#will insert a blank line

string = "Why not?"

print(string[7])
#will write the 7th character - note that the first character is 0 -> W
print(string[0:2])
#will write from the 1st to the 2nd character as the 3rd one is excluded
print(len(string))
#will return the lenght of the string
print(string.lower())
#method returns the string in lower case

print(string)
#we can see that string is showing as initially writen
string = string.upper()
print(string)
#method returns the string in upper case

string = "Why not?"
print(string.replace("?", " after all!"))
#replace a string with another string
print(string.split(" "))
#method splits the string into substrings if it finds instances of the separator

print("Please enter your name:")
x = input()
print("Bonjour" + " " + x)
#ask the user something to integrate it

name = "Jack"
age = 26
print(f"Bonjour, {name}. You are {age}.")
#f-string at the beginning of the print method will replace the curly braces expressions with their values

x = input("Please enter your second name:\n")
y = input("Please enter your age:\n")
message = (f"Hi {name}, {x}. You are now {y} instead of {age}")
print(message)
#improvement of the syntax by integrating the question on the input

a = input("Please enter your full name:\n")
while True:
    try:
        b = int(input("Please enter your age:\n"))
        if 0 <= b <= 120:
            message = (f"Hi {name}, {x}.\n"
                        f"You are now {b} instead of {age}")
            print(message)
            break
        else:
            print("Oopsy, the number is out of range")
    except NameError:
        print("Input was not a digit - please try again.")
    print(message)
#improvement2 of the syntax by integrating the question on the input & to check if the input age is a number between 0 and 120
