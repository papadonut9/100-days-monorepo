import logic

print("""
  ____   _  _               _                 
 / ___| (_)| |  ___  _ __  | |_               
 \___ \ | || | / _ \| '_ \ | __|              
  ___) || || ||  __/| | | || |_               
 |____/ |_||_| \___||_| |_| \__|              
       _                 _    _               
      / \   _   _   ___ | |_ (_)  ___   _ __  
     / _ \ | | | | / __|| __|| | / _ \ | '_ \ 
    / ___ \| |_| || (__ | |_ | || (_) || | | |
   /_/   \_\\\\__,_| \___| \__||_| \___/ |_| |_|
                                              
""")

moreParticipants = True

while moreParticipants:
    name = input('Enter your name: ')
    bid = float(input('Enter your bid: '))
    stillContinue = input('Are there any other members? Type yes/no').lower()

    if stillContinue == 'no':
        moreParticipants = False
    elif stillContinue == 'yes':
        moreParticipants = True
    else:
        print('invalid input')
