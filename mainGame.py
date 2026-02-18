import random
print("Your welcome in my game Stone Paper Scissoer")
op = ("stone", "paper", "scissoer")

user = input("Enter stone, paper, scissoer: ").lower()

computer = random.choice(op)
print("computer chose:", computer)

if(user == computer):
    print("Its a tie:", "sorry")

elif(user == "stone" and computer == "scissoer")or\
    (user == "paper" and computer == "stone")or\
    (user == "scissoer" and computer == "paper"):
    print("You Won this round")

elif user in op:
    print("You lose")

else:
    print("You enter invalid input! please enter in op: ")

print("retry next round")
