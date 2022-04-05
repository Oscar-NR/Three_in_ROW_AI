
#Class which containt the AI

#The behaviur as 'X' (first move), consist in obtain three corners, this will lead to a checkmate 
#The behaviur as 'O' (second move), consist identify if the player is trying obtain three corners and if so do a 456 line or 258 line the only option to avoid that tricky move
#Also the IA will check if there is a possibility to win or lose and will use that move at first option.

import random


class AI:

    #The positions of the corners just to made simple select one random corner
    corners = [1, 3, 7, 9]

    myTeam = 'N'
    otherTeam = 'N'
    # X always moves first, so we can know how many movements were done
    movesOfX = 0

    def __init__(self, team):

        self.moveOfX = 0
        if(team == 'X'):
            self.myTeam = 'X'
            self.otherTeam = 'O'        
        else:
            self.myTeam = 'O'
            self.otherTeam= 'X'




 
    #this function will return the next move of the AI
    def nextMove(self, board):

        #The Ai will behave in different way if the AI is the X player or the O player
        if(self.myTeam == 'X'): 
            if(self.movesOfX == 0):
                #Return a random corner
                randomPos = random.randint(0,3)
                return self.corners[randomPos]

            #At least 2 corners will be free
            if(self.movesOfX == 1):
                randomPos = random.randint(0,3)
                while(board[(self.corners[randomPos]-1)] != self.corners[randomPos]):
                    randomPos = random.randint(0,3)

                return self.corners[randomPos]

            if(self.movesOfX == 2):
                #Here we look for a winner move or avoid or avoid lose
                temp = self.takeALook(board);
                if(temp != 'N'):
                    return temp
                else:
                    randomPos = random.randint(0,3)
                    while(board[(self.corners[randomPos]-1)] != self.corners[randomPos]):
                        randomPos = random.randint(0,3)
                        
                    return self.corners[randomPos]

            #reach this point means that number of moves is >2
            #First the AI will look at the map an identify the critical positions
            temp = self.takeALook(board);
            if(temp != 'N'):
                return temp
            else:
                return self.randomPos(board)
        
        else:
            #The AI team is O
            if(self.moveOfX == 1):
                if(board[4] != 'X'):
                    return 5
                else:
                    return self.randomPos(board)
            
            if(self.moveOfX == 2):
                temp = self.takeALook(board);
                if(temp != 'N'):
                    return temp
                else:
                    #To avoid the tricky move
                    if(board[4] == "O"):
                        temp =  random.randint(0,8)
                        while( ((temp+1)%2 == 0) and (temp != 0) ):
                            temp =  random.randint(0,8)
                        return temp
                    return self.randomPos(board)

        
    #This function will check if there is a winner move, and also if there is a move to avoid lose but, first will try to win
    def takeALook(self, board):        

        lookValue = 0;
        avoidlose = 0;

        #Here is a lot of check for all the possibilites moves to win, each possibility will start with capitals letters to be able to see better where start each "block"
        
        #______HORIZONTAL_UP_LINE______

        if(board[0] == self.myTeam):
            lookValue += 1

        if(board[1] == self.myTeam):
            lookValue += 1

        if(board[2] == self.myTeam):
            lookValue += 1

        if(board[0] == self.otherTeam):
            lookValue -= 1

        if(board[1] == self.otherTeam):
            lookValue -= 1

        if(board[2] == self.otherTeam):
            lookValue -= 1

        #this means that we can win, so check in which position is the winner move
        if(lookValue == 2):
            if(board[0] == '1'):
                return 1
            if(board[1] == '2'):
                return 2
            if(board[2] == '3'):
                return 3   
            
        #this means we can lose, so check in which position is the move to avoid lose move
        if(lookValue == -2):
            if(board[0] == '1'):
                avoidlose = 1
            if(board[1] == '2'):
                avoidlose = 2
            if(board[2] == '3'):
                avoidlose = 3



        #______HORIZONTAL_MIDDLE_LINE______

        if(board[3] == self.myTeam):
            lookValue += 1

        if(board[4] == self.myTeam):
            lookValue += 1

        if(board[5] == self.myTeam):
            lookValue += 1

        if(board[0] == self.otherTeam):
            lookValue -= 1

        if(board[1] == self.otherTeam):
            lookValue -= 1

        if(board[2] == self.otherTeam):
            lookValue -= 1

        #this means that we can win
        if(lookValue == 2):
            if(board[3] == '4'):
                return 4
            if(board[4] == '5'):
                return 5
            if(board[5] == '6'):
                return 6   
            
        #this means we can lose
        if(lookValue == -2):
            if(board[3] == '4'):
                avoidlose = 4
            if(board[4] == '5'):
                avoidlose = 5
            if(board[5] == '6'):
                avoidlose = 6



        #______HORIZONTAL_BOTTOM_LINE______

        if(board[6] == self.myTeam):
            lookValue += 1

        if(board[7] == self.myTeam):
            lookValue += 1

        if(board[8] == self.myTeam):
            lookValue += 1

        if(board[6] == self.otherTeam):
            lookValue -= 1

        if(board[7] == self.otherTeam):
            lookValue -= 1

        if(board[8] == self.otherTeam):
            lookValue -= 1

        #this means that we can win
        if(lookValue == 2):
            if(board[6] == '7'):
                return 7
            if(board[7] == '8'):
                return 8
            if(board[8] == '9'):
                return 9   
            
        #this means we can lose
        if(lookValue == -2):
            if(board[6] == '7'):
                avoidlose = 8
            if(board[7] == '8'):
                avoidlose = 8
            if(board[8] == '9'):
                avoidlose = 9


        #______VERTICAL_LEFT_LINE______

        if(board[0] == self.myTeam):
            lookValue += 1

        if(board[3] == self.myTeam):
            lookValue += 1

        if(board[6] == self.myTeam):
            lookValue += 1

        if(board[0] == self.otherTeam):
            lookValue -= 1

        if(board[3] == self.otherTeam):
            lookValue -= 1

        if(board[6] == self.otherTeam):
            lookValue -= 1

        #this means that we can win
        if(lookValue == 2):
            if(board[0] == '1'):
                return 1
            if(board[3] == '4'):
                return 4
            if(board[6] == '7'):
                return 7  
            
        #this means we can lose
        if(lookValue == -2):
            if(board[0] == '1'):
                avoidlose = 1
            if(board[3] == '4'):
                avoidlose = 4
            if(board[6] == '7'):
                avoidlose = 7
        


        #______VERTICAL_MIDDLE_LINE______

        if(board[1] == self.myTeam):
            lookValue += 1

        if(board[4] == self.myTeam):
            lookValue += 1

        if(board[7] == self.myTeam):
            lookValue += 1

        if(board[1] == self.otherTeam):
            lookValue -= 1

        if(board[4] == self.otherTeam):
            lookValue -= 1

        if(board[7] == self.otherTeam):
            lookValue -= 1

        #this means that we can win
        if(lookValue == 2):
            if(board[1] == '2'):
                return 2
            if(board[4] == '5'):
                return 5
            if(board[7] == '8'):
                return 8  
            
        #this means we can lose
        if(lookValue == -2):
            if(board[1] == '2'):
                avoidlose = 2
            if(board[4] == '5'):
                avoidlose = 8
            if(board[7] == '8'):
                avoidlose = 8



        #______VERTICAL_RIGHT_LEFT_LINE______

        if(board[2] == self.myTeam):
            lookValue += 1

        if(board[5] == self.myTeam):
            lookValue += 1

        if(board[8] == self.myTeam):
            lookValue += 1

        if(board[2] == self.otherTeam):
            lookValue -= 1

        if(board[5] == self.otherTeam):
            lookValue -= 1

        if(board[8] == self.otherTeam):
            lookValue -= 1

        #this means that we can win
        if(lookValue == 2):
            if(board[2] == '3'):
                return 3
            if(board[5] == '5'):
                return 5
            if(board[8] == '9'):
                return 9  
            
        #this means we can lose
        if(lookValue == -2):
            if(board[2] == '3'):
                avoidlose = 3
            if(board[5] == '6'):
                avoidlose = 6
            if(board[8] == '9'):
                avoidlose = 9



        #______MAIN_DIAGONAL_LINE______
        if(board[0] == self.myTeam):
            lookValue += 1

        if(board[4] == self.myTeam):
            lookValue += 1

        if(board[8] == self.myTeam):
            lookValue += 1

        if(board[0] == self.otherTeam):
            lookValue -= 1

        if(board[4] == self.otherTeam):
            lookValue -= 1

        if(board[8] == self.otherTeam):
            lookValue -= 1

        #this means that we can win
        if(lookValue == 2):
            if(board[0] == '1'):
                return 1
            if(board[4] == '5'):
                return 5
            if(board[8] == '9'):
                return 9  
            
        #this means we can lose
        if(lookValue == -2):
            if(board[0] == '1'):
                avoidlose = 1
            if(board[4] == '5'):
                avoidlose = 6
            if(board[8] == '9'):
                avoidlose = 9



        #______SECONDARY_DIAGONAL_LINE______
        if(board[2] == self.myTeam):
            lookValue += 1

        if(board[4] == self.myTeam):
            lookValue += 1

        if(board[6] == self.myTeam):
            lookValue += 1

        if(board[2] == self.otherTeam):
            lookValue -= 1

        if(board[4] == self.otherTeam):
            lookValue -= 1

        if(board[6] == self.otherTeam):
            lookValue -= 1

        #this means that we can win
        if(lookValue == 2):
            if(board[2] == '3'):
                return 3
            if(board[4] == '5'):
                return 5
            if(board[6] == '7'):
                return 7  
            
        #this means we can lose
        if(lookValue == -2):
            if(board[2] == '3'):
                avoidlose = 3
            if(board[4] == '5'):
                avoidlose = 5
            if(board[8] == '9'):
                avoidlose = 7


        if(avoidlose!='N'):
            return avoidlose
        else:
            return 'N'



    #Function which return a random valid position
    def randomPos(self, board):    
        
        randomPos = random.randint(0,8) 
        while(int(board[random]) != randomPos+1 ):
            randomPos = random.randint(0,8)

        return randomPos


