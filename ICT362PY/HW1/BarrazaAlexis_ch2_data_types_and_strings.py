# ICT362 - Modified ch2_data_types_and_string.py
# Author - Alexis Barraza 
# Date: August 23, 2026

# Sample Program #1
#print ("Hello World!\n")
#print(123123123123123123123123123123123123123123123123 + 1)
#print(10)
#print(0o10)
#print(0x10)
#print(0b10)
#print('This string contains a single quote (\') character.')
#print("This string contains a double quote (\") character.")
#print('a\
#... b\
#... c')
#print('foo\\bar')
#print('foo\tbar')
#print("a\141\x61")
#a = 4
#b = 3
#a=b
#+a
#-b
#print(a % b)
#

#Modified Sample of program 1

# Strings variables
greeting = ("Hello World!\n")
single_quote = ("This string contains a single quote (\') character.")
double_quote = ("This string contains a double quote (\") character.")
mulit_line_letters =("a\n... b\n... c")
backlash_message = ("foo\\bar")
tab_message = ("foo\tbar")
escape_message = ("a\141\x61")

# Number variables
large_number = (123123123123123123123123123123123123123123123123 + 1)
number_ten = (10)
octal_number = (0o10)
hex_number = (0x10)
binary_number = (0b10)
a = 4
b =3

# New string for 3 method variables from Python Documentation
course_name = ("software technology ii")
full_name = ("alexis barraza")
school_name = ("New Mexico State University")


# Using new variables for new string methods form Python Documentation
print("\nThree new string methods:")
print("Capitalize():")
print(course_name.capitalize())

print("\nupper():")
print(full_name.upper())

print("\nreplace():")
print(school_name.replace("New Mexico State University", "NMSU"))

# Original values of the new variables unchanged
print("\nOriginal variables that are still unchanged:")
print(course_name)
print(full_name)
print(school_name)


# The original sample program output
print("\nOrignal Sample 1 output:")
print(greeting)
print(large_number)
print(number_ten)
print(octal_number)
print(hex_number)
print(binary_number)

print(single_quote)
print(double_quote)
print(mulit_line_letters)
print(backlash_message)
print(tab_message)
print(escape_message)
a = b
+a
-b
print(a % b)
print(a ** b)




