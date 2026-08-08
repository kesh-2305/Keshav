def lower_bound(arr, x):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < x:
            low = mid + 1
        else:
            high = mid
    return low

# Example usage
shorted_list = [1, 2, 3, 3, 5, 5]
x = 4
position = lower_bound(shorted_list, x)
print(position)  # 3
