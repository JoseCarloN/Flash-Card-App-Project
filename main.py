from tkinter import *
import pandas as pd
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')
WAIT_TIME = 3000

data_path = 'data/french_words.csv'
words_to_learn_path = 'data/words_to_learn.csv'

try:
    words_data = pd.read_csv(words_to_learn_path)
except FileNotFoundError:
    words_data = pd.read_csv(data_path)
finally:
    words_dict = words_data.to_dict(orient='records')

word = {}


# ------------------------- CHANGE CARD ------------------------- #
def next_card():
    global word, flip_timer

    word = choice(words_dict)
    window.after_cancel(flip_timer)

    canvas.itemconfig(card_background, image=front_image)
    canvas.itemconfig(language_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=word.get('French'), fill='black')
    flip_timer = window.after(ms=WAIT_TIME, func=flip_card)


def flip_card():
    global word

    canvas.itemconfig(language_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=word.get('English'), fill='white')
    canvas.itemconfig(card_background, image=back_image)


# ------------------------- WORDS TO LEARN ------------------------- #
def learnt_word():
    global words_dict, word
    words_dict.remove(word)
    pd.DataFrame.from_records(words_dict).to_csv('data/words_to_learn.csv', index=False)
    next_card()


# ------------------------- UI ------------------------- #
window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
correct_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

correct_button = Button(image=correct_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=learnt_word)
correct_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0, command=next_card)
wrong_button.grid(row=1, column=0)

language_text = canvas.create_text(400, 150, text='', font=LANG_FONT)
word_text = canvas.create_text(400, 263, text='', font=WORD_FONT)

flip_timer = window.after(ms=WAIT_TIME, func=flip_card)
next_card()

window.mainloop()

