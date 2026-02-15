a1 = int(input("Enter your first number"))
a2 = int(input("Enter your second number"))
a3 = int(input("Enter your third number"))
a4 = int(input("Enter your fourth number"))

if(a1>a2 and a1>a3 and a1>a4):
    print("grater number is a1:",a1)

elif(a2>a1 and a2>a3 and a2>a4):
    print("grater number is a2:",a2)

elif(a3>a1 and a3>a2 and a3>a4):
    print("grater num is a3:",a3)

else:
    print("Grater number is a4:",a4)

print("end of the game")