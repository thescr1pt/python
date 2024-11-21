print("Enter size of array: ")
n = int(input())

arr = []
# Read array
print("Enter array elements: ")
for i in range(n):
    arr.append(input())

# only print elements who appear once (non duplicates)
print("\nNon duplicates: ")
for i in arr:
    if arr.count(i) == 1:  # Check if their count = 1 before printing them
        print(i)
