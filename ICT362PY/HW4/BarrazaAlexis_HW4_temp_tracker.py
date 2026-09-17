########################################################
# Software Req DOC:Temp Tracker HW4                    #
# Release Date: September 16, 2026                     #
# Coder: Alexis Barraza                                #
# Description: This progam demonstrates,               #
# Python input, user input, while loops and            #
# celcius to Fahrenheit                                #
########################################################


#Psudo code
# A variable to store user_input temp 
# use that input value to convert to Fahrenheit 
# Prints the converted temp in a flot format
# Place the input statement inside a while loop that keeps count of how many
# temp converted during the session
# Ends the loop when user enters "quit"
# After the loop ends, prints the total number of conversions completed
# and the average of temps entered

converted_temp_count = 0
total = 0
user_input = ""

while user_input != "quit":
    
    # Keep input as a string first to check for "quit"
    user_input = input("Enter a number in Celsius or type quit to end program: ")
    
    # Convert the input to lowercase and remove extra spaces.
    if user_input.lower().strip() =="quit":
        break # break exits the entire loop immediately
    
    #Convert to float after verifying it's not quit
    celsius = float(user_input)
    #Convert celsius to fahrenheit
    celsius_to_fahrenheit = (celsius * 1.8 ) + 32
   
    
    # Track the number of coversionns and the total celcius values.
    total += celsius
    converted_temp_count += 1
   
    
    print(f"The Celsius value of {celsius:.2f}°C. In Fahrenheit is: {celsius_to_fahrenheit:.2f}°F")

# If the user quits before entering a temp
# avoid dividing by zero.
if converted_temp_count == 0:
    print(f"Sorry to see you go without trying the program :( ")
else:
    average = total/converted_temp_count
    print(f"There were {converted_temp_count} values entered with an average of {average:.2f}°C")

