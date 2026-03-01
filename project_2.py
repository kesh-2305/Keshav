import random
n = random.randint(1, 100)
a = -1
guesses = 0
while(a != n):
    guesses +=1
    a = int(input("Enter your gusee: "))
    if(a > n):
        print("Lower number please")
    elif(a < n):
        print("Higher number please")
    
    elif(a <= 0 ):
        print("Enter a valid number please")
    
    elif(a == n):
        print(f"Congratulations you have gusse the correct number {guesses} attempt")
        print("You Won \n thanks you")