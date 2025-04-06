
import numpy as np
# Creating two matrices
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])
#Matrix Addition
matrix_sum = np.add(matrix_A, matrix_B)
print("Matrix Addition (A + B):")
print(matrix_sum)
# Matrix Multiplication (Element-wise)
matrix_product_elementwise = np.multiply(matrix_A, matrix_B) 
print("\nElement-wise Matrix Multiplication (A* B):")
print(matrix_product_elementwise)
# Matrix Dot Product (Matrix Multiplication)
matrix_dot_product = np.dot(matrix_A, matrix_B)
print("\nMatrix Dot Product (A. B):")
print(matrix_dot_product)
# Transposing a matrix
matrix_transpose = np.transpose(matrix_A)
print("\nTranspose of Matrix A:")
print(matrix_transpose)