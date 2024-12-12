# HW1_BAILEYELIJAH
# 11/5/24


numItems = int(input("How many items will you purchase? "))
storeItems=["pencils", "notebook", "headphones",\
            "mouse" "keyboard", "marker", "DVD"]

# Create a list to hold valie inputs
cart = []

# Show user items in list
print(*storeItems)

# For loop to iterate numItems times
for item in range (numItems):
    userInput = input(f"Enter item # {item + 1}: ")
    while userInput not in storeItems:
        print(f"{userInput} is not in stock!")
        userInput = input(f"Enter item # {item + 1}: ")
        # Once valud unput is given, add it to a list
        cart.append(userInput)

print()
print("You are done with shopping!!")
print()
print("here are the items you purchased")
# loop through cart and print each item
for i in cart:
    print()
    
