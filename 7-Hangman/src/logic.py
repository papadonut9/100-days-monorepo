import random
import wordlist
import uxlib
import game

lives = 7
display = []

chosenWord = random.choice(wordlist.ready)
wordLength = len(chosenWord)

uxlib.start(0)

for _ in range(0, wordLength):  # Displays the initial dashes
    display.append('_')
print(display)

while not game.isFinished:
    userChar = input('Enter your choice: ').lower()

    if userChar in display:  # Prevents user from re-guessing the same character.
        print('You\'ve already guessed it')

    for position in range(wordLength):  # Answer checker
        if userChar == chosenWord[position]:
            display[position] = userChar

    if userChar not in chosenWord:  # Life reducer
        lives -= 1
        print('Sorry! You\'ve made a wrong guess so you lost a life!')
        print(uxlib.phases[lives])

    print(display)

    if '_' not in display:  # Check if user has guessed all letters
        game.isFinished = True
        uxlib.gameOver()

    elif lives == 0:  # If lives went down to zero, the game finishes!
        game.isFinished = True
        uxlib.gameOver(won=False, answer=chosenWord)


