"""
    Module: BarrazaAlexis_Lesson 2
    Author: Alexis Barraza
    Date: August 26, 2026
    Course: ICT 362 - Software Technology II
    
    Assignment: Lists, Tuples, and For Looping Statements
"""

# Task 1: Organize animal observations
# 100+ animal observations
# Add new observation as they are collected
# Correct mistakes in the dataset.
# Remove invalid entries.
# Examine subsets of data from particular dates or locations.
# Sort observation to find patterns

observations = [
    "deer", "rabbit","fox", "deer", "bear", "coyote", 
    "rabbit", "deer", "hawk", "fox"
]

# Reasearchers collected three new observations
observations.append("turkey")
observations.append("deer")
observations.append("owl")

# Volunteer accidentally entered "rabit" instead of "rabbit"
observations.append("rabit")
print(f'Before remove() method was used {observations}\n')
observations.remove("rabit")

print(f'After remove() method was used {observations}')

# Real datasets contain typos that must be cleaned befory analysis.
# This would remove 'owl' since it's the last item in the list and stored
# In duplicate
duplicate = observations.pop()

# First five observations came from Camera Station A.
# station_a stores  animals 0-4 five is excluded
station_a = observations[:5]
print(station_a)

# The last three observations came from Camera Station C
station_c = observations[-3:]
print(f'Staion_C Observaations {station_c}')

# Researches want a larger set of data but need specied grouped together
sorted_observations = sorted(observations)
print(f'Observations will be sorted in alphabetical order {sorted_observations}')