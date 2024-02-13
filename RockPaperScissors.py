import random
print("Welcome to Rock Paper Scissors!")
print("What do you choose ? Type 0 for Rock, 1 for Paper, 2 for Scissors")
user_choice=int(input())
rock='''
    _____
---'  ___)
     (____)
     (____)
     (___)
---._(__)

'''

paper='''
    ____
---'  __)__
       ____)
       _____)
      _____)
---._____)  

'''  

scissors='''
    ____
---'  __)___
       _____)
      _______)
      (__)
---.__(_)

'''
comp_choice=random.randint(0,2)
choice=[rock,paper,scissors]
if(user_choice<3) and (user_choice>=0):
  print("Computer chose:")
  print(choice[comp_choice])
  print("You chose:")
  print(choice[user_choice])
  if(user_choice==comp_choice-1) or (user_choice==comp_choice+2):
    print("You lose!")
  elif(user_choice==comp_choice+1) or (user_choice==comp_choice-2):
    print("You win!")
  else:
    print("Draw!")
else:
    print("You chose an invalid number. You lose!")
