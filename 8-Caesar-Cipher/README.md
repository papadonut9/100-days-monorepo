# Caesar's Cipher

### Python implementation for the Caesar's cipher where the user enters a string of text without spaces and gets the encrypted text by substitution a letter with other letter. To learn more about Caesar's cipher, check Caesar Cipher [wiki](https://en.wikipedia.org/wiki/Caesar_cipher).

### Changelog:

`v1.1.4 - Stable`

- Improved UX
- Fixed the glitch where an error occurred when anything other than a-z was inserted.
- Fixed the `IndexError` issue that occurred when a very large number was used as the rotation factor.
- Added support for restarting the program by accepting user input.

`v0.1.3 - Beta`

- Added decrypt functionality.
- Now user can choose between encrypting and decrypting their messages.
- Optimised `logic.py` which had redundant code. The `encrypt()` and `decrypt()` functions are still in the source but
  are not used.

`v0.0.2 - Alpha`

- Improved encrypt functionality.
- Fixed `IndexError` glitch which occurred when the string contained the alphabet z or when the rotation went beyond z.

`v0.0.1 - Alpha`

- Added encrypt functionality. (Did not link it to `main.py` )
