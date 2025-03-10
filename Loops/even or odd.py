a=list(map(int,input("Enter few numbers").split()))
print("The even numbers are:")
for i in a:
    if(i%2==0):
        print(i," ",end="")
print("\nThe odd numbers are:")
for i in a:
    if(i%2!=0):
        print(i," ",end="")