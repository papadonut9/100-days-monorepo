# Hangman

### Python implementation for the Hangman game

### Changelog:

`v1.2.7 - Stable`

- UX improvements
- Compartmentalized code a bit
- Fixed the glitch where if a player entered a character which is already guessed, the player will get a prompt which
  notifies the user instead of straightaway deducting a life.

`v1.1.6 - Stable`

- Removed clutter and cleaned up the code a little.

`v1.1.5 - Stable`

- Added Lives system. Every player will get 7 lives at beginning.
- Pending Code refactoring. Will do that in a future patch.

`v0.1.4 - Beta`

- Fixed the input glitch

`v0.1.3 - Beta`

- Updated input system.
- The input system has a known glitch in which the user enters the correct character again, then the characters
  remaining also decreases.
- Removed disabled code.
- Minor refactors to make the code more legible.
- Even though this is a beta version, there is no lives system implemented as of now. Will be doing that in a future
  update.

`v0.0.2 - Alpha`

- Replaced the system where whole word was accepted instead of individual alphabets
- Disabled the lives system till the user input system is improved.
- In this version, the player can only enter a single alphabet since there was a bug which considered every alphabet to
  be incorrect.

`v0.0.1 - Alpha`

- Added custom wordlist. You can make one yourself by uncommenting line 38-44 in `logic.py`.
- Added limit by set number of chances.
- Cosmetic looks added in `main.py`.
- Recognising full words instead of individual letters due to it's work in progress nature. 