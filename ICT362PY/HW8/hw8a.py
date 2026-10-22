########################################################
# Software Req Doc: HW8 Working with Files in Python   #
# Release Date: October 12, 2026                       #
# Coder: Alexis Barraza                                #
# Description: This program demonstrates different ways
# to read from a text file and write user input to a file.#
########################################################

# Requirement 1.4: Read the entire file.
with open("hw8a.txt", "r") as file:
    print("--- Reading in the entire file:")
    contents = file.read()
    print(contents)
    
print(100 * "=")

# Requirement 1.5: Loop over the file object.
with open("hw8a.txt", "r") as file:
    print("--- Looping over the lines: ")
    
    for line in file:
        print(line.strip())
        
print(100 * "=")

# Requirement 1.6: Store the lines in a list.
with open("hw8a.txt", "r") as file:
    lines = file.readlines()
    
print("--- Storing the lines in a list:")

for line in lines:
    print(line.strip())
    
print(100 * "=")

# Requirement 1.7: Ask the user for their name.
name = input("What's your name? ")

# Requirement 1.8: Store the user's name in a file.
with open("hw8a_gest.txt", "w") as guest_file:
    guest_file.write(name)
    
print(f"Thank you, {name}! Your name was saved to hw8a_guest.txt.")