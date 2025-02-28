import numpy as np
arr = np.arange(10)
print("Original array:", arr)
print("Element at index 5:", arr[5])
print("Slice from index 5 to 8:", arr[5:8])
arr[5:8] = 12
print("Modified array:", arr)