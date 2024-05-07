def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transposed = [[0 for row in range(rows)] for col in range(cols)]

    for row in range(rows):
        for col in range(cols):
            transposed[col][row] = matrix[row][col]
    return transposed


matrix = [[1, 2, 3],
         [4, 5, 6], 
         [7, 8, 9]]
transposed_matrix = transpose(matrix)

print(transposed_matrix)
