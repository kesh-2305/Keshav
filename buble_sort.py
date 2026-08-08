def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
           if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]

bubble_sort(arr)
print(arr)"""


def sorted_array(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr[j+1] = arr[j+1] , arr[j]
arr = [1 , 2 , 3 ,4]
sorted_array(arr)
print("sorted array", arr)
