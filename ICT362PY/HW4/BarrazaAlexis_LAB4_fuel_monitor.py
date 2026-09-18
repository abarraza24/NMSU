########################################################
# Software Req DOC: Hw4 Fuel monitor                   #
# Release Date: September 17, 2026                     #
# Code: Alexis Barraza                                 #
# Description: This progam demonstrates user input,    #
# boolean conditions, arithmetic, and while loops      #
########################################################

# Pseudo Code
# Ask the user to input the starting fuel amount example 100
fuel = float(input("Enter a starting fuel amount(liters): "))
# Use a While loop that continues as long as the fuel level is above 15
while fuel > 15:
    # Inside the loop
    # Will ask the pilot to enter the fuel spent in the latest thruster burst
    spent = float(input("Enter the fuel spent in the latest thruster burst: "))
    # then will subtract that amount from the remaining fuel
    # after subtraction it replaces the old value of fuel with the new result
    fuel -= spent
    # Then will display the updated fuel level
    # when the fuel drops <= 15 the loop stops
    if fuel > 15:
         print(f"Remaining fuel: {fuel:.2f} (liters)")
    # if fuel is equal to or less then 15 we stop the loop imediately and print warning
    elif fuel <= 15:
        break;
# Print a final warning "LOW FUEL WARNING: Thruster sequence stopped. Remaining fuel: X liters."
print(f"LOW FUEL WARNING: Thruster sequence stopped. Remaining fuel: {fuel:.2f} liters.")