import logic
import auction_db
import ui
moreParticipants = True
db = auction_db.bids

ui.splash()
while moreParticipants:
    name = input('Enter your name: ')
    bid = round(float(input('Enter your bid: ')), 2)
    logic.auctionInput(db, name, bid)
    stillContinue = input('Are there any other members? Type yes/no: ').lower()

    if stillContinue == 'no':
        moreParticipants = False
    elif stillContinue == 'yes':
        logic.clrscr()
        moreParticipants = True
        ui.splash()
    else:
        print('invalid input')
        logic.clrscr()
        ui.splash()

print(logic.declareWinner(db))
