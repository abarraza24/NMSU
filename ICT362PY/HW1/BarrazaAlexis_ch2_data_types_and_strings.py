"""
    Module: BarrazaAlexis_ch2_data_types_and_strings.py
    Author: Alexis Barraza
    Date: August 24, 2026
    Course: ICT 362 - Software Technology II
    Assignment: Skill Builder 1 - Code style, DocStrings, Comments, and Software Requirements
    
    Description:
        This program demonstrates basic Python variables, data types, string printing,
        escape characters, arithmetic operators, and string methods.
        
    
    Software Requirements:
        Req 1: Demonstrate string printing and basic string manipulation
        Req 2: Demonstrate data types and variables.
        Req 3: Print lowercase "a" using ASCII and hexidecimal escapte values.
        Req 4: Assignm and reassign values to variables.
        Req 5: Demonstrate unary operators.
        Req 6: Domonstrate modulus and exponent operators_
        Req 7: Demonstrate three Python string methods.
        Req 8: Show string methods return a new values and do not change the original
                variables unless reassigned.
"""

# Req 1.1 : store a greeting string that includes a new line
greeting = ("Hello World!\n")

# Req 1.3 stores a message(string) that includes a single quote
single_quote = ("This string contains a single quote (\') character.")

# Req 1.4 stores a message(string) that includes a double quote
double_quote = ("This string contains a double quote (\") character.")

# Req 1.5 Stores a string that includes a backlash character.
backlash_message = ("foo\\bar")

# Req 1.6 string that prints across a multiple lines
mulit_line_letters =("a\n... b\n... c")

# Req 1.2 Stores a string that includes a tab escape sequence.
tab_message = ("foo\tbar")

# Req 3: Store a string that prints a lowercase "a" using ASCII and hex escape values.
escape_message = ("a\141\x61")

#  Req 2.1 Stoe the result of a long integer operation
large_number = (123123123123123123123123123123123123123123123123 + 1)

# req 2.2 Storing values using decimal, octal, hexadecimal and binary notation.
number_ten = (10)
octal_number = (0o10)
hex_number = (0x10)
binary_number = (0b10)

#Req 4: Assign values to variables a and b
a = 4
b =3

# Req 7: Stores strings that will be used with three Python string methods.
course_name = ("software technology ii")
full_name = ("alexis barraza")
school_name = ("New Mexico State University")


# Req 7.1: Demonstrate capitalize(), which capitalizes the first character.
print("\nThree new string methods:")
print("Capitalize():")
print(course_name.capitalize())

# Req 7.2: Demonstrate upper(), which converts the string to uppercase.
print("\nupper():")
print(full_name.upper())

# Req 7.3: Demonstrate replace(), which replaces one string value with another.
print("\nreplace():")
print(school_name.replace("New Mexico State University", "NMSU"))

# Req 8: Print the original variables to show the string methods did not change them.
print("\nOriginal variables that are still unchanged:")
print(course_name)
print(full_name)
print(school_name)


# Req 1 and Req 2: Print the original sample program output.
print("\nOrignal Sample 1 output:")
print(greeting)
print(large_number)
print(number_ten)
print(octal_number)
print(hex_number)
print(binary_number)

# Req 1.2 through Req 1.6 and Req 3: Print strings with escape characters.
print(single_quote)
print(double_quote)
print(mulit_line_letters)
print(backlash_message)
print(tab_message)
print(escape_message)

# Req 4.1: Reassign the value of a to equal the value of b.
a = b

# Req 5.1 and Req 5.2: Demonstrate unary positive and negative operators.
+a
-b
# Req 6.1: Print the result of the modulus operator.
print(a % b)
# Req 6.2: Print the result of the exponentiation operator
print(a ** b)




