#Coder: Nguyễn Ngọc Thảo Vy
#ID: K244111446
#Email: vynntk24411@st.uel.edu.vn
#Description: Exercise 2 - Automatic coffee ordering machine (improve)

blist = ['Americano', 'Café Latte', 'Cappuccino', 'Oranges', 'Colacola', 'Grapefruit']
plist = [2500, 3000, 3000, 4000, 1500, 4000]
blistUserChoose = []  # the menu number of each drink that the user selected
plistUserChoose = []  # the quantity of each drink that the user selected

# Print the menu for food/drink
print("No.", "Food Name\tPrice")
for i in range(len(blist)):
    print(i + 1, '.', blist[i], '\t', plist[i])
print("Please tell me the drink you ordered.")

while True:  # loop for choosing food/drink from the menu
    noFoodName = 0
    # User has to choose from 1 -> n
    while noFoodName <= 0 or noFoodName > len(blist):
        strnoFoodName = input("Please choose the food name(enter number)[{}-{}]:"
                              .format(1, len(blist)))
        # If the value is a digit, convert it to int
        if strnoFoodName.isdigit():
            noFoodName = int(strnoFoodName)
        else:
            noFoodName = 0  # reset to 0 if the input is not valid
    blistUserChoose.append(noFoodName)

    noQuantity = 0
    while noQuantity <= 0:  # quantity must be > 0
        strnoQuantity = input("Please enter quantity[>0]:")
        if strnoQuantity.isdigit():
            noQuantity = int(strnoQuantity)
        else:
            noQuantity = 0
    plistUserChoose.append(noQuantity)

    # Confirm to continue or not
    question = input("Do you want to choose another food?(yes/no):")
    # If no, finish choosing the food/drink
    if question.strip().lower() == 'no':
        break

print("The list of ordered food/drink:")
total = 0
print("Food Name\tPrice\tQuantity\tMoney")
# Loop to print all food/drink that the user has chosen
for i in range(len(blistUserChoose)):
    foodName = blist[blistUserChoose[i] - 1]       # name of the drink
    quantity = plistUserChoose[i]                  # quantity bought
    unitPrice = plist[blistUserChoose[i] - 1]      # unit price
    money = quantity * unitPrice                   # money for this item
    total = total + money                          # add to the total
    print(foodName, "\t", unitPrice, "\t", quantity, "\t\t\t", money)
print("\tThe total amount is:\t", total, " money ")

while True:  # loop for the user to pay money
    strmoney = input("Enter the amount to be paid >>")
    if strmoney.isdigit() == False:
        print(strmoney, " is not valid, it should be a digit number ")
    else:
        paid = int(strmoney)
        if paid < total:
            print("Not enough money, you have to pay ", total, " money ")
        else:
            print("Paid is successfully!")
            if paid > total:
                print("Change is", paid - total, " money")
            break
print("Thank you so much! see you again!")
