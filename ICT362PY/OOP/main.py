"""
Main Execution Script (main.py)

Purpose:
1. Entry Point: Coordinates the program by importing classes from organized folder modules.
2. Object Instantiation: Creates specific instances (objects) of classes (e.g., my_dog, your_dog).
3. Method Execution: Calls object methods to run the application logic.

Import Syntax Pattern:
from <folder_or_package>.<module_filename> import <ClassName>
"""

from dog_class_example.dog import Dog
from restaurant.Resturant import Resturant

print("Learning OOP in Python: main.py imports classes from project folders\n")
print("Imported Dog class from the 'dog_class_example' package.\n")

# Instantiating two independent objects from the Dog blueprint
my_dog = Dog("Fito", 6)
your_dog = Dog("Lucy", 10)

# Interacting with my_dog
print(f"My dog's name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

# Interacting with your_dog
print(f"\nYour dog's name is {your_dog.name}")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

print('*' * 40)
print("\nResturant Class:")

#Instantiating three(objects) resturrants from Resturant class
Mexican_resturant = Resturant("Filibertos", "Mexican Food")
Chinese_resturant = Resturant("China Casa", "Chinese Food")
Thai_resturant = Resturant("Pad-Thai Cafe", "Thai Food")

# Calling descripe method from resturant class
Mexican_resturant.describe_restaurant()
Chinese_resturant.describe_restaurant()
Thai_resturant.describe_restaurant()

