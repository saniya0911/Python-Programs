import random
import os
from art import logo

def deal_card():
    cards =[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if sum(cards)>21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, comp_score):
   if user_score==comp_score:
      return "Draw!"
   elif comp_score==0:
      return "You Lose! Opponent has a Blackjack."
   elif user_score==0:
      return "Win with a Blackjack!"
   elif user_score>21 or user_score<comp_score:
      return "You Lose!"
   elif comp_score>21 or user_score>comp_score:
      return "You Win!"
   
def play_game():
 print(logo)
 user_cards =[]
 computer_cards =[]
 is_game_over=False
 for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

 while not is_game_over:  #for user
   user_score = calculate_score(user_cards)
   comp_score = calculate_score(computer_cards)

   print(f"Your cards : {user_cards}, current score : {user_score}")
   print(f"Computer's first card : {computer_cards[0]}")
   if user_score ==0 or comp_score==0 or user_score>21:
    is_game_over = True
   else:
    deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if deal == "y":
        user_cards.append(deal_card())
    else:
        is_game_over=True

 while comp_score !=0 and comp_score<17:   #for computer
   computer_cards.append(deal_card())
   comp_score = calculate_score(computer_cards)

 print(f"Your final hand : {user_cards}, final score: {user_score}")
 print(f"Computer's final hand : {computer_cards}, final score: {comp_score}")
 print(compare(user_score,comp_score))

while input("Do you want to play a game of Blackjack ? Type 'y' or 'n': ")=="y":
   os.system('cls')
   play_game()