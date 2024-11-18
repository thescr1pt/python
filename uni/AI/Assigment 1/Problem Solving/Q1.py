number_of_rows = int(input("Enter number of rows: "))
number_of_columns = int(input("Enter number of columns: "))

matrix_values = []
for row_idx in range(number_of_rows):
    row_values = []
    for col_idx in range(number_of_columns):
        print("Enter the value for element (", str(row_idx), ",", str(col_idx), "): ")
        row_values.append(int(input()))
    matrix_values.append(row_values)

print("The Matrix")

for row_idx in range(number_of_rows):
    print(matrix_values[row_idx])

print("The following indexes have odd values ")
for row_idx in range(number_of_rows):
    for col_idx in range(number_of_columns):
        if matrix_values[row_idx][col_idx] % 2 == 1:
            print([row_idx, col_idx])
