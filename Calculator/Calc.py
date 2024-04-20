import os
from art import logo
def add(n1,n2):
    return n1+n2

def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations ={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
 print(logo)
 num1 = float(input("Enter the first number : "))

 for ch in operations:
    print(ch)

 should_continue= True

 while should_continue:
  operation = input("Pick an operation: ")
  num2 = float(input("Enter the next number : "))
  answer = operations[operation](num1,num2)
  print(f"{num1} {operation} {num2} = {answer}")

  if input(f"Type 'y' to continue calculating with {answer}: ") == 'y' :
     num1 = answer
  else:
     should_continue=False
     os.system('cls')
     calculator()

calculator()