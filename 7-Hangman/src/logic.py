import random

wordList = ['laser', 'castaway', 'brunette', 'aftermath', 'czar', 'inquisition', 'reimbursement', 'haberdashery', 'scalawag', 'sophomore',
            'siesta', 'stowaway', 'ornithologist', 'cutlass', 'wasabi', 'mortified', 'jazz', 'smidgen', 'confidant', 'hearse',
            'occupant', 'quarantine', 'quiver', 'atlantis', 'exponential', 'lichen', 'cranium', 'qubit', 'stagecoach', 'sapphire',
            'doppelganger', 'hypothermia', 'doubloon', 'gallop', 'nutmeg', 'periwinkle', 'gondola', 'snobbish', 'dimple', 'westworld',
            'danerys', 'dolores', 'agenda', 'sophie', 'radiation', 'disorganized', 'zephyr', 'procrastinate', 'novelist', 'vandalize',
            'understand', 'download', 'continuum', 'enunciate', 'beckon', 'hamper', 'ruthless', 'accrete', 'hinder', 'dwell',
            'mountain', 'exacerbate', 'peril', 'propulsion', 'mushroom', 'trickle', 'incessant', 'insect', 'incest', 'genocide']
customWordlist = []
wordLisT = ['incense', 'star', 'peril', 'dwell']

chosenWord = random.choice(wordLisT)
print(chosenWord)                       # Disable this in v0.1
userWord = input('Enter your choice: ')
userWord = userWord.lower()

chances = 7
isRight = False

while chances != 0:
    if userWord == chosenWord:
        print('Correct!')
        isRight = True
        chances = 0
    else:
        chances -= 1
        print(f'INcorrect answer. Chances remaining: {chances}')
        userWord = input('Enter your choice: ')
        userWord = userWord.lower()


if isRight == True:
    print('You won!')
else:
    print('You lost! ')

""" # Use this to generate your own wordlist to replace mine

wordLimit = 69
for word in range(0, wordLimit):
    customWordlist.append(input(f'{word}: '))

print(customWordlist) """
