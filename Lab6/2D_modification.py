import numpy as np
arr_2d = np.array([[1,2,3],[4,5,6]])
print("Original array:", arr_2d)
print("Original array:", arr_2d.ndim)
print("Element at index 0:", arr_2d[0])
print("Slice from index at 0 form 1 to 3:", arr_2d[0,1:3])
arr_2d[1, 1] = 12
print("Modified array:", arr_2d)