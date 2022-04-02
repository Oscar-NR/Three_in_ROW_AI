
#This function will check if there is a winner
def winnerCheck(board):

    #horizontal up line 
    if( (board[0] == board[1]) and (board[1] == board[2]) and (board[0] =='X' or board[0] == 'O') ):
        return board[0]
    #horizontal middle line
    if( (board[3] == board[4]) and (board[4] == board[5]) and (board[3] =='X' or board[3] == 'O') ):
        return board[3]
    #horizontal bottom line
    if( (board[6] == board[7]) and (board[7] == board[8]) and (board[6] =='X' or board[6] == 'O') ):
        return board[6]


    #vertical left line
    if( (board[0] == board[3]) and (board[3] == board[6]) and (board[0] =='X' or board[0] == 'O') ):
        return board[0]
    #vertical middle line
    if( (board[1] == board[4]) and (board[4] == board[7]) and (board[1] =='X' or board[1] == 'O') ):
        return board[2]
    #vertical right line
    if( (board[2] == board[5]) and (board[5] == board[8]) and (board[2] =='X' or board[2] == 'O') ):
        return board[3]


    #principal diagonal\
    if( (board[0] == board[4]) and (board[0] == board[8]) and (board[0] =='X' or board[0] == 'O') ):
        return board[0]
    #secundary diagonal/
    if( (board[2] == board[4]) and (board[4] == board[6]) and (board[0] =='X' or board[0] == 'O') ):
        return board[0]

    return 'N'
