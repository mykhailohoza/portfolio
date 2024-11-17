from random import shuffle

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}
playing = True 

class Card():
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return f"{self.rank} of {self.suit}" 

class Deck():
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))
    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp +='\n'+card.__str__()
        return "The deck has: "+ deck_comp
        
    def shuffle(self):
        shuffle(self.deck)
        
    def deal(self):
        return self.deck.pop()

    
# a = Deck()
# a.shuffle()
# print(a)

class Hand():
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank =='Ace':
            self.aces +=1
        
        
    def adjust_for_ace(self):
        while self.value >21 and self.aces:
            self.value -= 10
            self.aces -=1
            

class Chips():
    def __init__(self):
        self.total = 100
        self.bet =0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
    
        
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input(print("Player, make your bet! ")))
            break
        except:
            print("You entered not a number")
        else:
            if chips.bet > chips.total:
                print("Sorry, your bet can't exceed",chips.total)
            else:
                break

        
def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()
    

def hit_or_stand(deck, hand ):
    global playing
    desicion = 'wrong'
    
    while desicion not in ['hit', 'stand']:
        desicion = input(print("Do you want to hit or to stand? \nEnter 'hit' or 'stand: ")).lower()
    
    
    if desicion == 'hit':
        hit(deck, hand)
    else:
        print('player stnads. Dealer is playing')
        playing = False
    
    
def show_some(player, dealer):
    print('\n Dealre`s Hand:')
    print("First card hidden!")
    print(dealer.cards[1])

    print("\nPlayer`s hand: ")
    for card in player.cards:
        print(card)
        
def show_all(player, dealer):
    print("\nDealer`s hand: ")
    for card in dealer.cards:
        print(card)
        
    print(f"Value of delares hand is: {dealer.value}")
        
    print("\nPlayer`s hand: ")
    for card in player.cards:
        print(card)
    print(f"Value of player hand is: {player.value}")


def player_busts(player, dealer,chips):
    print("Bust player")
    chips.lose_bet()

def player_wins(player, dealer,chips):
    print("player won")
    chips.win_bet()

def dealer_busts(player, dealer,chips):
    print("player won! dealer busted")
    chips.win_bet()
    
def dealer_wins(player, dealer,chips):
    print("Dealer won")
    chips.lose_bet()
    
def push(player, dealer):
    print('Dealer and player tie!PUSH') 
    
    


while True:
    print("Welcome")
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    
    player_chips = Chips()
    take_bet(player_chips)
    
    show_some(player_hand, dealer_hand)
    
    while playing:
        hit_or_stand(deck, player_hand)
        
        show_some(player_hand, dealer_hand)
        
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break
    if player_hand.value <= 21:
        while dealer_hand.value > 17:
            hit(deck, dealer_hand)
            
        show_all(player_hand, dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
    
    print(f"Player total chips are: {player_chips.total}")
    
    new_game = input
    desicion = 'wrong'
    
    while desicion not in ['y', 'n']:
        desicion = input(print("Do you want to play another hand? \nEnter 'y' or 'n: ")).lower()
    if desicion == 'y':
        playing = True
        continue
    else:
        print("Thanks for the game")
        break