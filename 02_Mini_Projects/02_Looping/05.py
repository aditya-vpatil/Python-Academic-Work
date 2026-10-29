'''Number Guessing Game'''

secret_number = 37
attempts = 0
guessed = False
while attempts < 5:

    guess = int(input("Guess the number: "))
    attempts = attempts + 1
    
    if guess == secret_number:
        print("Correct! You win.")
        guessed = True
        break 
    elif guess < secret_number:
        print("Too low")
    else:
        print("Too high")


print("Attempts used:", attempts)


if guessed == False:
    print("You lose. The secret number was", secret_number)
    print("You can try again")