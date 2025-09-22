#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import tkinter
from random import randint

colours_eng = ['Red', 'Blue', 'Green', 'Pink', 'Black',
               'Yellow', 'Orange', 'Purple', 'Brown']

colours = ['Rød', 'Blå', 'Grønn', 'Rosa', 'Svart',
           'Gul', 'Oransje', 'Lilla', 'Brun']

colour = 0
points = 0
time_left = 30


def start_game(event):
    if time_left == 30:
        countdown()
    next_color()


def next_color():
    global points
    global colour

    if time_left > 0:
        box.focus_set()
        
    if box.get().lower() == colours[colour].lower():
        points = points + 1

    box.delete(0, tkinter.END)

    colour = randint(0, len(colours)-1)
    text = randint(0, len(colours)-1)


    label.config(fg=str(colours_eng[colour]), text=str(colours[text]))
    points_label.config(text="Poeng: " + str(points))
    

def countdown():
    global time_left

    if time_left > 0:
        time_left = time_left - 1
        time_label.config(text="Tid igjen: " + str(time_left))
        time_label.after(1000, countdown)
    else:
        time_label.pack_forget()
        label.pack_forget()
        box.pack_forget()


root = tkinter.Tk()

root.title("Fargespill")
root.geometry("475x300")


instructions = tkinter.Label(root,
                             text="Skriv inn fargen PÅ ordet, ikke selve ordet!",
                             font=("Helvetica", 15))
instructions.pack()


points_label = tkinter.Label(root,
                             text="Trykk enter for å starte.",
                             font=("Helvetica", 30))
points_label.pack()


time_label = tkinter.Label(root,
                           text="Tid igjen: " + str(time_left),
                           font=("Helvetica", 30))
time_label.pack()



label = tkinter.Label(root, font=("Helvetica", 100))
label.pack()

box = tkinter.Entry(root)


root.bind("<Return>", start_game)
box.pack()
box.focus_set()

root.mainloop()




