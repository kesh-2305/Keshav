# tc.py
# Small program demonstrating time complexity examples in Python

# O(1) constant time example

def constant_time_example(arr):
    if not arr:
        return None
    return arr[0]


# O(n) linear time example

def linear_time_example(arr):
    total = 0
    for value in arr:
        total += value
    return total


# O(n^2) quadratic time example

def quadratic_time_example(arr):
    pairs = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            pairs.append((arr[i], arr[j]))
    return pairs


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]

    print("O(1) constant time example:", constant_time_example(numbers))
    print("O(n) linear time example:", linear_time_example(numbers))
    print("O(n^2) quadratic time example: number of pairs =", len(quadratic_time_example(numbers)))
