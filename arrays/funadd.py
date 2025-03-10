# Write a function to add integer values of an array.

from audioop import avg
from operator import index
from turtle import position
from typing import final

#Initialize array 
arr = list(map(int,input("Enter values:").split()))
sum = 0
#Loop through the array to calculate sum of elements 
for i in range(0,len(arr)):
    sum = sum + arr[i]
print("Sum of all integer values in array: ",sum) 