import random


def display_board(board):
    print(board[1]+ '|' + board[2] + '|' + board[3])
    
    print(board[4]+ '|' + board[5] + '|' + board[6])
 
    print(board[7]+ '|'+ board[8] + '|'+ board[9])
    
    print('\n'*2)
    


    





def player_input():
    # output = (player1 marker , player 2 marker)
    marker = ' '
    while marker not in ['X','O']:
        marker = input("Please pick marker for player1 'X' or 'O': ").upper()
        
    if(marker == 'X'):
        return ('X', 'O')
    else:
         return ('O', 'X') 
        
    
    
  
  







def place_marker(board, marker, pos):
    
    board[pos] = marker
    
    
    




def win_check(board, mark):
#    checking rows if they have the same mark
   if(board[1] == board[2] == board[3] == mark):
       return True
   if(board[4] == board[5] == board[6] == mark):
     return True
   if(board[7] == board[8] == board[9] == mark):
     return True
 
#  cheking columns if they have the same mark
   if(board[1] == board[4] == board[7] == mark):
       return True
   if(board[2] == board[5] == board[8] == mark):
     return True
   if(board[3] == board[6] == board[9] == mark):
     return True
# check if diagnols have the same mark
   if(board[1] == board[5] == board[9] == mark):
     return True
   if(board[3] == board[5] == board[7] == mark):
     return True
  



 






def choose_first():
    
    result = random.randint(1,2)
    
    if(result == 1):
        return 'player 1'
    else:
        return 'player 2'



    
    
    
def space_check(board, pos):
    return board[pos] == ' '
    
   
    

def full_board(board):
    for i in range(1,10):
        if (space_check(board,i) == True):
            return False
        else:
            return True
   
    

            


def player_choice(board):
       pos = 0
       
       while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board, pos) :
            pos = int(input("pick a position between 1-9: "))      
       return pos
           
          



def replay():
        choice = ' '
        
        while choice not in ['Y', 'N']:
            choice = input("do yo want to play again select 'Y' for yes or 'N' for no: ").upper()
        
        if(choice == 'Y'):
            return True
        else:
         
            return False
        



print('Welcome to tick tack toe')

game_on = True
while game_on:
    
 board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
 player1,player2 = player_input()
 
 
 turn = choose_first()
 
 print(turn + " will go first")
 
 play_game = input('Ready to play? select y or n: ').lower()
 if(play_game == 'y'):
  
   game_on == True
 elif play_game == 'n':
     game_on == False
     break
     
     
 while game_on == True:
     
    if turn == 'player 1':
        # player 1 turn 
        
        # show the board
        display_board(board)
        
        # choose pos
        pos = player_choice(board)
        
        # place the marker on the pos
        place_marker(board,player1,pos)
        
        # check if they won
        
        if win_check(board, player1) == True:
            display_board(board)
            print('PLAYER 1 HAS WON')
            game_on = False
        else:
            if(full_board(board) == 'True'):
                display_board(board)
                print("Tie Game")
                game_on = False
            else:
                turn = 'player 2'
        
        
    else:    
        #  player 2 turn 
        
      
        
        # show the board
        display_board(board)
        
        # choose pos
        pos = player_choice(board)
        
        # place the marker on the pos
        place_marker(board,player2,pos)
        
        # check if they won
        
        if win_check(board, player2) == True:
            display_board(board)
            print('PLAYER 2 HAS WON')
            game_on = False
        else:
            if(full_board(board) == 'True'):
                display_board(board)
                print("Tie Game")
                game_on = False
            else:
                turn = 'player 1'
                
      
         
     
     
     
        
     
 
 

 
 

 
    


 

 
        
        