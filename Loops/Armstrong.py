n=int(input("Enter a 3 digit number:"))
m=n
sum=0
while(n>0):
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
if(sum==m):
    print("Armstrong number")
else:
    print("Not an armstrong number")