##a=int(input("THE pattern we need to print"))
##print(a)
for i in range(1,10):
    for j in range(1,10):
        if j<=i:
            print("(",end='')
        else:
            print(" ")
    print()
