import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','$','%','&','(',')','*','+']

print("Welcome to the Password Generator")
l=int(input("How many letters would you like in your Password ?\n"))
s=int(input("How many symbols would you like in your Password ?\n"))
n=int(input("How many numbers would you like in your Password ?\n"))

p=[]
for char in range(0,l):
    p.append(random.choice(letters))

for char in range(0,s):
    p.append(random.choice(symbols))

for char in range(0,n):
    p.append(random.choice(numbers))
    
random.shuffle(p)
password=""
for char in p:
    password+=char

print(f"Your password is : {password}")
