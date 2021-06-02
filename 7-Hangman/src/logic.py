import random

wordList = ['laser', 'castaway', 'brunette', 'aftermath', 'czar', 'inquisition', 'reimbursement', 'haberdashery', 'scalawag', 'sophomore',
            'siesta', 'stowaway', 'ornithologist', 'cutlass', 'wasabi', 'mortified', 'jazz', 'smidgen', 'confidant', 'hearse',
            'occupant', 'quarantine', 'quiver', 'atlantis', 'exponential', 'lichen', 'cranium', 'qubit', 'stagecoach', 'sapphire',
            'doppelganger', 'hypothermia', 'doubloon', 'gallop', 'nutmeg', 'periwinkle', 'gondola', 'snobbish', 'dimple', 'westworld',
            'danerys', 'dolores', 'agenda', 'sophie', 'radiation', 'disorganized', 'zephyr', 'procrastinate', 'novelist', 'vandalize',
            'understand', 'download', 'continuum', 'enunciate', 'beckon', 'hamper', 'ruthless', 'accrete', 'hinder', 'dwell',
            'mountain', 'exacerbate', 'peril', 'propulsion', 'mushroom', 'trickle', 'incessant', 'insect', 'incest', 'genocide']
wordLisT = ['incense', 'star', 'peril', 'dwell']

chosenWord = random.choice(wordLisT)
print(chosenWord)
wordLength = len(chosenWord)
print(wordLength)
display = []

for _ in range(0, wordLength):
    display.append('_')
print(display)

isFinished = False

while not isFinished:
    userChar = input('Enter your choice: ').lower()

    for position in range(wordLength):
        if userChar == chosenWord[position]:
            display[position] = userChar

    print(display)
    if '_' not in display:
        isFinished = True
        print('You WIN')


