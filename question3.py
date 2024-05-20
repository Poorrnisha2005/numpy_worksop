#write a program to find the factorial of a nummber

a=int(input("Enter a number"))
fact=1
while(a>0):
    fact=fact*a
    a=a-1
print(fact)
