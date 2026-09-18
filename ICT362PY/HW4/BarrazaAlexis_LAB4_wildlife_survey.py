########################################################
# Software Req DOC: HW4 Wildlife Survey               #
# Release Date: September 17, 2026                    #
# Code: Alexis Barraza                                #
# Description: This program demonstrates user input,  #
# sentinel values, while loops, and running totals.   #
########################################################


# Pseudo Code
# Create a variable to keep track of the total animals spotted
# Ask the ranger to enter the number of animals spotted
# Use -1 as the sentinel value to end the survey
# If the input is not -1 add it to the running total
# Print the updated total after each observation post
# When the ranger enters -1 stop the loop
# Print the grand total of animals spotted

#Create a variable to store running total
total_animals = 0

#Create a variable for number of animals spotted
animals_spotted = 0

# Keep looping until the ranger enters -1
while animals_spotted != -1:
    
    # Ask the ranger how many animals were spotted at the observations post
    # This is where we convert the input into an integer
    animals_spotted = int (input("Enter the number of animals spotted or enter -1 to end survey: "))
    
    #checkc that the ranger did check the sentinal value flag,
    if animals_spotted != -1:
        # Add the current sightings to the running total
        total_animals += animals_spotted
        
        #Print the updated total
        print(f"Updated total animals spotted: {total_animals}")

# Once -1 is entered the while loop stops and prints the final total 
print(f"Grand total of animals spotted: {total_animals}")