import random
import shelve

# fetch current highscore
def get_highscore():
    try:
        with open('highscores.txt', 'r') as file:
            highscores = file.readlines()
            if highscores:
                # extract the name and score
                name, score = highscores[0].strip().split(',')
                return name, int(score)
            else:
                return None, 0
    except FileNotFoundError:
        return None, 0

# function to update the highscore in the file
def update_highscore(playername, attempts):
    with open('highscores.txt', 'w') as file:
        file.write(f"{playername},{attempts}\n")

# function to read player number input and handle errors with the input
def input_playernumber():
    while True:
        try:
            input_str = input("Please input a number between 1-100: ")
            playernumber = int(input_str)
            if playernumber > 0 and playernumber < 101:
                return playernumber
            else:
                print("Invalid number! Try again!")
        except ValueError:
            print("Invalid number! Try again!")
            inputNumber = -1
        
# generate a random int in between 1 and 100
randomNumber = random.randint(1, 100)
# debug output of random number
print(randomNumber)

attempts = 0
playername = input("What's your name? ")
inputNumber = -1

while inputNumber != randomNumber:
    inputNumber = input_playernumber()
    if inputNumber < randomNumber:
        print("Too low Cutie 😘")
    if inputNumber > randomNumber:
        print("Too high Cutie 😘")
    attempts = attempts + 1
print("You guessed the Number Cutie 🥳")

# get the current highscore from the file
highscore_name, highscore_score = get_highscore()

# compare current score with highscore
if highscore_score == 0 or attempts < highscore_score:
    print(f"Good job, {playername}! {attempts} ATTEMPTS MAKE A NEW HIGHSCORE! 🎉")
    update_highscore(playername, attempts)
else:
    print(f"BUT: {highscore_name} with {highscore_score} attempts was better at guessing than you.")