# P4HW2
# Elijah Bailey
# 11/7/2024

import sys

# Loop to keep asking for employees until the user quits
while True:
    # Input for employee name
    employee = input("Enter employee name or 'q' to quit: ")
    if employee.lower() == 'q':  # check for quit input
        sys.exit("Exiting program.")
    
    # Input for regular hours, pay rate, and overtime
    try:
        hours_worked = float(input("How many hours did they work? "))
        pay_rate = float(input("What is their hourly pay rate? $"))
        overtime_hours = float(input("How many overtime hours did they work? "))
    except ValueError:
        print("Invalid input, please enter numeric values.")
        continue  # skip to the next iteration of the loop if input is invalid

    # Calculate regular pay and overtime pay
    overtime_rate = pay_rate * 1.5  # Assuming overtime is paid at 1.5 times the regular rate
    regular_pay = hours_worked * pay_rate
    overtime_pay = overtime_hours * overtime_rate

    # Total gross pay
    gross_pay = regular_pay + overtime_pay

    # Display the results
    print("\n" + "-"*40)
    print(f"Employee: {employee}")
    print(f"Hours Worked: {hours_worked}")
    print(f"Overtime: {overtime_hours}")
    print(f"Hourly Pay Rate: ${pay_rate:.2f}")
    print(f"Overtime Pay Rate: ${overtime_rate:.2f}")
    print(f"Gross Pay: ${gross_pay:.2f}")
    print("-"*40 + "\n")
