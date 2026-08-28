"""
    Module: BarrazaAlexis_Lesson 2
    Author: Alexis Barraza
    Date: August 26, 2026
    Course: ICT 362 - Software Technology II
    
    Assignment: Lists, Tuples, and For Looping Statements hw2b
    
    Description:
        This program works with a list of tuples. Each tuples stores an animal,
        camera station, and day observed.
"""

# Task 3: Hands-on working with a List of Tuples
trailCamDetail = [
    ("deer", "A", 1),
    ("rabbit", "B", 1),
    ("fox", "C", 2),
    ("hawk", "D", 2),
    ("bear", "A", 3),
    ("coyote", "B", 3),
    ("squirrel", "C", 4),
    ("owl", "D", 4),
    ("turkey", "A", 5),
    ("raccoon", "B", 5),
    ("deer", "C", 6),
    ("rabbit", "D", 6),
    ("fox", "A", 7),
    ("hawk", "B", 7),
    ("bear", "C", 8),
    ("coyote", "D", 8),
    ("squirrel", "A", 9),
    ("owl", "B", 9),
    ("turkey", "C", 10),
    ("raccoon", "D", 10),
    ("deer", "A", 11),
    ("rabbit", "B", 11),
    ("fox", "C", 12),
    ("hawk", "D", 12),
    ("bear", "A", 13),
    ("coyote", "B", 13),
    ("squirrel", "C", 14),
    ("owl", "D", 14),
    ("turkey", "A", 15),
    ("raccoon", "B", 15),
    ("deer", "C", 16),
    ("rabbit", "D", 16),
    ("fox", "A", 17),
    ("hawk", "B", 17),
    ("bear", "C", 18),
    ("coyote", "D", 18),
    ("squirrel", "A", 19),
    ("owl", "B", 19),
    ("turkey", "C", 20),
    ("raccoon", "D", 20),
    ("bobcat", "A", 2),
    ("opossum", "B", 4),
    ("elk", "C", 6),
    ("moose", "D", 8),
    ("beaver", "A", 10),
    ("otter", "B", 12),
    ("lynx", "C", 14),
    ("badger", "D", 16),
    ("porcupine", "A", 18),
    ("weasel", "B", 20),
]

# Step 7.2: Print all trail camera observations
print("Step 7.2: Trail camera observations.")

for observation in trailCamDetail:
    print(f"On day {observation[2]} at Station {observation[1]} a {observation[0]} was spotted")
    

# Step 7.4: Appending three of my favorite animals that are not on the list
trailCamDetail.append(("wolf", "A", "21"))
trailCamDetail.append(("mountian lion", "B", "22"))
trailCamDetail.append(("bison", "C", "23"))

# Step 7.4: Print the last 8 records
print("\nStep 7.4: Last 8 trail camera observations")

for observation in trailCamDetail[-8:]:
    print(f"On day {observation[2]} at Station {observation[1]} a {observation[0]} was spotted")


