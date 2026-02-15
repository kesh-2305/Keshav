l1 = "make a lot of money"
l2 = "buy now"
l3 = "scane qr"
l4 = "you won"

message = input("Enter your comment: ")

if((l1 in message) or (l2 in message) or (l3 in message) or (l4 in message)):
    print("this comment is a spam")

else:
    print("you are safe from spams")

print("thanks you")