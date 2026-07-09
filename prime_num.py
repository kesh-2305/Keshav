n = int(input())
for i in range(2, n/2):
    if (n % i == 0):
        break
        print("your num is not a prime num")  
    else:
        print("your num is a prime num")