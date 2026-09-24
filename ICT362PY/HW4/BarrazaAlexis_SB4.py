########################################################
# Software Req Doc: HW
# Release Date: September 17, 2026
# Code: Alexis Barraza
# Description: This program demonstrates user input,
# if-else statements, while loops, lists, and moving
# items from one list to another.
########################################################

# Pseudo Code
# Variables
group_size = 0
toppings = []
user_input = ""
# Requirement 1: Welcome the user to Zion's Pizza Restaurant
print("\tRequirement 1")  # Check the dinner group size
print("=" * 40)
print(f"  Welcome, to Zion's Pizza Restaurant!")
print("=" * 40)
group_size = int (input("How many people are in your group? "))
# Ask how many people are in the dinner group
# If there are more than 8 people, tell them they have to wait
if group_size > 8:
    print("Im sorry you have to wait! ")
else:
    # Otherwise tell them their table is ready
    print("Your table is ready! follow me")

    # Visual separator
    print("=" * 40)
    print("\tRequirement 2")  # Ask for pizza toppings until quit is entered

    # Requirement 2: Ask the user what topping they want on their pizza
    # Use a while loop that keeps asking for toppings
    # Stop the loop when the user enters "quit"
    while user_input != "quit":
        # Keep the user input as a string to check for quit
        user_input = input("What toppings would you like on your Pizza ?\nEnter 'quit' when you are finished: ")
        
        # Clean the input to check for quit by converting to lowercase and removing extra spaces
        cleaned_input = user_input.lower().strip()
        
        if cleaned_input== "quit":
            break # break exits the enitre loop immediately
        
        # Requirement 3: Print a message each time a topping is added
        print("\tRequirement 3")  # Add the current topping to the pizza
        toppings.append(user_input.strip())
        print(f"Added! Your current toppings {', ' .join(toppings)}")
        print()
    # Final summary after the loop ends
    print("\n" + "=" * 40)
    if len(toppings) > 0:
        print(f"Awesome! Your pizza will have: {', '.join(toppings)}")
    else:
        print("Your pizza will hane no toppings.")
    print("=" * 40)
        

# Requirement 4: Create a list called sandwich_orders
# Add different sandwich names to sandwich_orders
print("\tRequirement 4")  # Create a list of sandwich orders

sandwich_orders = [
    "roast beef",
    "turkey",
    "grilled cheese",
    "veggie"
]

# Requirement 5: Create an empty list called finished_sandwiches
print("\tRequirement 5")  # Create an empty list for completed sandwiches
finished_sandwiches = []

# Requirement 6: Loop through sandwich_orders
# Print a message showing which sandwich is being made
print("\tRequirement 6")  # Process each sandwich order

while sandwich_orders:
    # Remove the first sandwhich from sandwhich_orders
    current_sandwich = sandwich_orders.pop(0)
    print(f"Im working on your {current_sandwich} sandwich.")
    
    # Requirement 7: Move each completed sandwich
    # from sandwich_orders into finished_sandwiches
    finished_sandwiches.append(current_sandwich)
# Requirement 7
print("\tRequirement 7")  # Sandwiches have been moved to finished_sandwiches
print()

# Requirement 8: Loop through finished_sandwiches
# Print a message showing each sandwich that was made
print("\tRequirement 8")  # Print all completed sandwiches
for sandwich in finished_sandwiches:
    print(f"I made a {sandwich} sandwich.")
# Requirement 9: Add comments throughout the code
# explaining what each requirement does
print("\n" + "=" * 40)
print("\tRequirement 9 - Summary")
print("=" * 40)

print("1. Checks the dinner group size and tells the user if they need to wait or if their table is ready.")
print("2. Keeps asking for pizza toppings until the user enters quit.")
print("3. Adds each topping to the pizza and confirms it to the user.")
print("4. Creates a list of sandwich orders.")
print("5. Creates an empty list for finished sandwiches.")
print("6. Processes each sandwich order and prints which sandwich is being made.")
print("7. Moves each completed sandwich into the finished_sandwiches list.")
print("8. Prints each sandwich that was completed.")
print("9. Summarizes what each requirement does.")