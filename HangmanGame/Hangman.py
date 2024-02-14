#Choose a random word from the given list
import random
from words import word_list
import stages
print(stages.logo)
#words=["Misapprehension","Miscellaneous","Acquaintance","Irrespective","Prearranged","Surreptitious","Misconception","Entrepreneur","Paraphernalia","Lackadaisical","Magnanimous","Meretricious","Narcissistic","Misdemeanour"]
word_chosen=(random.choice(word_list)).lower()
#Create a list with blanks.
guess_list=[]
for i in range(len(word_chosen)):
    guess_list.append('_')
print(word_chosen)
print(guess_list)   

#Keeping track of lives
lives=6
#play 
used_letters=[]
while '_' in guess_list and not lives==0:
  
  letter=(input("Guess a letter : ")).lower()
  if letter in used_letters:
     print(f"You have already guessed {letter}.")
  
  flag=0
  
  for position in range(len(word_chosen)):
    l=word_chosen[position]
    if l==letter:
        guess_list[position]=letter
        flag=1
  if not flag==1:
       lives-=1
       print(f"{letter} is not in the word.")
       print(f"You have {lives} lives left now:")
  else:
     used_letters.append(letter)
  print(stages.stages[lives])
  print(guess_list)
if(not '_' in guess_list):
   print("You Won!")   
else:
   print("You Lose!")