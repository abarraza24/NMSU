########################################################
# Software Req DOC: SB3                                #
# Release Date: September 10, 2025                     #
# Code: Alexis Barraza                                 #
# Description: This progam demonstrates dictionaries,  #
# loops, key-value pairs, and list of dictionaries.    #
########################################################

#Requirement 1: Create a glossary dictionary with five programming terms
print("Requirement 1: Glossary Dictionary")

# Requirement 1.1: Creating a glossary for five programmin terms
glossary = {
    "List": "A collection of items stored in a particular order.",
    "Tuple": "A collection of items that cannot be changed after it is created.",
    "For Loop": "A loop that repeats code for each item in a collection",
    "If Statement": "A statement that checks conditions and runs if the condition is True.",
    "Boolean Expression": "An expression that evaluates to either True or False."
}

# Requirement 1.2: Looping through each key and value in the glossary dictionary
for word, defenition in glossary.items():
    # Requirement 1.3: Print each programming word and its definition.
    print(f"\t{word}-{defenition}")
    

# Requirement 2: Creating a three dictionaries representing different people.
print("\nRequirement 2: People Dictionary List")

# Requirement 2.1: Store information about the first person
person_1= {
    "first_name": "Alex",
    "last_name": "Barraza",
    "age": "28",
    "city": "Las Cruces"
}

# Requirement 2.2: Store information about the second person
person_2 = {
    "first_name": "Jacky",
    "last_name": "Carreon",
    "age": "26",
    "city": "Albuquerue"
}

# Requirement 2.3: Store information about the third person
person_3 = {
    "first_name": "Fito",
    "last_name": "Barraza",
    "age": "6",
    "city": "Santa Fe"
}

# Requirement 2.4: Create an empty list to store the person dictionaries.
people =[]

# Requirement 2.5: Append each person dictionary to the people list.
people.append(person_1)
people.append(person_2)
people.append(person_3)

# Requirement 2.6: Loop through each dictionary stored in the people list
for person in people:
    # Requirement 2.7: Print all the information stored for people
    print(f"\t{person['first_name']} {person['last_name']}, " 
          f"of {person['city']}, is {person['age']} years old."
          )