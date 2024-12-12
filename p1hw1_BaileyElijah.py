# Elijah Bailey
# 9/17/2024
# P1HW1
# Input and Output with mathematical expressions

print("------Calculating Exponents------")
print()
print()

# Get base value (as an integer) from the user
base_value = int(input("Enter an integer as a base value: "))

# Get exponent value from user
exponent = int(input("Enter as integer as the exponent: "))

# Raise the base_value to the exponent
value = base_value ** exponent

print()
print()

# Display output to the user
print(base_value, "raise to the power of", exponent, "is", value, "!!")

print()
print()
print("---------Addition and Subtracion---------")
print()
print()
start_num = int(input("Enter a starting interger: "))
add_num = int(input("Enter an interger to add: "))
sub_num = int(input("Enter an integer to subtract: "))
print()
print()
print(start_num, "+", add_num, "-", sub_num, "is equal to", start_num + add_num - sub_num)
