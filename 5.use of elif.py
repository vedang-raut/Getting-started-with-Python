#use of elif 

num=int(input("Eneter the value="))
print("lets Test the value",num)
if num%3==0 and num%5==0:
    print("The condition is satisfied")
elif num%3==0:
    print("The condition is only satisfied by 3")
elif num%5==0:
    print("The condition is only satisfied by 5")
else:
    print("The given input cannot be satisfied")
