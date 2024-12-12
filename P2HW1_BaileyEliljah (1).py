# Elijah
# 10/8/2024
# P2HW1

# Get budgets from user
print("This program calculates and displays travel expenses")
total_budget = float(input("Enter Budget: "))
print()
travel_destination = input ("Enter Your Travel Destination: ")
print()
gas_budget = float(input ("How much do you think you will spend on gas? "))
print()
accomidation_budget = float(input ("Approximately, how much will you need for accomidation/hotel"))
print()
food_budget = float(input ("Last, how much do you need for food? "))
print()
print()
print()
# print travel expense
print ("----------Travel Expenses-----------")
print(f"{'Location:':<18}{travel_destination}")
print(f"{'Initial Budget:':<18}${total_budget:,.2f}")
print(f"{'Fuel:':<18}${gas_budget:,.2f}")
print(f"{'Accomidation:':<18}${accomidation_budget:,.2f}")
print(f"{'Food:':<18}${food_budget:,.2f}")
print ("------------------------------------")
print()
total = total_budget - gas_budget - accomidation_budget - food_budget
print(f"{'Remaining Balance:':<18}${total:,.2f}")
