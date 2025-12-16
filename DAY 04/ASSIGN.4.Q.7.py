# Function to add and subtract two matrices
def matrix_operations(mat1, mat2):
    rows = len(mat1)
    cols = len(mat1[0])

    add_result = []
    sub_result = []

    for i in range(rows):
        add_row = []
        sub_row = []
        for j in range(cols):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
        add_result.append(add_row)
        sub_result.append(sub_row)

    return add_result, sub_result


# Main program

# 3x4 matrix as list of lists
matrix1 = [
    [2, 8, 3, 4],
    [5, 5, 7, 8],
    [9, 11, 13, 12]
]

# 3x4 matrix as tuple of tuples
matrix2 = (
    (13, 15, 11, 9),
    (6, 8, 6, 5),
    (5, 3, 2, 1)
)

# Function call
addition, subtraction = matrix_operations(matrix1, matrix2)

# Print results
print("Matrix Addition:")
for row in addition:
    print(row)

print("\nMatrix Subtraction:")
for row in subtraction:
    print(row)
