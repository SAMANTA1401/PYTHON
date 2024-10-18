matrix=[[2,3,4],
        [5,6,7],
        [8,9,0]]

matrix_trans=[[0,0,0],
                [0,0,0],
                [0,0,0]]

for rows in range(len(matrix)):
    for columns in range(len(matrix[0])):
        matrix_trans[columns][rows] = matrix[rows][columns]
print("the transpose matrix is :")
for items in matrix_trans:
    print(items)