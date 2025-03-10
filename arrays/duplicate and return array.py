# Write a method to remove duplicate elements from an array.

#Initialize array
arr =list(map(int,input("Enter values:").split()))
finalarr = [] #empty array
#Using loop to remove duplicated elements
for i in arr:
    if i not in finalarr:
        finalarr.append(i)
print(finalarr)