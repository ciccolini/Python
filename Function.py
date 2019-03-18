#to create a function
#by using def keyword
def my_function():
    print("Hello from a function")

#to call a function
my_function()

#to add as many parameters as possible
def my_function(fsurname):
    print(fsurname + " " + "Name")

my_function("Anthony")
my_function("Romain")
my_function("MP")
#improvement
def my_function(fsurname, fname):
    print(fsurname + " " + fname)

my_function("Anthony","Da Mota")
my_function("Romain", "Alexandre")
my_function("MP", "Ciccolini")

#to set up a default parameter value
def my_country(country = "France"):
    print("I am from " + country)

my_country("UK")
my_country("Spain")
my_country()
my_country("Singapore")

#to let the function return a value
def my_result(x):
    return 5 * x

print(my_result(3))
print(my_result(4))
print(my_result(5))

#to create a recursion of a function
#It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result
#example 1
def tri_recursion(k):
    if k > 0 :
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result

print("\nRecursion example result")
tri_recursion(6)

#example 2; find all final values from each node
world = {
    "Africa": {
        "Waganda": 7000
    },
    "Europe": {
        "France": {
            "PACA": {
                "Nice": 1520
            }
        }
    },
    "America": {
        "United States": {
            "New York": 142
        }
    }
}

def display_population(node):
    for key in node.keys():
        next_value = node[key]
        if type(next_value) is dict:
            display_population(next_value)
        else:
            print(f"\n{next_value}")

display_population(world)

#example 3; sum from world
def sum_population(node):
    result = 0
    for key in node.keys():
        next_value = node[key]
        if type(next_value) is dict:
            result += sum_population(next_value)
        else:
            return next_value
    return result

print(sum_population(world))

#LAMBDA FUNCTION; small anonymous function with any number of arguments, but can only have one expression
x = lambda a : a + 10
print(f"\n{x(5)}")

x = lambda a, b : a * b
print(x(4, 5))

x = lambda a, b, c : a + b + c
print(x(1, 2, 3))

#to combine a function and a lambda function
def my_func(n):
    return lambda a : a * n

mydoubler = my_func(2)
mytripler = my_func(3)
print(mydoubler(6))
print(mytripler(6))

exit()
