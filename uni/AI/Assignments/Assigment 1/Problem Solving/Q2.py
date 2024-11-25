num_rows = int(input("Enter number of rows: "))
num_columns = int(input("Enter number of columns: "))

odd_value_indices = []
matrix_values = []
for row_index in range(num_rows):
    row = []
    for col_index in range(num_columns):
        element_value = int(
            input(
                "Enter the value for element ("
                + str(row_index)
                + ","
                + str(col_index)
                + "): "
            )
        )
        if element_value % 2 == 1:
            element_value = int(input("Enter a new value to replace the odd value: "))
            odd_value_indices.append([row_index, col_index])

        row.append(element_value)

    matrix_values.append(row)

print("The matrix")

for row_index in range(num_rows):
    print(matrix_values[row_index])

print("The following indexes originally had odd values: ", odd_value_indices)
