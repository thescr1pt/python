import pandas as pd


def slicing(df, startRow, endRow, startCol, endCol):
    return df.iloc[startRow:endRow, startCol:endCol]


arr = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]

n = 7

arr = pd.DataFrame(arr)

startRow = int(input("Enter start row: "))
endRow = int(input("Enter end row: "))
startCol = int(input("Enter start column: "))
endCol = int(input("Enter end column: "))

print(slicing(arr, startRow, endRow, startCol, endCol))
