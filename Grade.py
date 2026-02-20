M = int(input("Enter your marks: "))

if(M > 90):
    print("Grade A+")

elif(M < 90 and M > 80):
    print("Grade A")
elif(M < 80 and M > 70):
    print("Grade B")
elif(M < 70 and M > 60):
    print("Grade C")
elif(M < 60 and M > 50):
    print("Grade D")

else:
    print("Grade E")