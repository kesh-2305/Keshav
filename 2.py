k1 = int(input("enter English marks: "))
k2 = int(input("enter Hindi marks: "))
k3 = int(input("enter Mathmatics marks: "))

total_percentage = (100*(k1 + k2 + k3))/300

if(total_percentage>=40 and k1>=33 and k2>=33 and k3>=33):
    print("you are pass:",total_percentage)

else:
    print("sorry brother try next year:",total_percentage)

print("thanks you mr.miss")