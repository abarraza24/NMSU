import random, math, datetime, calendar, os

courses = ['History', 'Math', 'Physics', 'CompSci']
#math
rads = math.radians(90)
print(math.sin(rads))
#Random
random_course = random.choice(courses)
print(random_course)
# datetime
today = datetime.date.today()
print(today)
# calander
print(calendar.isleap(2020))
# os
print(os.getcwd())
