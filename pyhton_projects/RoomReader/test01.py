from tkinter import *
from tkinter import messagebox
import tkinter as tk
from PIL import Image, ImageTk
import tkinter.messagebox as msgbox

''' 
When we say, for example " import tkinter as tk" we are renaming the library. Same with line 5
'''


WINDOW_SIZE = "860x525"

COLUMN_STEP = 4             # space between buttons
ICON_COLUMN = 1             # space between window border and icon
NAME_COLUMN = ICON_COLUMN + COLUMN_STEP            # placement of name buttons ( temp, humidity, and AQ)
VALUE_COLUMN = NAME_COLUMN + COLUMN_STEP          # placement of value column ( celcius, IAQ )
STATUS_COLUMN = VALUE_COLUMN + COLUMN_STEP

# this determines the space between each box and column
GRID_PADX = 10
GRID_PADY = 10

#changes the length and width of the boxes
BUTTON_PADX = 80
BUTTON_PADY = 20

'''
This is used for the column span for each type of button ( icon, name ( ex: temp), value ( celsius),  status
'''
COLUMNSPAN_NAME = 3
COLUMNSPAN_VALUE = 3
COLUMNSPAN_STATUS = 2

# states which row temp, humidity, AQ and CC is places. Try changing them
TEMP_ROW = 3
HUMIDITY_ROW = 2
AIRQUALITY_ROW = 4
CCA_TEAM_ROW = 1

#TEMP_ROW = 2
#HUMIDITY_ROW = 3
#AIRQUALITY_ROW = 4
#CCA_TEAM_ROW = 1


BORDER_WIDTH = 4

'''
these are variables that we put in the code when creating buttons so that the fist column buttons are uniform
'''
ICON_WIDTH = 80
ICON_HEIGHT = 75

CCA_ICON_WIDTH = 140
CCA_ICON_HEIGHT = 140

REFRESH_TIMER = 2000

root = Tk()

# "settings" for the main window
root.title(" CANTON CHARTER ACADEMY ")     # Set title of the window
icon = PhotoImage(file='myicon.png')       # Select title bar icon
root.iconphoto(True, icon)                 # Set title bar icon
root.geometry(WINDOW_SIZE)                 # Set window size
root.configure(bg="lightblue", relief="groove", 
               bd=5, borderwidth=16, 
               highlightbackground="lightblue", 
               highlightthickness=4)

'''These functions are used when making buttons '''

def on_closing():
    if msgbox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

def show_team_message():
    msgbox.showinfo("CCA Jr Robotics Team", "SWARA MUNOLI \nANISH BHARGAVA \nPAAVANI JAIN")

def show_temp_message():
    msgbox.showinfo("Temperature", "Show temperature info")

def show_humidity_message():
    msgbox.showinfo("Humidity", "Show temperature info")

def show_IAQ_message():
    msgbox.showinfo("Index of Air Quality", "Show air quality info")        

def update_temperature():
    global temp_button_text
    global counter1
    counter1 = (counter1 + 1)
    temp_button_text_c = str(counter1)
    temp_button_text_f = str((counter1 + (counter1 * 9/5)))
    Temperature_value.config(text=temp_button_text_c + u'\u00b0' + ' C' + "          " + temp_button_text_f + u'\u00b0' + ' F')
    #Temperature_value.config(text= temp_button_text_f + u'\u00b0' + ' F' + "        " + temp_button_text_c + u'\u00b0' + ' C')
    root.after(REFRESH_TIMER, update_temperature)


def update_humidity():
    global humidity_button_text
    global counter2
    counter2 = (counter2 + 1)
    humidity_button_text = str(counter2)
    Humidity_value.config(text=humidity_button_text + u"\u0025" + " RH")
    root.after(REFRESH_TIMER, update_humidity)

def update_air_quality():
    global air_quality_button_text
    global counter3
    counter3 = (counter3 + 1)
    air_quality_button_text = str(counter3)
    AirQuality_value.config(text=air_quality_button_text + " IAQ")
    root.after(REFRESH_TIMER, update_air_quality)

counter1 = 0
counter2 = 0
counter3 = 0

def show_iaq_image():
    # Create a new top-level window (pop-up)
    popup = Toplevel()
    popup.title("IAQ Color Coding")

    # Load the image using Pillow
    image = Image.open("IAQ_color_coding.jpg")  # Replace "image.jpg" with your image file path
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(popup, image=photo)
    image_label.image = photo  # Keep a reference to the image to prevent garbage collection
    image_label.pack()

    # Add a close button to the pop-up
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

def show_humidity_image():
    # Create a new top-level window (pop-up)
    popup = Toplevel()
    popup.title("Humidity Chart")

    # Load the image using Pillow
    image = Image.open("ideal_humidity.jpg")  # Replace "image.jpg" with your image file path
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(popup, image=photo)
    image_label.image = photo  # Keep a reference to the image to prevent garbage collection
    image_label.pack()

    # Add a close button to the pop-up
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

def show_temperature():
    # Create a new top-level window (pop-up)
    popup = Toplevel()
    popup.title("Temperature Chart")

    # Load the image using Pillow
    image = Image.open("temp_chart.jpg")  # Replace "image.jpg" with your image file path
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(popup, image=photo)
    image_label.image = photo  # Keep a reference to the image to prevent garbage collection
    image_label.pack()

    # Add a close button to the pop-up
    close_button = tk.Button(popup, text="Close", command=popup.destroy)
    close_button.pack()

