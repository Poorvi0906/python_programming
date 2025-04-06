import numpy as np
M1 = np.random.randint(1, 11, (3, 3))
M2 = np.random.randint(1, 11, (3, 3))
subtraction_result = M1 - M2
division_result = np.divide(M1, M2, where=M2!=0)
print("Matrix 1:\n", M1)
print("Matrix 2:\n", M2)
print("Subtraction Result:\n", subtraction_result)
print("Element-wise Division Result:\n", division_result)