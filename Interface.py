
#This file is the interface, responsible of comunication between the player and the rest of code


#This represent the board game
positions = ['1','2','3','4','5','6','7','8','9']
winner = 'N'
turn = 'X';
validMove = False

import gameThree
from AIThree import AI

print('Welcome to three in row game')
print('X moves first:')
print('1- X team')
print('2- O team')

while validMove == False:
    move = int (input('Your team: ') )   
    try:
        if(move == 1 or move == 2):
            validMove = True
            if (move == 1):
                computer = AI('O')
            else:
                computer = AI('X')                     
        else:
            move = input('Please introduce 1 for X or 2 for O')          
    except:
        move =  input('Introduce 1 for X team or 2 for O team')      

#Show the Initial state of the board game
print('   ', positions[0], positions[1], positions[2])
print('   ', positions[3], positions[4], positions[5])
print('   ', positions[6], positions[7], positions[8])


while(winner =='N'):  
    #Reset the flag validMove
    validMove = False
    
    while validMove == False:
        move = int(input('Next move:') )   
        try:   
            if(positions[move-1] =='X' or positions[move-1] == 'O' or move > 9 or move < 1 ):
                print('Invalid position, please enter a valid one: ')     
            else:
                validMove = True
        except:
            print('Invalid position, please enter a valid one: ')    

    #Writing the valid position
    positions[move-1]= turn
    #Show the new state of the board game
    print('   ', positions[0], positions[1], positions[2])
    print('   ', positions[3], positions[4], positions[5])
    print('   ', positions[6], positions[7], positions[8])

    winner = gameThree.winnerCheck(positions)

    #after a valid move change the team turn
    if (turn == 'X'):
        turn ='O'
    else:
        turn = 'X'      
        
print('The winner was: ', winner)   

    
