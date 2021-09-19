

string = 'hereYaGo'
new_str = ''

for letter in string:
    if letter == letter.upper():
        new_str += ' '
    new_str += letter


print(new_str)
