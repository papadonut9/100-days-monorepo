# Password Generator
### Features
- Users have complete control over how many characters, numbers and symbols they want in their passwords.
- Users can also directly select how many characters they want in their passwords. (planned)
- Tired of figuring whether the character is O or 0, I or l? An option to generate more easily readable passwords while omitting ambiguous characters. (planned)
- Since the randomness of this password generator is fully based upon the `random` library, it is open-source and secure. 
### Changelog:

 `v0.1.2` 
 - Removed the sleep method from the fake entropy generation due to some annoyance
 - Disabled the length function because a new method is under development that further adds one more way to generate secure passwords. 
 - Also shuffled the string twice to increase randomness.

 `v0.1.1` 
 - added basic functionality
 - Users can fine control over how many letters, numbers and characters they want in their password string
 