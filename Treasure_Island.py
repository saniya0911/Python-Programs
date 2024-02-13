print("Welcome to Treasure Island.\nYour mission is to find the Treasure.")
dir=input("You are on a crossroad. Where do you wanna go ? Left or Right ?")
if(dir.lower()=="right"):
    print("You fell into a hole.Game Over!")
else:
    mod=input("Do you wanna swim or do you wanna wait for a boat ?")
    if(mod.lower()=="swim"):
        print("Game Over")
    else:
        door=input("Red door or Blue door or Yellow door ?")
        if(door.lower()=="red") or (door.lower=="yellow"):
            print("Game Over!")
        else:
            print("You win!")
