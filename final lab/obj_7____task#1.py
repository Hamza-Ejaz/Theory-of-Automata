
import re

user_input = input('enter email to validate: ')

p1 = re.match(r"([a-zA-Z]+[.-_])*[A-Za-z0-9]+@[a-zA-Z-]+(\.[com|edu|co|uk|tk|pk])+",user_input)

if p1:
    print('Email ID is valid...')
else:
    print('invalid ID!!!')
