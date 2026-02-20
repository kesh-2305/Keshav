A = int(input("Enter first num: "))
B = int(input("Enter second num: "))
C = int(input("Enter third num: "))

if( A > B and A > C):
    print("A is Grater")

elif(B > A and B > C):
    print("B is Grater")

elif(C > A and B < C):
    print("C is Grater")

elif( A == B and A == C):
    print("all are equal")

elif( A == B ):
    print("A is equal to B")

elif( A == C):
    print(" A is equal to C")

elif( B == C):
    print(" B is equal to C")