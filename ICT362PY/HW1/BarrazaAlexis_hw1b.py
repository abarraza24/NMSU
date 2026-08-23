# ICT362 - hw1b variables
# Author - Alexis Barraza 
# Date: August 22, 2026

#Name variable with leading white space char, and escape sequences \t & \n
name = "  \tAlexis Barraza-Andrade\n  "

#Origninal Name had to use repr() for string representation
# with leading white space char, and escape sequences \t & \n
print("Original Name")
print(repr(name))

# Removing whitespace trailing only
print("\nUsing strip()")
print(name.strip())

# Removing right side only whitespace trailing
print("\nUsing rstrip()")
print(name.rstrip())

# Removing left side only whitespace trailing
print("\nUsing ltrip()")
print(name.lstrip())


