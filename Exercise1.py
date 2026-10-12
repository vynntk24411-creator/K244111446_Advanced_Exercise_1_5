#Coder: Nguyễn Ngọc Thảo Vy
#ID: K244111446
#Email: vynntk24411@st.uel.edu.vn
#Description: Exercise 1 - Automatic coffee ordering machine

# Price of each drink (won)
PRICE_AMERICANO = 2500
PRICE_LATTE = 3000
PRICE_CAPPUCCINO = 3000

print("Please tell me the drink you ordered.")
noA = int(input("Number of Americano (cups):"))
noL = int(input("Number of cafe lattes (cups):"))
noC = int(input("Number of cappuccinos (cups):"))

# Calculate the total order amount
total = 0
total += noA * PRICE_AMERICANO
total += noL * PRICE_LATTE
total += noC * PRICE_CAPPUCCINO

print("The total amount is:", total, " money ")

money = int(input("Enter the amount to be paid >>"))
if money < total:
    print("Not enough money.")
else:
    print("Change is", money - total, " money ")
