
import numpy as np
# Creating a ID NumPy array 
array_1d = np.array([1, 2, 3, 4, 5, 6])
print("ID Array:")
print(array_1d)
# Reshaping the ID array to a 2x3 2D array 
array_2d = array_1d.reshape(2, 3)
print("\nReshaped to 2D Array (2x3):")
print(array_2d)
#Accessing elements using indexing
print("\nElement at position (1, 2):", array_2d[1, 2])
#Modifying an element
array_2d[0, 1] = 10
print("\nModified Array (After changing element at position (0,1) to 10):") 
print(array_2d)
# Calculating the sum of the array elements
array_sum = np.sum(array_2d)
print("\nSum of all elements in the array:", array_sum)


