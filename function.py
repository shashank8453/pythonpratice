def my_function():
    print("hi")

my_function()


# Passing single Arguments or parameters
def pass_arguments(name):
    print("hi" +   name)

pass_arguments("  shashank")


# Passing multiple  Arguments or parameters
def pass_arguments(name,friend,sister):
    print("hi" +name+"hi"+friend+"hi"+sister)

pass_arguments("  shashank  ","  rama  ","  namratha")


# function with return type

def squrae(x):
    s=x**2
    return s
print(squrae(4))


# Python code to demonstrate
# call by reference


mylist = [10, 20, 30, 40]
def add_more(list):
    list.append(50)
    print("Inside Function", list)


# Driver's code
# mylist = [10, 20, 30, 40]

add_more(mylist)
print("Outside Function:", mylist)