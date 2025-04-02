import random

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
        
# generate a random int in between 1 and 100
randomNumber = random.randint(1, 100)
# debug output of random number
print(randomNumber)

attempts = 0
inputNumber = -1
playername = input("What's your name? ")

while inputNumber != randomNumber:
    inputNumber = int(input("Please input a Number between 1-100: "))
    if inputNumber < randomNumber:
        print("Too low Cutie 😘")
    if inputNumber > randomNumber:
        print("Too high Cutie 😘")
    attempts = attempts + 1
print("You guessed the Number Cutie 🥳")

if attempts > 1:
    print("You needed "+ str(attempts) +" attempts.")
elif attempts == 1:
    print("You needed 1 attempt.")

# get the current highscore from the file
highscore_name, highscore_score = get_highscore()

# compare current score with highscore
if highscore_score == 0 or attempts < highscore_score:
    print(f"Good job, {playername}! NEW HIGHSCORE! 🎉")
    update_highscore(playername, attempts)
else:
    print(f"CORRECT, but: {highscore_name} with {highscore_score} attempts was better at guessing than you.")