from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ('Ariel', 40, 'italic')
WORD_FONT = ('Ariel', 60, 'bold')

data_path = 'data/french_words.csv'

# ------------------------- UI ------------------------- #
window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)

front_image = PhotoImage(file='images/card_front.png')
back_image = PhotoImage(file='images/card_back.png')
correct_image = PhotoImage(file='images/right.png')
wrong_image = PhotoImage(file='images/wrong.png')

canvas = Canvas(height=526, width=800, bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.create_image(400, 263, image=front_image)
canvas.grid(row=0, column=0, columnspan=2)

correct_button = Button(image=correct_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
correct_button.grid(row=1, column=1)

wrong_button = Button(image=wrong_image, highlightthickness=0, bg=BACKGROUND_COLOR, borderwidth=0)
wrong_button.grid(row=1, column=0)

language_text = canvas.create_text(400, 150, text='French', font=LANG_FONT)
word_text = canvas.create_text(400, 263, text='trouve', font=WORD_FONT)

window.mainloop()

