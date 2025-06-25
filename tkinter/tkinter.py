#statement1 = False
#statement2 = True

#test1 = statement1 and statement2
#test2 = statement1 or statement2
#test3 = statement1 and not statement2
#test4 = statement2 and not statement1

#print(test1)
#print(test2)
#print(test3)
#print(test4)



'''from tkinter import *
import tkinter as tk
window = Tk()
canvas = Canvas(window, bg="wheat4", height = 300, width = 300)
canvas.pack()
canvas.create_line(0,0,300,300, fill = "dark sea green3", width = 10)
canvas.create_line(0,300,300,0, fill = "misty rose", width = 10)
root = tk.Tk()
root.mainloop()'''


#Dount darwing

from tkinter import *
import tkinter as tk
window = Tk()
canvas = Canvas(window, bg="red", height = 300, width = 300)
canvas.pack()
canvas.create_oval(50,50,250,250, fill = "burlywood")
canvas.create_oval(125,125,175,175, fill = "lemon chiffon")
#root = tk.Tk()
window.mainloop() 
