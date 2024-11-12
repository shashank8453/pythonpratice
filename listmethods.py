list1=[1,23,4,5,6,7,8,1,1]

for i in list1[::-1]:
    print(i,end="")
print(list1[::-1])
list3=[3,4,5]
list1.append(2)
print(list1)
list2=list1.copy()
print(list2)
print(list1.count(1))
# list1.extend(list3)
list1=list1+list3
print(list1)

list1.insert(-1,9)

list1.pop(-1)
list1.remove(23)
list1.reverse()
print(list1)

# ["(())","(())"]
# ["((()))","((()))","((()))"]
n=int(input("enter the number"))
l1=[n*"("+")"*n  for i in range (1,n+1)]
print(l1)