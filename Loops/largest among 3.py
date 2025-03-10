a=list(map(int,input("Enter 3 numbers:").split()))
big=a[0]
for i in range(0,3):
    if(a[i]>big):
        big=a[i]
print(big)