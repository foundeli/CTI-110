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

if money == 0:
    print("No change")

# Check for debt
if money < 0:
    print("OUCH!! You're in debt")
    
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
# print(f"Pennies: {num_pennies}")

else:
    num_dollars = 0
    num_quarters = 0
    num_dimes = 0
    num_nickels = 0
    num_pennies = 0

# Print dollar amount gramatically correct
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} dollar")
    else: #variable is greater than one
        print(f"{num_dollars} dollars")

#Print quarter amount gramatically correct
if num_quarters > 0:
    if num_dollars == 1:
        print(f"{num_quarters} quarters")
    else: # Variable is grater than one
        print(f"{num_quarters} quarters")

#Print dimes amount gramatically correct
if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} dime")
    else: # Variable is grater than one
        print(f"{num_dimes} dime")

#Print nickles amount gramatically correct
if num_nickles > 0:
    if num_nickles == 1:
        print(f"{num_nickles} nickle")
    else: # Variable is grater than one
        print(f"{num_nickles} nickle")

#Print penny amount gramatically correct
if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} penny")
    else: # Variable is grater than one
        print(f"{num_pennies} penny")
