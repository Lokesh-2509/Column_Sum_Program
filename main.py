def column_wise_sums(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    sums = [0] * cols
    for j in range(cols):
        for i in range(rows):
            sums[j] += matrix[i][j]
    return sums
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = []
print("Enter the elements row-wise:")
for i in range(rows):
    row_values = list(map(int, input().split()))
    matrix.append(row_values)
result = column_wise_sums(matrix)
print(result)

