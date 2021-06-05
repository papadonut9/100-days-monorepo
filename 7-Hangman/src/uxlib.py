import game


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


def gameOver(won=True, answer=''):
    """
        Displays a game over status which varies according to the game outcome

        :parameter
            won(bool): pass the game outcome as won or lost. The default value is True
            answer: pass the chosen word from wordlist. It will be shown if the player loses the game.
    """
    if won is True:
        print('You Won!')
        print('GAME OVER')
    else:
        print(f'You lost! The correct answer was {answer}')
        print('GAME OVER')


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
