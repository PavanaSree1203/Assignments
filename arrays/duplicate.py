# Write a function to find the duplicate values of an array.
 
#Initialize array    
arr = [21,11,31,13,11]
#Using loop to check duplicate values in array
for i in range(0,len(arr)):
    for k in range(i + 1,len(arr)):
        if arr[i] == arr[k]:
            print("Duplicate element in given array:",arr[k])