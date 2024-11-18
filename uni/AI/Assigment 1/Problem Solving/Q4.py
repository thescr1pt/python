m = int(input("Enter the number of elements: "))

arr = []
for i in range(m):
    arr.append(int(input("Enter the element in index " + str(i) + ": ")))


h = input("Enter your choice 'r' to shift right or 'l' to shift left ")

if h == "l":
    rem = arr[0]
    arr.remove(arr[0])
    arr.append(rem)
    print(arr)
else:
    rem = arr[-1]
    arr.pop()
    nw = [rem]
    nw += arr
    print(nw)
