from tkinter import *
import pandas as pd
from random import choice
from Flashcard import Deck, Flashcard

session_done = False
timer_interval = None

def get_words():
  with open('Body Parts Dictionary.csv', 'r') as file:
    return pd.read_csv(file).to_dict('records')

def get_next_word():
  global deck
  unknowns = deck.get_unknowns()
  if unknowns:
    return choice(deck.get_unknowns())
  return None

def knows_word():
  global current_word, session_done, deck
  if session_done:
    deck = Deck(get_words())
    session_done = False
  else:
    current_word.learn()
  current_word = get_next_word()
  if current_word == None:
    canvas.itemconfigure(current_word_lbl, text="No More Words!")
    session_done = True
  else:
    canvas.itemconfigure(current_word_lbl, text=current_word.l2_word)
  
def show_latin():
  global current_word
  window.after_cancel(timer_interval)
  current_word = get_next_word()
  canvas.itemconfigure(current_word_lbl, text=current_word.l2_word)
  

def unknown_word():
  global timer_interval
  canvas.itemconfigure(current_word_lbl, text=current_word.l1_word)
  timer_interval = window.after(3000, show_latin)
  

window = Tk()
window.title('Flash Cards')
window.config(padx=20, pady=20)
target_lang = 'Latin'
deck = Deck(get_words())
current_word = get_next_word()

canvas = Canvas(height=600, width=600)
logo = PhotoImage(file='chalkboard.gif')
canvas.create_image(300, 300, image=logo)
canvas.grid(row=0, column=0, columnspan=2)
canvas.create_text(300, 210, text=target_lang, font=('Arial', 32, 'bold'))
current_word_lbl = canvas.create_text(300, 320, text=current_word.l2_word, font=('Arial', 24, 'bold'))

btn_known = Button(text='✅', command=knows_word)
btn_known.grid(row=1, column=0)
btn_unk = Button(text='🔴', command=unknown_word)
btn_unk.grid(row=1, column=1)






window.mainloop()