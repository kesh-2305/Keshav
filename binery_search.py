def binary_search(arr, low, high, x):
    if low > high:
        return False

    mid = (low + high) // 2

    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        return binary_search(arr, low, mid - 1, x)
    else:
        return binary_search(arr, mid + 1, high, x)


import sys

data = list(map(int, sys.stdin.read().split()))

if not data:
    sys.exit()

n = data[0]
arr = data[1:1 + n]
x = data[1 + n]

if binary_search(arr, 0, n - 1, x):
    print("Found")
else:
    print("Not Found")
