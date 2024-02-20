#3 flavors
#Espresso- 50 ml water, 18g coffee
#Latte- 200ml water, 24g coffee, 150 ml milk
#Cappuccino- 250ml water, 24g coffee, 100ml milk

flavors = {
    "espresso":{
    "ingredients":{
    "water":50,
    "coffee":18,
    },
    "cost": 1.5
   },
   "latte":{
    "ingredients":{
      "water":200,
      "coffee":24,
      "milk":150,
   },
    "cost": 2.5
   },
   "cappuccino":{
   "ingredients":{
    "water":250,
    "coffee":24,
    "milk":100,
   },
    "cost": 3.0
   }
}
profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee":100
}

def resorce_check(order):
    '''Returns True when order can be made, False if ingredients are insufficient.'''
    for item in order:
        if order[item]>resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    '''Returns the total calculated from the coins inserted.'''
    print("Please insert coins.")
    total = int(input("How many quarters?: "))*0.25
    total += int(input("How many dimes?: "))*0.1
    total += int(input("How many nickels?: "))*0.05
    total += int(input("How many pennies?: "))*0.01
    return total

def is_transaction_successfull(payment, drink_cost):
    '''Return True when the payment is accepted, or False if money is insufficient.'''
    if payment>=drink_cost:
        change = round(payment-drink_cost, 2)
        print(f"Here is ${change} change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(name, ingredients):
    '''Deduct the required ingredients from the resources.'''
    for item in ingredients:
        resources[item]-=ingredients[item]
    print(f"Here is your {name}. Enjoy!")

is_on = True
while is_on:
    choice = input("What would you like ? (espresso/latte/cappuccino): ").lower()
    if(choice=="off"):
        is_on=False
    elif choice=="report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: ${profit}")
    else:
        drink = flavors[choice]
        if resorce_check(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successfull(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
            

