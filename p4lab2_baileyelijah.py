
# Elijah Bailey
# 10/31/2024
# P4Lab2
# Program ask user for integer
# While loop to control program running continuously
run_again = "yes"
valid_input = ["yes", "y", "no", "n"]

while run_again == "yes" or run_again == "y":
    user_int = int(input("Enter an integer: "))
    if user_int >=0:
        for num in range(1,13):
            print(f"{user_int} * {num} = {user_int * num}")
   
    else:
        print("Cannot accept negative values!!")
  
    print()
 
    run_again = input("Would you like to run the program again?").lower()
  
# Valudate the user's input
 
    while run_again not in valid_input:
 
        print("INVAALID REPONSE ENTERED!")
        run_again = input("Would you like to run the program again?").lower()

 
# Loop breaks
print ("Exiting programs...")
