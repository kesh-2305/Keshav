n = int(input("enter the value of n upto which we want the fibonacci serios"))

if(n <= 0):
    print("number enterd id not coorect  it should be > 0 ", n)

print(1, end = ",")

if (n == 1 ):
    pass
else:
    print( 1 , end = ",")

    if (n == 2):
        pass
    else :
        # print the remaning part of the serios
        prev = 1
        prev_prev = 1

        for num in (3, n+1):
            print(prev+ prev_prev, end = ",")
            prev,prev_prev = prev + prev_prev ,prev
