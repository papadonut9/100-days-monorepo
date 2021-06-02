import random
import wordlist
import uxlib
import game

lives = 7

chosenWord = random.choice(wordlist.ready)
print(chosenWord)
wordLength = len(chosenWord)
print(wordLength)
display = []

uxlib.start(2)

for _ in range(0, wordLength):
    display.append('_')
print(display)

while not game.isFinished:
    userChar = input('Enter your choice: ').lower()

    for position in range(wordLength):
        if userChar == chosenWord[position]:
            display[position] = userChar

    if userChar not in chosenWord:
        lives -= 1
        print(uxlib.phases[lives])

    print(display)

    if '_' not in display:
        game.isFinished = True
        print('You WIN')

    elif lives == 0:
        game.isFinished = True
        print('You lose')
