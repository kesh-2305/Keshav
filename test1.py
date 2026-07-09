n = int(input())

if (n < 0) :
    print("n is negative", n)
    print("absolute value is", (abs(n)))

elif(n == 0):
    print("n is zero", n)
    print("Zero is natural number")

elif(n > 0):
    print("n is positive", n)
    if (n % 2 == 0):
        print("n is even", n)
    elif(n % 2 != 0):
        print("n is odd", n)
    elif(n % 3 == 0):
        print("n is divisibal by 3", n)
    
