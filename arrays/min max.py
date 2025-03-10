# Write a function to find the minimum and maximum value of an array.

#Initialize array
arr = [100,3,3000,20,500,9999,10000,10003]

#minimum value of array
minposition = arr.index(min(arr))
print ("The minimum is at position:", minposition)

#maximum value of array
maxposition = arr.index(max(arr))
print ("The maximum is at position::", maxposition)