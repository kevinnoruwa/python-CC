import random
from types import new_class

values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[self.rank]
        
    def __str__(self):
        
       return self.rank + " of " + self.suit
    
    



class Deck():  
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # create card objects 
                created_card =  Card(suit,rank)
                self.all_cards.append(created_card)
                
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()
    




class Player:
    def __init__(self, name):
        self.name = name
        self.all_cards = []
    def remove_one(self):
        return self.all_cards.pop(0)
    def add_cards(self,new_cards):
        self.new_cards = new_cards
        if type(new_cards) == type([]):
            # for a list of cards
            self.all_cards.extend(new_cards)
        else:
            # for a single card obj
            self.all_cards.append(new_cards)
    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'
    
    
    

# Game setup

player_one = Player("One")

player_two = Player("Two")


new_deck = Deck()

new_deck.shuffle()



for x in range(0,26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

round_num = 0
game_on = True

while game_on == True:
    round_num += 1
    print(f"Round: {round_num}")
    
    if (len(player_one.all_cards) == 0):
        print("player one, out of cards! player Two Wins!")
        game_on = False
        break
    if( len(player_two.all_cards) == 0):
        print("player two, out of cards! player one Wins!")
        game_on = False
        break
    
    # Start new round
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    
    # while at war
    
    
    
    at_war = True
    
    while at_war == True:
        if(player_one_cards[-1].value > player_two_cards[-1].value):
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards) 
            at_war = False
            
        elif(player_one_cards[-1].value < player_two_cards[-1].value):
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards) 
            at_war = False
            
        else:
            print("WAR!")
            if (len(player_one.all_cards) < 5):
                print("player one unable to declare war")
                print("Player Two wins!")
                game_on = False
                break
            elif(len(player_two.all_cards) < 5):
                print("player Two unable to declare war")
                print("player one Wins!")
                game_on = False
                break
            else:
                for num in range(0,3):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_one.remove_one())
            
            
    
    
    
    