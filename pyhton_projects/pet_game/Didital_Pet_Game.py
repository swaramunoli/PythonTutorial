from tkinter import *
from tkinter.ttk import *
from tkinter.simpledialog import *
from time import*
from random import *

root = Tk()
root.geometry("300x650+500+50")

#initialization

calm_img = PhotoImage(file='calm.png')
happy_img = PhotoImage(file='happy.png')
grumpy_img = PhotoImage(file='grumpy.png')
sad_img = PhotoImage(file='sad.png')
annoyed_img = PhotoImage(file='annoyed.png')

pet_img = PhotoImage(file='pet.png')
play_img = PhotoImage(file='play.png')
feed_img = PhotoImage(file='feed.png')

pauseicon = PhotoImage(file='pauseicon.png')

play_level = 50
feed_level = 50
pet_level = 50

#functions

def check_play(lower, upper):
    if play_level >= lower and play_level <= upper:
        return True
    else:
        return False
    

def check_feed(lower, upper):
    if feed_level >= lower and feed_level <= upper:
        return True
    else:
        return False


def check_pet(lower, upper):
    if pet_level >= lower and pet_level <= upper:
        return True
    else:
        return False

    
def update_display():
    if time() < annoyed_done:
        display_lbl.configure(image = annoyed_img)

    elif check_play(33, 66) and check_feed(33, 66) and check_pet(33,  75):
        display_lbl.configure(image=calm_img)

    elif check_play(50, 75) and check_feed(50, 75) and check_pet(50, 75):
        display_lbl.configure(image=happy_img)

    elif check_play(25, 100) and check_feed(25, 100) and check_pet(25, 100):
        display_lbl.configure(image=grumpy_img)

    else:
        display_lbl.configure(image = sad_img)

def update_ui():
    play_bar['value'] = play_level
    feed_bar['value'] = feed_level
    pet_bar['value'] = pet_level
    update_display()


#Functions: User Interface (UI) +  buttons

def play():
    global play_level
    check_click()
    play_level +=5
    if play_level>100:
        play_level =100
    update_ui()

def feed():
    global feed_level
    check_click()
    feed_level +=5
    if feed_level>100:
        feed_level =100
    update_ui()

def pet():
    global pet_level
    check_click()
    pet_level +=5
    if pet_level>100:
        pet_level =100
    update_ui()
    
def update_levels():
    global play_level,pet_level, feed_level
    
    which = randint(1,3)
    
    if which ==1 and play_level >=5:
        play_level -=5 

    if which == 2 and pet_level >= 5:
        pet_level -=5

    if which ==3 and feed_level >=5:
        feed_level -=5

next_update = 0
def schedule_update():
    global next_update
    delay = randint(2,5)
    next_update = time() +delay

playing = True
def frame():
    root.after(5,frame)
    if playing == True:
        if time() >= next_update:
            update_levels()
            schedule_update()
        update_ui()

last_click = 0
annoyed_done = 0

def check_click():
    global last_click, annoyed_done
    cur = time()
    if cur - last_click < 1:
        annoyed_done = cur +5
    last_click = cur

def toggle_pause():
    global playing
    if playing == True:
        playing = False
    else:
        playing = True


#set up UI
display_lbl = Label(root,image = calm_img)
display_lbl.pack(pady=10)

name_lbl = Label(root,text="Name" )
name_lbl.pack()

play_button = Button(root,text="Play", width = 10,command=play)
play_button.pack(pady=10)

play_label = Label(root,image = play_img)
play_label.pack()

play_bar = Progressbar(root, length=250)
play_bar.pack()




feed_button = Button(root,text="Feed", width = 10, command=feed)
feed_button.pack(pady=10)

feed_label = Label(root,image = feed_img)
feed_label.pack()

feed_bar = Progressbar(root, length=250)
feed_bar.pack()




pet_button = Button(root,text="Pet", width = 10, command=pet)
pet_button.pack(pady=10)

pet_label = Label(root,image = pet_img)
pet_label.pack()

pet_bar = Progressbar(root, length=250)
pet_bar.pack()

paused_btn= Button(root, image=pauseicon, command=toggle_pause)
paused_btn.pack(pady = 10)




#start game

name = askstring("Name", "What's your pets name?")
name_lbl.configure(text=name)


schedule_update()
frame()
root.mainloop()