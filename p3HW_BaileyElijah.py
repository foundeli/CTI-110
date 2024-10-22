# Elijah Bailey
# P3HW2
# 10/22/24

# Regular Division
print(100/3)

#Floor Division - returns the whole number
print(100//3)

# Modules Division - return the remainder only as an integer
print(100%3)
print(7%4)
...

# Get money value from user as a float
money = float(input("Enter the amount of money as a float: $"))

# Convert money to a whole number
money = round(money * 100)

print(money)

# Calculate the amount of dollars in the money variable
num_dollars = money // 100
print(f"Dollars: {num_dollars}")

# Remove the dollars from money variable
money = money - (num_dollars * 100)

# Calculate the amount of quarters in the money variable
num_quarters = money // 25
print(f"Quarters: {quarters}")

# Become the quarters from money variable
money = money - (num_quarters * 25)

# Calculate the amount of dimes in the money variable
num_dimes = money // 10
print(f"Dimes: {num_dimes}")

# Remove the quarters from money variable
money = money - (num_dimes * 10)

# Calculate the amount of nickles in the money variable
num_nickles = money // 5
print(f"Nickles: {num_nickels}")

# Remove the quarters from money variable
money = money - (num_nickles * 5)

# Create a variable for pennies
num_pennies = money
print(f"Pennies: {num_pennies}")
