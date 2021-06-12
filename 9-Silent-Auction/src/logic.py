import os


# noinspection SpellCheckingInspection
def clrscr():
    if os.name == 'posix':
        os.system('clear')
    elif os.name == 'nt':
        os.system('cls')


# noinspection SpellCheckingInspection
def auctionInput(bid_db, name='', bidval=0.00, ):
    application = {
        'name': name,
        'bid': bidval
    }
    bid_db.append(application)


# noinspection SpellCheckingInspection
def declareWinner(bid_db):
    maxV = 0.00
    winner = ''
    for bid in bid_db:
        if bid['bid'] > maxV:
            maxV = bid['bid']
            winner = bid['name']
    return f'The winner of the Auction is {winner} with a winning bid of {maxV}'


# Testing
# import auction_db
#
# bids = auction_db.bids
# print(declareWinner(bids))
# clrscr()
