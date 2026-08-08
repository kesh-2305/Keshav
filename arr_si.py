def print_num(arr, si):
    if(si < 0):
        return
    print(arr[si], end=' ')
    print_num(arr, si - 1)

print_num([1, 2, 3, 4, 5], 4)

