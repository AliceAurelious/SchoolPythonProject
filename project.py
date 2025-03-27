import random
# generate a random int in between 1 and 100
randomNumber = random.randint(1, 100)
# debug output of random number
print(randomNumber)

attempts = 0
inputNumber = -1
while inputNumber != randomNumber:
    inputNumber = int(input("Please input a Number between 1-100: "))
    if inputNumber < randomNumber:
        print("Too low Cutie 😘")
    if inputNumber > randomNumber:
        print("Too high Cutie 😘")
    attempts = attempts + 1
print("You guessed the Number Cutie 🥳")
if attempts > 1:
    attempts = str(attempts)
    print("You needed " + attempts +" attempts.")
elif attempts == 1:
    print("You needed 1 attempt.")
