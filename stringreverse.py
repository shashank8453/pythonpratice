#string reversing using different methods


# using slicing with function
def reversestr(name):
    return name[::-1]

print(reversestr("shashank"))


#using slicing without function
str1reverse="soma"
print(str1reverse[::-1])

# using the for loop
forstr="rama"
for char in forstr[::-1]:
    print(char, end="")