"""
Module: BarrazaAlexis_Lesson 3
Author: Alexis Barraza
Date: August 26, 2026
Course: ICT 362 - Software Technology II

Assignment: Working with Logic statements and Dictionaries

Description:
    The purpose of this program is to work with logic operators, for loops and dictionaries.
    It converts student number grades into a letter grade.
"""

# Appendix A class Grades Dictionary 
classGrades = {
"Ava": 90,
"Liam": 77,
"Emma": 83,
"Noah": 87,
"Olivia": 72,
"Elijah": 94,
"Sophia": 59,
"James": 85,
"Isabella": 98,
"William": 89,
"Mia": 66,
"Benjamin": 82,
"Charlotte": 84,
"Lucas": 75,
"Amelia": 91,
"Henry": 79,
"Harper": 86,
"Alexander": 73,
"Evelyn": 88,
"Michael": 49,
"Abigail": 68,
"Daniel": 97
}

# Empty Dictionary for letter grades
classLetterGrades ={}
# Loop through grade(statement) in the classGrades dictionary 
for grade in classGrades:
    # If the student's grade is 90 or higher we assign letter 'A'
    if classGrades[grade] >= 90:
        classLetterGrades[grade] = "A"
        
    # If the student's grade is 80 or higher we assign letter 'B'
    elif classGrades[grade] >= 80:
        classLetterGrades[grade] = "B"
    # If the student's grade is 70 or higher we assign letter 'C'
    elif classGrades[grade] >= 70:
        classLetterGrades[grade] = "C"
    # If the student's grade is 60 or higher we assign letter 'D'
    elif classGrades[grade] >= 60:
        classLetterGrades[grade] = "D"
    # If  non of the conditions are true assign letter 'F'
    else:
        classLetterGrades[grade] = "F"
        

# Loop through the classLetterGrades.items(), which gives us the key and value
# and stores them in student and grade. Print the student name in a 12 
# Character field and print the grade right aligned in a 3 character field
for student, grade in classLetterGrades.items():
    print(f"Student {student:12} recieved a grade of {grade:>3}")
