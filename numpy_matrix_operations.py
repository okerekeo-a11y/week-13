"""
Ogechukwu Okereke
CMSC 111
Week 13 Assignment1
"""
import numpy as np
array = np.arange(1, 101)
print("Array from 1 to 100:")
print(array)
matrix = array.reshape(10, 10)
print("\n10x10 Matrix:")
print(matrix)
rows_5_to_8 = matrix[4:8]
print("\nRows 5 to 8:")
print(rows_5_to_8)
total_sum = np.sum(matrix)
print("\nSum of all elements:")
print(total_sum)
