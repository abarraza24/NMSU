from pathlib import Path

path = Path('HW6/pi_digits.txt')
path2 = Path('HW6/programming.txt')
path2.write_text('I love programming.')
contents = path.read_text().rstrip()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
    
print(pi_string)
print(len(pi_string))
