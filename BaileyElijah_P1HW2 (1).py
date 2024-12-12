# Elijah Bailey
# 9/26/24
# P1HW2
# Program that does basic math on numbers that are entered

print ("----------This Program Calculates and displays travel expense----------")
print ()
print ()

# Get Budget From User
budget = int(input("enter budget: "))

# Get travel destination from user
travel_destination = input("Enter Travel Destination: ")

# Gas Budget
gas = int(input("How Much Do You Think You Will Spend On Gas?: "))

# Accomidation budget
hotel = int(input("Approximately, how much will you need for accomidation/hotel?: "))

# Food budget
food = int(input("Last, how much do you need for food?: "))
print ()
print ()
print ("----------Travel Expenses----------")
print ("Location: ", travel_destination)
print ("Initial Budget: ", budget)
print ()
print ("Fuel: ", gas)
print ("Accomidation: ", hotel)
print ("Food: ", food)
print ()
print ()
subtraction_result = budget - gas - hotel - food
print ("remaining balance: ", subtraction_result)
