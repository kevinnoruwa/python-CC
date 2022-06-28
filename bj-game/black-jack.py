from cgi import test
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " of " + self.suit
    
    


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                 self.deck.append(Card(suit, rank))
                 
    def __str__(self):
        deck_comp = ' '
        
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The deck has: " + deck_comp
        
        
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
    
class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
        
    def add_card(self,card):
        self.cards.append(card)
        self.value +=  values[card.rank]
        
        
        if (card.rank == 'Ace'):
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    


class Chips:
    def __intit__(self, totals = 100):
        self.totals = totals
        self.bet = 0
        
    def win_bet(self):
        self.totals += self.bet
    
    def lose_bet(self):
        self.totals -= self.bet
        
        

def take_bet(chips):
    print("THIS!!")
    print(chips.totals)
    while True:
        try:
            chips.bet = int(input("How many chips would like to bet?"))
        except:
            print("Sorry please provide an integer ")
            
        else:
            if(chips.bet > chips.totals):
                print(f"sorry, you do not have enough chips! you have: {chips.total}")
            else:
                break
            
def hit(deck,hand):
    single_card = deck.deal()
    Hand.add_card(single_card)
    Hand.adjust_for_ace()
    


def hit_or_stand(deck, hand):
    global playing
    
    while True :
        
        x = input("Hit or stand? Enter h or s")
        
        if x[0].lower() == 'h':
            hit(deck,hand)
            
        elif(x[0].lower() == 's'):
            print("Player Stands Dealers Turn")
            playing = False
        else:
            print("Sorry, please try again")
            break
        
def show_some(player,dealer): 
    
    print('\n Dealers hand: ')
    print("First card hidden!")
    print(dealer.cards[1])
    
    print("\n players hand: ")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    
    print("\n dealer hand: ")
    for card in dealer.cards:
        print(card)
        
    print(f"value of dealers hand is: {dealer.value}")    
        
    print("\n players hand: ")
    for card in player.cards:
        print(card)
    
    print(f"Value of players hand is: {player.value}")



def player_busts(player, dealer, chips):
    
    print("BUST PLAYER !")
    chips.lose_bet()
    pass
def player_wins(player,dealer,chips):
    print("player Wins")
    chips.win_bet()
def dealer_busts(player, dealer, chips):
    print("PLAYER WINS ! DEALER BUSTED!")
    chips.win_bet()
def dealer_wins(player,dealer, chips):
    print("Dealer wins")
    chips.lose_bet()
def push(player, dealer):
    print("Dealer and player tie ! push ")





while True:
    
    print("Welcome to blackjack")
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    # set up player chips
    
    player_chips = Chips()
   
   
    take_bet(player_chips) 
    
    show_some(player_hand,dealer_hand)
    
    
    while playing:
        
        hit_or_stand(deck, player_hand)
        
        show_some(player_hand,dealer_hand)
        
        if player_hand.value > 21 :
            player_busts(player_hand,dealer_hand, player_chips)
            
            break
        
        
        if player_hand.value <= 21:
            
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)
                
            show_all(player_hand, dealer_hand)
            
            
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand,player_chips)
                
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
                
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)     
            else:
                push(player_hand, dealer_hand)
            
            
            print(f"\n player total chips ar at {player_chips.total}")
            
            new_game = input("would you like to play another hand? y/n").lower()
            
            if new_game == 'y':
                playing =True
                continue
            else:
                print("Thank you for playing!")   
                break
        