n = int(input("Enter any natural number: "))

evenSum = 0

oddSum = 0

for i in range(1, n+1):
    if (i%2==0):
        print(i, "is even")
        evenSum = i +evenSum
    else:
        print(i, "is odd")
        oddSum =  i + oddSum

print("The sum of even integars", evenSum)

print("The sum of odd integars", oddSum)