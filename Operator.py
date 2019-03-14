#to verify the type of any object
myint = 5 #entier
myfloat = 7.3 #decimal
mycomplex = 1j #complexe avec j pour la partie imaginaire
print(myint, type(myint))
print(myfloat, type(myfloat))
print(mycomplex, type(mycomplex))

#to change the type of the value
print(float(myint)) #will be 5.0
print(int(myfloat)) #will be 7

a, b = 5, 7
print(a + b)
print(a - b)
print(a * b)
print(a / b)

#test condition if
a,b = 2,5
if a > 0:
    b +=5
    print(b, a, "what")
else:
    print("bloubloup")

#combine both text and a variable, Python uses the + character
#ERROR if 4 without "" as Python doesn't combine string & number
mystring = "hello"
print(mystring + " 4 " + "the world")

#end the code
exit()
