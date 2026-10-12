#Coder: Nguyễn Ngọc Thảo Vy
#ID: K244111446
#Email: vynntk24411@st.uel.edu.vn
#Description: Exercise 4 - Multiplication table game machine

import random  # Import random module
import time    # Import time-related modules

correctAns = 0  # Right count
wrongAns = 0    # Wrong count

# Ask how many questions to play (must be a positive integer)
count = 0
while count <= 0:
    strCount = input("How many times should I do?")
    if strCount.isdigit():
        count = int(strCount)
    else:
        count = 0
        print("Please enter a positive integer number!")

while count != 0:
    # Generate numbers from the 3rd to the 9th table
    a = random.randint(3, 9)
    b = random.randint(3, 9)
    # If it is the 5th table, generate random numbers again
    if a == 5 or b == 5:
        continue

    count = count - 1
    print("%d X %d?" % (a, b))
    startTime = time.time()  # Measure reaction time
    try:
        product = int(input())
    except ValueError:
        product = None  # Not a number -> regarded as a wrong answer
    endTime = time.time()
    print("I answered in %.1f seconds" % (endTime - startTime))

    # Check if the multiplication is correct
    if product == a * b:
        correctAns = correctAns + 1
        print("Right!\n")
    else:
        wrongAns = wrongAns + 1
        print("Try again!\n")

print("Total response %d, correct %d times"
      % (correctAns + wrongAns, correctAns))
