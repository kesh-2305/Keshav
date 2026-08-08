number = [1,2,3,4,5,6,7,8,9,10,11,12]

even = []
odd = []
prime = []
composite = []

for num in number:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)