#write a program to find the sum of digits of a given number'



a=int(input("Enter any number"))
sum=0
while(a!=0):
    d=a%10
    sum=sum+d
    a=a//10
print(sum)
