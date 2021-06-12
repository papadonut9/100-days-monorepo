import random

lettersList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
               'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numList = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

symList = ['!', '@', '#', '$', '%', '^', '&', '*',
           '(', ')', '-', '_', '=', '+', '[', '{', ']', '}', '|',  ';', ':', '\'', '"', ',', '<', '.', '>', '/', '?', '`', '~']


# length = int(input('Enter the password length: ')) # Useless at this version
charLength = int(
    input('Enter how many characters you want in your password: '))
numLength = int(input('Enter how many numbers you want in your password: '))
symLength = int(input('Enter how many characters you want in your password: '))

password = ''
generatedString = []

for character in range(0, charLength):
    generatedString.append(random.choice(lettersList))

for number in range(0, numLength):
    generatedString.append(random.choice(numList))

for symbol in range(0, symLength):
    generatedString.append(random.choice(symList))


random.shuffle(generatedString)
random.shuffle(generatedString)
for character in generatedString:
    password += character
print(f'Your generated password is: {password}')
