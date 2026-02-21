import random

def game():
    print("you are playing the game")
    score = random.randint(1, 60)
    with open("highscore.txt") as f:
        highscore = f.read()
        if(highscore!=""):
            highscore = int(highscore)
        else:
            highscore = 0

    
    print(f"your score: {score}")
    if(score>highscore):
        #write the highscore to the file
        with open("highscore.txt", "w") as f:
            f.write(str(score))
    return score
game()