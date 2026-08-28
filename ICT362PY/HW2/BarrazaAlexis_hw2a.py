"""
Module: BarrazaAlexis_Lesson 2
Author: Alexis Barraza
Date: August 26, 2026
Course: ICT 362 - Software Technology II

Assignment: Lists, Tuples, and For Looping Statements hw2a
"""

# Task 2: Hands-on simulating a Real Research Dataset
# Appendix A
trailCamList = [
    "deer",
    "rabbit",
    "fox",
    "deer",
    "bear",
    "coyote",
    "rabbit",
    "deer",
    "hawk",
    "fox",
    "squirrel",
    "deer",
    "raccoon",
    "rabbit",
    "turkey",
    "deer",
    "fox",
    "opossum",
    "hawk",
    "rabbit",
    "deer",
    "coyote",
    "squirrel",
    "deer",
    "bear",
    "rabbit",
    "fox",
    "turkey",
    "deer",
    "hawk",
    "rabbit",
    "raccoon",
    "deer",
    "fox",
    "coyote",
    "rabbit",
    "deer",
    "owl",
    "squirrel",
    "deer",
    "rabbit",
    "fox",
    "bear",
    "deer",
    "hawk",
    "turkey",
    "rabbit",
    "coyote",
    "deer",
    "fox",
    "rabbit",
    "squirrel",
    "deer",
    "racoon",
    "hawk",
    "deer",
    "fox",
    "rabbit",
    "turkey",
    "deer",
    "coyote",
    "squirrel",
    "deer",
    "rabbit",
    "owl",
    "fox",
    "deer",
    "bear",
    "rabbit",
    "hawk",
    "deer",
    "fox",
    "cojote",
    "rabbit",
    "squirrel",
    "deer",
    "raccoon",
    "fox",
    "deer",
    "turkey",
    "rabbit",
    "hawk",
    "deer",
    "coyote",
    "fox",
    "rabbit",
    "squirrel",
    "deer",
    "owl",
    "rabbit",
    "fox",
    "deer",
    "bear",
    "turkey",
    "rabbit",
    "deer",
    "hawk",
    "fox",
    "coyote",
    "rabbit",
    "deer",
    "squirrel",
    "raccoon",
    "deer",
    "fox",
    "rabbit",
    "hawk",
    "deer",
    "turkey",
    "coyote",
    "rabbit",
    "fox",
    "deer",
    "squirrel",
    "owl",
    "deer",
    "rabbit",
    "fox",
    "bear",
    "deer",
    "hawk",
    "rabbit",
    "coyote",
    "deer",
    "fox",
    "squirrel",
    "rabbit",
    "deer",
    "raccoon",
    "hawk",
    "fox",
    "deer",
    "turkey",
    "rabbit",
    "coyote",
    "deer",
    "squirrel",
    "fox",
    "rabbit",
    "owl",
    "deer",
    "hawk",
    "rabbit",
    "fox",
    "deer",
]

# Step 2: Creating a sorted version of traimCamlist
sorted_trailCamList = sorted(trailCamList)
print("Step 2: sorted trailCamList: ")
print(sorted_trailCamList)

# Step 3: Count squirrl and fox sightings.
# The sorted list groups the same animals together, making it easier to count.
print("\nStep 3:")
print("Squirrel sightings: 11")
print("Fox sightings: 21")

# Step 4.1: Append GroundHog to the end of the list
trailCamList.append("GroundHog")

# Step 4.2 insert crane as the 30th entry
# Since list indexes in python start at 0, the 30th place is index 29.
trailCamList.insert(29, "Crane")

# Step 4.3 Make skunk the first animal on the list
trailCamList.insert(0, "Skunk")

# Step 4.4 remove 1 turkey from the list
trailCamList.remove("turkey")

print("\nStep 4.4:")
sorted_trailCamList = sorted(trailCamList)

print("\nTurkeys left on the list: 7")
print(sorted_trailCamList)

# Step 4.5: Print a slice of the last 7 entries
print("\nStep 4.5: Last 7 entries:")
print(trailCamList[-7:])

# Step 4.6 Print 10th, 20th, 30th, and 40th entries
print("\nStep 4.6:")
print(f"The 10th animal observed was a {trailCamList[9]}\n")
print(f"The 10th animal observed was a {trailCamList[19]}\n")
print(f"The 10th animal observed was a {trailCamList[29]}\n")
print(f"The 10th animal observed was a {trailCamList[39]}\n")

# Step 4.8 Remove and replace the two misspelled animals
# "racoon" should be "raccoon"
# "cojote" should be "coyote"
trailCamList.remove("racoon")
trailCamList.append("raccoon")

trailCamList.remove("cojote")
trailCamList.append("coyote")

print("\nStep 4.8: List after correcting misspelled animals:")
print(trailCamList)


# Chapter 4 Activities: Working with lists

# Step 5.1: Use a for loop to print each entry in the observations list.
observations = [
    "deer",
    "rabbit",
    "fox",
    "deer",
    "bear",
    "coyote",
    "rabbit",
    "deer",
    "hawk",
    "fox",
]

print("\nStep 5.1: Printing each observation")

for observed in observations:
    print(observed)

print("\nStep 5.2: Printing observerd[-3:] for each animal")
for observed in observations:
    print(observed[-3:])

# Step 5.4 Print every other animal in the observation list
for number in range(0, len(observations), 2):
    print(observations[number])

# Step 5.6 Print every 5th animal
print("\nStep 5.6: Printing every 5th animal in trailCamList")
for animal in range(0, len(trailCamList), 5):
    print(trailCamList[animal])

# Step 6.2: Make a list for the price of each of the 25 cows
cows = [0.01]

for cow in range(1, 25):
    cows.append(cows[-1] * 2)

# step 6.3: Print the price of the 25th cow.
print("\nStep 6.3: Price of the 25th cow")
print(f"The 25th cow costs {cows[-1]}")

# Step 6.4: Print cows 1 through 25 with the assocatied price
print("n\Step 6.4: Cow prices")

for cow in range(0, 25):
    print(f"Cow number {cow + 1} ${cows[cow]:}")


# Task 3: Hands-On Working with a List of Tuples
