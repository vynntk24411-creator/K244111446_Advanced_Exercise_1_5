#Coder: Nguyễn Ngọc Thảo Vy
#ID: K244111446
#Email: vynntk24411@st.uel.edu.vn
#Description: Exercise 5 - Multiplication table game machine (improve)

import random
import time

correctAns = 0  # Right count
wrongAns = 0    # Wrong count

# List of the multiplications that were already asked (each item is a pair (a, b))
askedList = []

# 45 seconds, if the user answers over limitTime, the answer is wrong
limitTime = 45

# Tables 3, 4, 6, 7, 8, 9 -> 6 x 6 = 36 different multiplications at most
MAX_QUESTIONS = 36

# Ask how many questions to play (1 -> 36)
count = 0
while count <= 0 or count > MAX_QUESTIONS:
    strCount = input("How many times should I do? [1-%d]:" % MAX_QUESTIONS)
    if strCount.isdigit():
        count = int(strCount)
    else:
        count = 0
    if count <= 0 or count > MAX_QUESTIONS:
        print("Please enter an integer number from 1 to %d!" % MAX_QUESTIONS)

while count != 0:
    # Generate numbers from the 3rd to the 9th table
    a = random.randint(3, 9)
    b = random.randint(3, 9)
    # If it is the 5th table, generate random numbers again
    if a == 5 or b == 5:
        continue
    # If this multiplication was already asked, generate random numbers again
    if (a, b) in askedList:
        continue
    askedList.append((a, b))

    count = count - 1
    print("%d X %d?" % (a, b))
    # Measure reaction time
    startTime = time.time()
    try:
        product = int(input())
    except ValueError:
        product = None  # Not a number -> regarded as a wrong answer
    endTime = time.time()
    # Get the answering time
    calculateTime = endTime - startTime
    print("I answered in %.1f seconds" % calculateTime)
    if calculateTime > limitTime:
        print("You took too long to answer, the limit time is %d seconds, "
              "you answered in %.1f seconds" % (limitTime, calculateTime))

    # Check if the multiplication is correct and in time
    if product == a * b and calculateTime <= limitTime:
        correctAns = correctAns + 1
        print("Right!\n")
    else:
        wrongAns = wrongAns + 1
        print("Try again!\n")

print("Total response %d, correct %d times"
      % (correctAns + wrongAns, correctAns))
