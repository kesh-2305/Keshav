"# ternary operator"

A = int(input("Enter your first number: "))
B = int(input("Enter your second number: "))
C = int(input("Enter your thired number: "))

largest = A if (A > B and A > C) else B if (B > C) else C

print("Largest number is:", largest)
