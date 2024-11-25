rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

ans = []
matrix = []
for i in range(rows):
    row = []
    for j in range(columns):
        n = int(input("Enter the value for element (" + str(i) + "," + str(j) + "): "))
        if n % 2 == 1:
            ans.append([i, j])
        while n % 2 == 1:
            n = int(input("Enter a new value to replace the odd value: "))

        row.append(n)

    matrix.append(row)

print("The Matrix")

for i in range(rows):
    print(matrix[i])

print("The following indexes originally had odd values: ", ans)
