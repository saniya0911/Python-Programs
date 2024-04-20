import random
import os
from art import logo, vs
from data import data

def compare(a,b):
    if a>b:
        return "a"
    else:
        return "b"
    
length=len(data)
a = random.randint(0,length-1)
b = random.randint(0,length-1)
should_continue = True
score =0
print(logo)
while(should_continue):
    #print(logo)
    while a==b:
      b = random.randint(0,length-1)
    print(f"Compare A: {data[a]["name"]}, a {data[a]["description"]}, from {data[a]["country"]}.")
    print(vs)
    print(f"Against B: {data[b]["name"]}, a {data[b]["description"]}, from {data[b]["country"]}.")
    guess = (input("Who has more followers ? A or B ?: ")).lower()
    higher = compare(data[a]["follower_count"],data[b]["follower_count"])
    os.system('cls')
    print(logo)
    if guess == higher:
        score+=1
        #print(logo)
        print(f"You're right! Current score: {score}.")
        if higher == "b":
            a=b
        else:
            b = random.randint(0,length-1)
    else:
        #print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        should_continue=False
