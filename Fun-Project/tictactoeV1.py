#!/usr/bin/python3.5

#Fun Project -Author: Hari.R, hari1892@gmail.com
#CLi based Simple TicTicToe Game


board = {'top-left':'',
     'top-mid':'',
     'top-right':'',
         'mid-left':'',
     'mid-mid':'',
         'mid-right':'',
         'low-left':'',
         'low-mid':'',
         'low-right':''}


def dis():
 
    print(board['top-left'] + '|' + board['top-mid'] + '|' + board['top-right'])
    print('-----')
    print(board['mid-left'] + '|' + board['mid-mid'] + '|' + board['mid-right'])
    print('-----')
    print(board['low-left'] + '|' + board['low-mid'] + '|' + board['low-right'])
    print('-----')
    vi = ['x','o']
    if board['top-left'] == board['top-mid'] == board['top-right'] in vi: 
        print("winner is" + ' ' +  board['top-left'])
        exit()
    elif board['mid-left'] == board['mid-mid'] == board['mid-right'] in vi:
        print("winner is" + ' ' +  board['mid-left'])
        exit()
    elif board['low-left'] == board['low-mid'] == board['low-right'] in vi:
        print("winner is" + ' ' + board['low-left'])
        exit()
    elif board['top-left'] == board['mid-left'] == board['low-left'] in vi:
        print("winner is" + ' ' + board['top-left'])
        exit()
    elif board['top-mid'] == board['mid-mid'] == board['low-mid'] in vi:
        print("winner is" + ' ' + board['top-mid'])
        exit()
    elif board['top-right'] == board['mid-right'] == board['low-right'] in vi:
        print("winner is" + ' ' + board['top-right'])
        exit()
    elif board['top-left'] == board['mid-mid'] == board['low-right'] in vi:
        print("winner is" + ' ' + board['top-left'])
        exit()
    else:
        if board['top-right'] == board['mid-left'] == board['low-left'] in vi:
            print("winner is" + ' ' + board['low-left'])
            exit()




    
    
   
        
 #       board[mid-left] == board[mid-mid] == board[mid-right] or board[low-left] == board[low-mid] == board[low-right] 
    if '' not in list(board.values()):
        win()



def win():
    print("Game over, Game is Draw")
    exit()

def ins():
    player = input(str("choose player:(x or o)"))
    validinputs = ['x','o']
    if player not in validinputs:
        print("you have entered invalid input, please enter x or o:")
        ins()
    return player

def xinputs(player):
    validinputlists = list(board.keys())
    print( "below are the options\n" +  str(validinputlists))
    xinput = input(str("enter position" + ' ' +  player + ' ' +  'turn:')) 
    if xinput not in validinputlists:
        print("Invalid input,please try again with correct input")
        xinputs(player)
    if board[xinput] == '':
        board[xinput] = player
        dis()
        if player == 'x':
            player = 'o'
            s = xinputs(player)
            xinputs(s)
        elif player == 'o':
            player = 'x'
            s = xinputs(player)
            xinputs(s)
        else:
            print("invalid")
            xinputs(player)
    else:
        print("place already taken, Please enter again in diffrent position")
        xinputs(player) 



player = ins()
if player not in ['x','o']:
    player = ins()



while True:
    xinputs(player)
