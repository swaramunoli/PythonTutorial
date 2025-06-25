from tkinter import *
from random import *
from time import sleep

window = Tk()
canvas = Canvas(window, bg = "black", height = 300 , width = 300)
canvas.pack()

while True:
    canvas.delete("all")
    for i in range(10):
        x = randint(0,300)
        y = randint(0,300)
        canvas.create_oval(x,y,x+10,y+10, fill = "lemon chiffon", width =2)
        window.update()
        sleep(0.5)

