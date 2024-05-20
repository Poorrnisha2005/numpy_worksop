#write a program to find if the given number is prime no or not

a=int(input("Enter any number"))
c=0
for i in range(1,a+1,1):
    if(a%i==0):
        c=c+1
if(c==2):
    print("Prime Number")
else:
    print("Not a Prime Number")