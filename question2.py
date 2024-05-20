# find if the given number is a palindrome or not?
a=int(input("Enter any number"))
b = int(str(a)[::-1])
if(a==b):
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")