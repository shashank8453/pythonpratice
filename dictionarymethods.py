dict1={"item":1,"item2":2,"item3":3}
dict2=dict1.copy()
print(dict1,dict2,sep='/n')
print(f"{dict1}/n{dict2}")

print(dict1.items())

print(dict1.keys())  # to print items of dictionary
print(dict1.values()) # to print values of dictionary

dict3={1:"value"}
print(dict3.values())
dict1={"item":1,"item2":2,"item3":3}
dict1.pop("item")
print(dict1)
print(len(dict1))