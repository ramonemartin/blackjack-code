# Name: Ramone Martin
# Class: Codecademy
# Date: 12.8.2024

# Title: Blackjack Terminal Game
# Description: This is a blackjack terminal game using Object Oriented Programming. The game will have two classes, one for the dealer and another for the player. 

import random
# The random module will be used to randomly generate values from 1,11. 11 being an ace. 

class Blackjack:
# This class will create the game and all of the functions pertained to.
#It will require a function to draw cards, determine winners and losers, function to manage bets

# Here I am going to define my class variables
    deck = [
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11,
    2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11
    ]


 

    def __init__(self, name):
        """
        The initializer will have the players name and the amount they are going to wager.
        """
        self.name = name
        self.hand = []

    def __repr__(self):
        return ("This is player {name} ".format(name = self.name))
    
    def hit(self):
        random_card = random.choice(self.deck)
        self.deck.remove(random_card)
        if random_card == 11:
            either = int(input("1 or 11? "))
            if either == 1:
                self.hand.append(1)
            elif either == 11:
                self.hand.append(11)
            else:
                print("Invalid choice. defaulting to 11")
        else:
            self.hand.append(random_card)
   
        print(sum(self.hand))


    def stay(self):
        self.hand.append(0)
        print(sum(self.hand))
        
     
    def draw_cards(self):
            print("This is player {name}'s turn".format(name = self.name))
            for i in range(2):
                self.hit()
            while sum(self.hand) < 21:
                h = input("Would you like to hit or stay? ").lower()
                if h == 'hit'.lower():
                    self.hit()
                elif h == 'stay'.lower():
                    self.stay()
                    break
            if sum(self.hand) == 21:
                print("Blackjack!")
            elif sum(self.hand) > 21:
                print("Bust!")

    def view_hand(self):
        print("{name}'s hand: ".format(name = self.name))
        print(sum(self.hand))
    

            
# class Wager:

#     def __init__(self, name, amount):
#         self.amount = amount
#         self.name = name 
#         self.valid_bet = True
#         self.bank = 0


    
#     def valid_wager(self):
#         while self.valid_bet:
#             bet = int(input("How much are you going to bet? "))
#             if bet > self.amount:
#                 print("You do not have enough money. Try again. ")
#                 bet
#                 self.valid_bet == False
#             elif bet <= 0:
#                 print("You must bet something. ")
#                 bet
#                 self.valid_bet == False
#             else:
#                 self.valid_bet == True
#                 break
#         return bet

#     def add_to_bank(self):
#         self.bank += self.valid_wager()
#         return self.bank

#     def display_bank(self):
#         print(f"you have: ${self.bank}")



        




  


    

# The print statements here are used to test functions and troubleshoot(debug).


p1 = Blackjack('Ramone')
p2 = Blackjack('Dealer')

bank = 0
wager = int(input("How much are you going to bet? "))

p1.draw_cards()
p2.draw_cards()

player1_hand = sum(p1.hand)
player2_hand = sum(p2.hand)



def game_flow():
    if player1_hand <= 21 and player2_hand > 21:
        print(f"{p1.name} wins!")
        print(bank + wager)
    elif player1_hand == player2_hand:
        print("We have a tie!")
        print(bank)
    elif player2_hand <= 21 and player1_hand > 21:
        print(f"{p2.name} wins!")
        print(bank - wager)
    elif player2_hand > player1_hand and player1_hand and player2_hand <= 21:
        print(f"{p2.name} wins")
        print(bank - wager)
    elif player1_hand > player2_hand and player2_hand and player1_hand <= 21:
        print(f"{p1.name} wins")
        print(bank - wager)
    else:
        print("You both lose!")
        print(bank - wager)



print(f" {p1.name} : {player1_hand}")
print(f" {p2.name} : {player2_hand}")

play_again = input("Would you like to play again? ").lower()

if play_again == 'y':
    game_flow()
elif play_again == 'n':
    print("Good Game")
else:
    print("Please type y or n. ")
    print(play_again)











