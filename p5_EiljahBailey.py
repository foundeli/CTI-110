import random

def calcCashBack():
    # generate a random float for amount owed to store
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${total_owed:.2f}")
    cash = float(input("How much cash will you put in the self_checkout? "))
    # Calculate cash back
    cash_back = cash - total_owed
    return cash_back  # Return the cash back amount

def disperseCashBack(change):
    # Convert the float value into an integer (in cents)
    change = int(round(change * 100, 2))

    if change == 0:
        print("No Change Due")
        return

    # Calculate the amount of each coin needed
    num_dollars = change // 100
    change -= (num_dollars * 100)

    num_quarters = change // 25
    change -= (num_quarters * 25)

    num_dimes = change // 10
    change -= (num_dimes * 10)

    num_nickels = change // 5
    change -= (num_nickels * 5)

    num_pennies = change // 1

    # Display coins owed
    if num_dollars > 0:
        print(f"{num_dollars} Dollar{'s' if num_dollars > 1 else ''}")
    if num_quarters > 0:
        print(f"{num_quarters} Quarter{'s' if num_quarters > 1 else ''}")
    if num_dimes > 0:
        print(f"{num_dimes} Dime{'s' if num_dimes > 1 else ''}")
    if num_nickels > 0:
        print(f"{num_nickels} Nickel{'s' if num_nickels > 1 else ''}")
    if num_pennies > 0:
        print(f"{num_pennies} Penny{'ies' if num_pennies > 1 else ''}")

# Define the main function
def main():
    print("Welcome to the self checkout")
    cash_back = calcCashBack()  # Get the cashback amount
    print(f"Change is ${cash_back:.2f}")
    disperseCashBack(cash_back)  # Dispense the cashback

# Call the main function
if __name__ == "__main__":
    main()
