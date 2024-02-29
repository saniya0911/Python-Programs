import turtle
import pandas as pd
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "myprog/Projects/US_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states = pd.read_csv("myprog/Projects/US_states_game/50_states.csv")
all_states = states.state.to_list()
guessed_states =[]

while len(guessed_states)<50:
    answer = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()

    if answer == "Exit":
        break
    if answer in all_states:
        guessed_states.append(answer)
        t=turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = states[states.state==answer]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer)

states_not_guesssed =[]

for s in all_states:
    if s not in guessed_states:
        states_not_guesssed.append(s)

data = pd.DataFrame(states_not_guesssed)
data.to_csv("myprog/Projects/US_states_game/states_left.csv")
#turtle.mainloop() #so that the the screen stays on even after clicking
#screen.exitonclick()