#The program for palindrome.


str=input("Enter the string value:")
rev=str[::-1]
print("The reverse order of string is:",rev)
if str==rev:
    print("The string is Palindrome")
else:
    print("The string is not Palindrome")


