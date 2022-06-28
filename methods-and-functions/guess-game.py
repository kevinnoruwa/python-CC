from random import shuffle 
# This fucntion is used to shuffle the list
def shuffle_list(mylist):
  shuffle(mylist)
  return mylist
# this function takes in the users guess
def player_guess():
  guess = ''
  while guess  not in ['0', '1', '2']:
        guess = input("enter a number between 0, 1, or 2 \n ")
        return int(guess)
  

# This function is to check if the users guess is correct
def check(mylist, guess):
      if mylist[guess] == 'O':
            print("you found the ball!")
      else:
            print("You did not pick the correct place")
            print( f"this was the correct place {myList}")
            
          
myList = ['', 'O', '']
# mixed list
mixed_list = shuffle_list(myList)
# the guess that the user submitted
guess = player_guess()
check(mixed_list,guess)
  
