import random
import wordlist

class ux:
    def start(lines):
        print(""" 
    __  __                                                        
   / / / /  ____ _   ____     ____ _   ____ ___     ____ _   ____ 
  / /_/ /  / __ `/  / __ \   / __ `/  / __ `__ \   / __ `/  / __ \\
 / __  /  / /_/ /  / / / /  / /_/ /  / / / / / /  / /_/ /  / / / /
/_/ /_/   \__,_/  /_/ /_/   \__, /  /_/ /_/ /_/   \__,_/  /_/ /_/ 
                           /____/                                 
""")
        for _ in range(0, lines):
            print('')


    phases = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
========='''
          ]





class game():
    isFinished = False
    livesDepleted = False


lives = 7

chosenWord = random.choice(wordlist.test)
print(chosenWord)
wordLength = len(chosenWord)
print(wordLength)
display = []

ux.start(2)

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
        print(ux.phases[lives])

    print(display)

    if '_' not in display:
        game.isFinished = True
        print('You WIN')

    elif lives == 0:
        game.isFinished = True
        print('You lose')
