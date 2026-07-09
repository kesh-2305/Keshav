first = int(input("Enter your triangle first side: "))
second = int(input("Enter your triangle second side: "))
third = int(input("Enter your triangle third side:  "))

if first == second and second == third:
    print("triangle is equilateral because there all sides are equal")

elif first == second or second == third or third == first :
    print("triangle is isosceles because there two sides are equal")

else:
    print("triangle is scalene ")