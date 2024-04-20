import os
from art import logo
print(logo)
print("Welcome to the Silent Auction.")
bidders={}
decision="yes"

def highest_bidder(bidders):
  highest_bid=0
  winner=""
  for bidder in bidders:
    amount=bidders[bidder]
    if(amount>highest_bid):
      highest_bid=amount
      winner=bidder
  print(f"The winner is {winner} with the bid of ${highest_bid}!")

while(decision=="yes"):
 name=input("What's your name ? ")
 bid=int(input("What's your bid ?: $"))
 bidders[name]=bid
 decision=(input("Are there other users who want to bid in the auction ? Type yes or no.")).lower()
 if(decision=="yes"):
    os.system('cls')

highest_bidder(bidders)