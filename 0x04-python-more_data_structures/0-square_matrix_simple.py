#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    # Get the number of rows and columns in the matrix
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    # Create a new matrix to store the squared values
    result_matrix = [[0 for _ in range(num_cols)] for _ in range(num_rows)]

    # Iterate through the original matrix and compute the square values
    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[i][j] = matrix[i][j] ** 2

    return result_matrix
