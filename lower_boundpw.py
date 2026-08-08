def search(arr, x, is_left):
    l, r = 0, len(arr)
    while l < r:
        m = (l + r) // 2
        if (arr[m] < x) or (is_left is False and arr[m] == x):
            l = m + 1
        else:
            r = m
    return l


def find_range(arr, target):
    left = search(arr, target, True)
    if left == len(arr) or arr[left] != target:
        return [-1, -1]
    right = search(arr, target, False) - 1
    return [left, right]


if __name__ == "__main__":
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        n = int(input().strip())
        arr = list(map(int, input().split()))
        target = int(input().strip())
    else:
        n = int(data[0])
        arr = list(map(int, data[1:1+n]))
        target = int(data[1+n])
    print(*find_range(arr, target))