# Get images
temp_icon_file = Image.open('room-temperature01.png')
temp_icon_resize = temp_icon_file.resize((50,50), Image.LANCZOS)
temp_icon = ImageTk.PhotoImage(temp_icon_resize)

humidity_icon_file = Image.open('humidity.png')
humidity_icon_resize = humidity_icon_file.resize((50,50), Image.LANCZOS)
humidity_icon = ImageTk.PhotoImage(humidity_icon_resize)

AirQuality_icon_file = Image.open('IAQ.png')
AirQuality_icon_resize = AirQuality_icon_file.resize((90,90))
IAQ_icon = ImageTk.PhotoImage(AirQuality_icon_resize)

cca_team_icon_file = Image.open('cca_team.jpeg')
cca_team_icon_resize = cca_team_icon_file.resize((170,170))
cca_team_icon = ImageTk.PhotoImage(cca_team_icon_resize)


# Create Buttons

Temperature_icon = Button(root, image=temp_icon, borderwidth=BORDER_WIDTH, width=ICON_WIDTH, height=ICON_HEIGHT, relief="groove", command=show_temp_message)
Temperature_icon.grid(row=TEMP_ROW, column=ICON_COLUMN, padx = GRID_PADX, pady = GRID_PADY)

Temperature = Button(root, text="Temperature", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=4, height=1)
Temperature.grid(row=TEMP_ROW, column=NAME_COLUMN, columnspan=COLUMNSPAN_NAME, padx = GRID_PADX, pady = GRID_PADY)

Temperature_value = Button(root, text="Temperature", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), command=update_temperature, width=6, height=1)
Temperature_value.grid(row=TEMP_ROW, column=VALUE_COLUMN, columnspan=COLUMNSPAN_VALUE, padx = GRID_PADX, pady = GRID_PADY)

Temperature_status = Button(root, text="GOOD", fg='green', padx = BUTTON_PADX, pady = BUTTON_PADY, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=1, height=1,command=show_temperature)
Temperature_status.grid(row=TEMP_ROW, column=STATUS_COLUMN, columnspan=COLUMNSPAN_STATUS, padx = GRID_PADX, pady = GRID_PADY)


Humidity_icon = Button(root, image=humidity_icon, borderwidth=BORDER_WIDTH, width=ICON_WIDTH, height=ICON_HEIGHT, relief="groove", command=show_humidity_message)
Humidity_icon.grid(row=HUMIDITY_ROW, column=ICON_COLUMN, padx = GRID_PADX, pady = GRID_PADY)

Humidity = Button(root, text="    Humidity   ", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=4, height=1)
Humidity.grid(row=HUMIDITY_ROW, column=NAME_COLUMN, columnspan=COLUMNSPAN_NAME, padx = GRID_PADX, pady = GRID_PADY)

Humidity_value = Button(root, text="   Humidity   ", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), command=update_humidity, width=6, height=1)
Humidity_value.grid(row=HUMIDITY_ROW, column=VALUE_COLUMN, columnspan=COLUMNSPAN_VALUE, padx = GRID_PADX, pady = GRID_PADY)

Humidity_status = Button(root, text="GOOD", fg='green', padx = BUTTON_PADX, pady = BUTTON_PADY, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=1, height=1, command= show_humidity_image )
Humidity_status.grid(row=HUMIDITY_ROW, column=STATUS_COLUMN, columnspan=COLUMNSPAN_STATUS, padx = GRID_PADX, pady = GRID_PADY)


AirQuality_icon = Button(root, image=IAQ_icon, borderwidth=BORDER_WIDTH, width=ICON_WIDTH, height=ICON_HEIGHT, relief="groove", command=show_IAQ_message)
AirQuality_icon.grid(row=AIRQUALITY_ROW, column=ICON_COLUMN, padx = GRID_PADX, pady = GRID_PADY)

AirQuality = Button(root, text="  Air Quality  ", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=4, height=1)
AirQuality.grid(row=AIRQUALITY_ROW, column=NAME_COLUMN, columnspan=COLUMNSPAN_NAME, padx = GRID_PADX, pady = GRID_PADY)

AirQuality_value = Button(root, text="  Air Quality  ", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), command=update_air_quality, width=6, height=1)
AirQuality_value.grid(row=AIRQUALITY_ROW, column=VALUE_COLUMN, columnspan=COLUMNSPAN_VALUE, padx = GRID_PADX, pady = GRID_PADY)

AirQuality_status = Button(root, text="GOOD", fg='red', padx = BUTTON_PADX, pady = BUTTON_PADY, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=1, height=1, command=show_iaq_image)
AirQuality_status.grid(row=AIRQUALITY_ROW, column=STATUS_COLUMN, columnspan=COLUMNSPAN_STATUS, padx = GRID_PADX, pady = GRID_PADY)

###################

cca_team_iconb = Button(root, image=cca_team_icon, borderwidth=BORDER_WIDTH, width=CCA_ICON_WIDTH, height=CCA_ICON_HEIGHT, relief="groove", padx = BUTTON_PADX, pady = BUTTON_PADY, command=show_team_message)
#cca_team_iconb.grid(row=CCA_TEAM_ROW, column=ICON_COLUMN, padx = GRID_PADX, pady = GRID_PADY, columnspan=2)
cca_team_iconb.grid(row=CCA_TEAM_ROW, column=8, padx = GRID_PADX, pady = GRID_PADY, columnspan=2)

update_temperature()
update_humidity()
update_air_quality()

root.mainloop()
