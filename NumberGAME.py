import random

print("Hello my friend, welcome to a new game")

num = random.randint(1, 1000)
chances = 15

while chances > 0:
    guess = int(input("Guess a number between 1 and 1000: "))

    if guess < 1 or guess > 1000:
        print("Invalid! Please enter a number between 1 and 1000")
        continue

    if num == guess:
        print("Congratulations! Your guess is right 🎉")
        break

    elif num > guess:
        print("Your guess is too Low")

    else:
        print("Your guess is too High")

    chances -= 1
    print("Chances left:", chances)

if chances == 0:
    print("Game Over 😢 The number was:", num)
