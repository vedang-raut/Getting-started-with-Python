li=[22,32,'Python','California',56,78,90]
print("The current list is:",li)
tuple=tuple(li)
print("NOw it is tuple",tuple)
li=list(tuple)
print(li)
for i in range(2,5):
    li.append(i)
    print(li)




