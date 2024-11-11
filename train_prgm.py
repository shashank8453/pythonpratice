
# integers=[i for i in range(1,101)]
# odd=[pow(i,2) for i in integers if i%2!=0]
# even=[i**2 for i in integers if i%2==0]
# print(odd)
# print(even)
dict_ops={"name":"rama","age":12,"gender":"male"}
dict_ops["new_name"]="shaku"
dict_ops["numbers"]=[i for i in range(10)]
for k,v in dict_ops.items():
    print(k,v)

