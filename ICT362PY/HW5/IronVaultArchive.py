########################################################
# Software Req Doc: HW5 Iron Vault Archive            #
# Release Date: September 23, 2026                    #
# Coder: Alexis Barraza                               #
# Description: This program demonstrates functions,   #
# while loops, regex, dictionaries, user input, and   #
# try/except validation.                              #
########################################################

from datetime import datetime
import re
def validate_string(minNumber, maxNumber, strA):
    """
    Validate that a string is within the allowed length

    Args:
        minNumber: The minimum allowed string length.
        maxNumber: The maximum alled string length
        strA: The string being tested

    Returns:
        True if the string length is within the allowed range.
        False if the string is too short or too long.
    """
    if len(strA) < minNumber:
        return False
    elif len (strA) > maxNumber:
        return False
    else:
        return True
    
# Validate phone number 
def validate_phone(phone_str):
    """
    Validate a phone number using the requried regular expression.

    Args:
        phone_st: The phone number string entered by the user/

    Returns:
        True if the phone number matches the required patterns.
        False if the phone number does not match the pattern.
    """
    pattern = r"^(\(\d{3}\)|\d{3})([ -.]+)(\d{3})([ -.]+)(\d{4})$"
    return re.match(pattern, phone_str) is not None
# validate date function

def validate_date(date_string):
    """
    Validate a date entered in mm/dd/yyyy format.

    Args:
        date_string : The date string entered by user

    Returns:
        True if the date matches the required format and is a valid clander date. False if the format or date is invalid.
    """
    pattern = r"^(0?[1-9]|1[0-2])/(0?[1-9]|[12][0-9]|3[01])/\d{4}$"
    
    # Check if the date matches the required pattern
    if not re.match(pattern, date_string):
        return False
    try:
        datetime.strptime(date_string, "%m/%d/%Y")
        return True
    #If the date does not exist return False
    except ValueError:
        return False

# Validate email
def validate_email(email_str):
    """
    Validate an email address using a regular expression.

    Args:
        email_str: The email address entered by the user.

    Returns:
        True if the email address matches the required pattern.
        False if the email address does not match the pattern.
    """

    pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.match(pattern, email_str) is not None

# IronValutEntry dictionary to hold validated data 
ironVaultEntry = {}

#First name length requirements
min = 2
max = 12

# Last name length requirements
lastMin = 4
lastMax = 15

Firstname_prompt = f"Please enter your first name, minimun of {min} letters max of {max}\n"

Lastname_prompt = f"Please enter your last name, minimum of {lastMin} and max of {lastMax}\n"

# Collect and validate first name
while True:
    
    # Ask the user for their first name
    firstname = input(Firstname_prompt)
    
    # Call validate_string and check if the name is valid
    if validate_string(min, max, firstname):
        
        # Add the valid first name to the dictionary
        ironVaultEntry["FirstName"] = firstname
        
        # Exit the loop once  a valid first name is entered
        break
    else:
        Firstname_prompt = (
            f"Your entry was less then {min} or more than {max}. "
            f"Please re enter you first name\n"
        )

# Collect and validate last name
while True:
    
    # Ask the user for their last name
    lastName = input(Lastname_prompt)
    
    # Call validate_string and check if the name is valid
    if validate_string(lastMin, lastMax, lastName):
        
        # Add the valid first name to the dictionary
        ironVaultEntry["LastName"] = lastName
        
        # Exit the loop once  a valid first name is entered
        break
    else:
        Lastname_prompt = (
            f"Your entry was less then {lastMin} or more than {lastMax}. "
            f"Please re enter you last name\n"
        )
        
# Collect and validate onboard date
while True:
    onboardDate = input("Please enter the driver's onboard date in mm/dd/yyyy format: ")
    
    # Call validate_date
    if validate_date(onboardDate):
        
        # Add the valid date to the dictionary
        ironVaultEntry["OnboardDate"] = onboardDate
        
        # Exit the loop once a valid date is entered
        break
    else:
        print("Invalid date. Please enter a real date. Using mm/dd/yyyy.  ")

while True:
    
    phoneNumber = input (
        "Please enter the driver's phone number "
        "(Ex: 505-555-1234, (505) 555-1234, or 505.555.1234):\n "
    )
       # Call validate_phone and check if the phone number is valid
    if validate_phone(phoneNumber):

        # Add the valid phone number to the dictionary
        ironVaultEntry["Phone"] = phoneNumber

        # Exit the loop once a valid phone number is entered
        break

    else:
        print(
            "Invalid phone number. Please re-enter the phone number."
            "(Ex: 505-555-1234, (505) 555-1234, or 505.555.1234):\n"
        )

# Collect and validate email
while True:
    
    emailAddress = input(
                "Please enter the driver's email address "
                "(example: name@company.com):\n "
            )
    # Call validate_email and check if the email is valid
    if validate_email(emailAddress):
        
        # Add the valid email to the dictionary
        ironVaultEntry["Email"] = emailAddress
        
        # Exit the loop once a valid email is created
        break
    else:
        print(
            "Invalid email. Please re-enter the email address "
            "example: name@company.com)"
            )

# Print the final populated dictionary
print("\n" + "=" * 40)
print("Iron Vault Driver Record")
print("=" * 40)
print(ironVaultEntry)