import random
import math
from datetime import datetime
#Function Guess 1
def message():
    msg = "It's time to learn Python"
    return msg
print(f"msg")

#Function Guess 2
def calc_divide_mod(num1,num2):
    a = num1//num2
    b = num1%num2
    return a,b
n,r = calc_divide_mod(13,4)
print( f"13 divide by 4 is {n} with the remainder of {r}")

#Function guess 3
def roll_die():
    return random.randint(1, 6)
print("Rolled:", roll_die())

#Function guess 4
def current_year():
    return datetime.now().year
print("Current year:", current_year())

#Function guess 4
def reverse_text(text):
    return text[::-1]
print("Reversed:", reverse_text("Python"))

#Function guess 5
def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
print("Vowels:", count_vowels("Artificial Intelligence"))

#Function guess 6
def random_color():
    colors = ["red", "blue", "green", "yellow", "purple"]
    return random.choice(colors)
print("Random color:", random_color())

#Function guess 7
def hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)
print("Hypotenuse:", hypotenuse(3, 4))

#Function guess 8
def generate_password(length):
    chars = "abcdefghijklmnopqrstuvwxyz0123456789"
    return ''.join(random.choice(chars) for _ in range(length))
print("Password:", generate_password(8))