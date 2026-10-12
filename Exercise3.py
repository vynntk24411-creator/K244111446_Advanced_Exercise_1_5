#Coder: Nguyễn Ngọc Thảo Vy
#ID: K244111446
#Email: vynntk24411@st.uel.edu.vn
#Description: Exercise 3 - Number guessing game machine

# Necessary to use random numbers
import random

print("Let's play a number guessing game with me\n")
print("What's your name?\n")
# Enter player name
playerName = input()

# The first game has a limit of 5 guesses
limit = 5
# Setting the game repeat state
playAgain = 'YES'

print("Nice to meet you, " + playerName + ", I have a number between 1 and 30. Guess it\n")

while playAgain == 'YES':
    # Generate a new random number for every game
    ansNumber = random.randint(1, 30)
    count = 1
    guessNumber = -1
    print("You only have", limit, "guesses")

    while count <= limit and guessNumber != ansNumber:
        # Make sure the player enters an integer (invalid input does not use up a guess)
        try:
            guessNumber = int(input("Please enter the guessed number->"))
        except ValueError:
            print("Please enter an integer number!")
            continue

        if guessNumber == ansNumber:
            break  # If you get the correct answer, exit the inner while statement.
        elif guessNumber < ansNumber:
            print("The guessed number is less than the number with the computer.")
        else:
            print("The guessed number is greater than the number with the computer.")
        count = count + 1

    if guessNumber == ansNumber:
        print("You got it right in", count, "guess(es)!! Congratulations\n")
        # Win: the limit is decreased by 1 (but never below 1)
        if limit > 1:
            limit = limit - 1
    else:
        print("You ran out of guesses. The number of the computer is", ansNumber)
        # Lose: the limit is increased by 1
        limit = limit + 1

    playAgain = input("Shall we play the game again?(YES or NO)\n").strip().upper()

print("Thank you for playing, " + playerName + "! See you again!")
