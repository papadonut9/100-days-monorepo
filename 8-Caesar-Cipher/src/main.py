import logic

print("""

   _____                           
  / ____|                          
 | |     __ _  ___  ___  __ _ _ __ 
 | |    / _` |/ _ \/ __|/ _` | '__|
 | |___| (_| |  __/\__ \ (_| | |   
  \_____\__,_|\___||___/\__,_|_|   
  
  / ____(_)     | |                
 | |     _ _ __ | |__   ___ _ __   
 | |    | | '_ \| '_ \ / _ \ '__|  
 | |____| | |_) | | | |  __/ |     
  \_____|_| .__/|_| |_|\___|_|     
          | |                      
          |_|                    

""")
shouldContinue = True
while shouldContinue:
    mode = input('Enter encrypt/decrypt to continue: ').lower()

    if mode == 'encrypt' or mode == 'decrypt':
        userText = input(f'Enter the text you want to {mode}: ')
        rot = int(input('Shift by how many letters?: '))
        print(logic.caesar(mode=mode, data=userText, shift=rot))
    else:
        print("INVALID INPUT")

    wantContinue = input('Do you want to continue? Enter yes/no: ').lower()
    if wantContinue == 'no' or wantContinue == 'n':
        shouldContinue = False
        print('Exiting...')
    elif wantContinue == 'yes' or 'y':
        print('Restarting..')
    else:
        print('Invalid input! Please try again')
