from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
currentCard = {}

def flipCard():
    canvas.itemconfig(cardTitle, text = "English", fill = "white")
    canvas.itemconfig(cardWord, text = currentCard["English"], fill = "white")
    canvas.itemconfig(cardBackground, image = cardBackImg)

def next_card():
    global currentCard, flip_timer
    window.after_cancel(flip_timer)
    currentCard = random.choice(to_learn)
    canvas.itemconfig(cardTitle, text = "French", fill = "black")
    canvas.itemconfig(cardWord, text = currentCard["French"], fill = "black")
    canvas.itemconfig(cardBackground, image = cardFrontImg)
    flip_timer = window.after(3000, next_card)


window = Tk()
window.title("Flashy")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)

window.after(3000, func = flipCard)

flip_timer = window.after(3000, func = flipCard)

canvas = Canvas(width = 800, height = 526)
cardFrontImg = PhotoImage(file = "images/card_front.png")
cardBackImg = PhotoImage(file = "images/card_back.png")
cardBackground = canvas.create_image(400,263, image = cardFrontImg)
canvas.grid(row = 0, column = 0, columnspan = 2)
cardTitle = canvas.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
cardWord = canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))
canvas.config(bg = BACKGROUND_COLOR, highlightthickness = 0)

crossImage = PhotoImage(file = "images/wrong.png")
unknownButton = Button(image = crossImage, highlightthickness = 0, command = next_card)
unknownButton.grid(row = 1, column = 0)

checkImage = PhotoImage(file = "images/right.png")
checkButton = Button(image = checkImage, highlightthickness = 0, command = next_card)
checkButton.grid(row = 1, column = 1)

next_card()

window.mainloop()




