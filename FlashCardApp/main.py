from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("myprog/Projects/FlashCardApp/data/words.csv")
except FileNotFoundError:
    data = pandas.read_csv("myprog/Projects/FlashCardApp/data/french_words.csv")

words = data.to_dict(orient='records')
current_card={}

def flip():
    canvas.itemconfig(canvas_image, image=back)
    canvas.itemconfig(card_title, text="English",fill="white")
    canvas.itemconfig(card_word, text=current_card["English"] ,fill="white")

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    canvas.itemconfig(canvas_image, image=front)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill= "black")
    window.after(3000, func=flip)

def is_known():
    words.remove(current_card)
    data = pandas.DataFrame(words)
    data.to_csv("myprog/Projects/FlashCardApp/data/words.csv", index=False)
    next_card()

#UI
window = Tk()
window.title("Flash Card App")
window.geometry("850x700")
window.config(padx=50, bg=BACKGROUND_COLOR)
flip_timer=window.after(3000, func=flip)

front = PhotoImage(file="myprog/Projects/FlashCardApp/images/card_front.png")
back = PhotoImage(file="myprog/Projects/FlashCardApp/images/card_back.png")

canvas = Canvas(height=560, width=790,bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_image = canvas.create_image(395, 285, image=front)

card_title = canvas.create_text(380, 150 ,text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(380, 283 ,text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

cross = PhotoImage(file="myprog/Projects/FlashCardApp/images/wrong.png")
wrong = Button(image=cross, width=80, height=80,highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
wrong.grid(row=1, column=0)

tick = PhotoImage(file="myprog/Projects/FlashCardApp/images/right.png")
correct = Button(image=tick, width=80, height=80, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
correct.grid(row=1, column=1)

next_card()

window.mainloop()