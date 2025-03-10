class Python:
# Access through class    
 staticVariable = 9 
#Access through an instance
instance = Python()
print(instance.staticVariable) # Gives 12
#Change within an instance
instance.staticVariable = 15
print(instance.staticVariable) # Gives 15
print(Python.staticVariable) #Gives 12