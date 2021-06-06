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

mode = input('Enter encrypt/decrypt to continue: ').lower()

userText = input(f'Enter the text you want to {mode}: ')
rot = int(input('Shift by how many letters?: '))

if mode == 'encrypt':
    print(logic.caesar(mode=mode, data=userText, shift=rot))
elif mode == 'decrypt':
    print(logic.caesar(mode=mode, data=userText, shift=rot))
else:
    print("INVALID INPUT")
