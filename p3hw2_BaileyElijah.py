# Elijah Bailey
#10/24/2024



# Calculate reg and OT pay, given an empoyees hours worked


input: get the name as a string
input: Get the hours worked as an integer
Input: Get the pay rate as a float

Output: Print employee name

if hours worked is grater than 40:
    Calculate OT hours wored by subtracting 40 from hours worked
    Calculate OT pay (OT hours * pay rate * 1.5)
    Calculate reg pay(40 * regular pay rate)
    Calculate gross by adding OT pay and reg pay

else (employee worked 40 or less hours):
    overtime hours = 0
    overtime pay = 0
    calculate reg pay by multiplying original hours worked by reg pay rate


Output:
Display total hours worked
Display Regular pay rate
Display overtime hours worked
Display OT pay (OT hours times OT pay rate)
Display pay for regular hours worked at reg pay rate
Display gross pay - both reg pay and OT pay

