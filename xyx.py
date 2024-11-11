L=[i for i in range (0,15) if i%2!=0]
print("\n".join(map(str,L)))

for items in L:
    print(items)

print(*L,sep="\n")


dict1={i:f"items{i}" for i in range (1,50) if i%2==0}
print(dict1)