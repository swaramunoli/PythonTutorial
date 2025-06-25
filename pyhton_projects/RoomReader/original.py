from tkinter import *
#import time
#from tkinter import messagebox
from PIL import Image, ImageTk


WINDOW_SIZE = "860x550";

COLUMN_STEP = 4;
ICON_COLUMN = 1;
NAME_COLUMN = ICON_COLUMN + COLUMN_STEP;
VALUE_COLUMN = NAME_COLUMN + COLUMN_STEP;
STATUS_COLUMN = VALUE_COLUMN  + COLUMN_STEP;

GRID_PADX = 10;
GRID_PADY = 20;

BUTTON_PADX = 80;
BUTTON_PADY = 20;

COLUMNSPAN_NAME = 3;
COLUMNSPAN_VALUE = 3;
COLUMNSPAN_STATUS = 2;

TEMP_ROW = 1;
HUMIDITY_ROW = 2;
AIRQUALITY_ROW = 3;
CCA_TEAM_ROW = 4;

BORDER_WIDTH = 4;

ICON_WIDTH = 80;
ICON_HEIGHT = 75;
CCA_ICON_HEIGHT = 80;

REFRESH_TIMER = 2000;

root = Tk();

root.title(" CANTON CHARTER ACADEMY ");     # Set title of the window
icon = PhotoImage(file='myicon.png');       # Select title bar icon
root.iconphoto(True, icon);                 # Set title bar icon
root.geometry(WINDOW_SIZE);                 # Set window size
root.configure(bg="lightblue", relief="groove", 
               bd=5, borderwidth=16, 
               highlightbackground="lightblue", 
               highlightthickness=4);

def update_temperature():
    global temp_button_text
    global counter1
    counter1 = (counter1 + 1)
    temp_button_text_c = str(counter1);
    temp_button_text_f = str((counter1 + (counter1 * 9/5)));
    Temperature_value.config(text=temp_button_text_c + u'\u00b0' + ' C' + "          " + temp_button_text_f + u'\u00b0' + ' F')
    root.after(REFRESH_TIMER, update_temperature);


def update_humidity():
    global humidity_button_text
    global counter2
    counter2 = (counter2 + 1)
    humidity_button_text = str(counter2);
    Humidity_value.config(text=humidity_button_text + u"\u0025" + " RH")
    root.after(REFRESH_TIMER, update_humidity);

def update_air_quality():
    global air_quality_button_text
    global counter3
    counter3 = (counter3 + 1)
    air_quality_button_text = str(counter3);
    AirQuality_value.config(text=air_quality_button_text + " IAQ")
    root.after(REFRESH_TIMER, update_air_quality);

counter1 = 0;
counter2 = 0;
counter3 = 0;

# Get images
temp_icon_file = Image.open('room-temperature01.png');
temp_icon_resize = temp_icon_file.resize((50,50), Image.LANCZOS);
temp_icon = ImageTk.PhotoImage(temp_icon_resize);

humidity_icon_file = Image.open('humidity.png');
humidity_icon_resize = humidity_icon_file.resize((50,50), Image.LANCZOS);
humidity_icon = ImageTk.PhotoImage(humidity_icon_resize);

AirQuality_icon_file = Image.open('IAQ.png');
AirQuality_icon_resize = AirQuality_icon_file.resize((90,90));
IAQ_icon = ImageTk.PhotoImage(AirQuality_icon_resize);

cca_team_icon_file = Image.open('cca_team.jpeg');
cca_team_icon_resize = cca_team_icon_file.resize((100,100));
cca_team_icon = ImageTk.PhotoImage(cca_team_icon_resize);


# Create Buttons

Temperature_icon = Button(root, image=temp_icon, borderwidth=BORDER_WIDTH, width=ICON_WIDTH, height=ICON_HEIGHT, relief="groove");
Temperature_icon.grid(row=TEMP_ROW, column=ICON_COLUMN, padx = GRID_PADX, pady = GRID_PADY);

Temperature = Button(root, text="Temperature", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=4, height=1);
Temperature.grid(row=TEMP_ROW, column=NAME_COLUMN, columnspan=COLUMNSPAN_NAME, padx = GRID_PADX, pady = GRID_PADY);

Temperature_value = Button(root, text="Temperature", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), command=update_temperature, width=6, height=1);
Temperature_value.grid(row=TEMP_ROW, column=VALUE_COLUMN, columnspan=COLUMNSPAN_VALUE, padx = GRID_PADX, pady = GRID_PADY);

Temperature_status = Button(root, text="GOOD", fg='green', padx = BUTTON_PADX, pady = BUTTON_PADY, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=1, height=1);
Temperature_status.grid(row=TEMP_ROW, column=STATUS_COLUMN, columnspan=COLUMNSPAN_STATUS, padx = GRID_PADX, pady = GRID_PADY);


Humidity_icon = Button(root, image=humidity_icon, borderwidth=BORDER_WIDTH, width=ICON_WIDTH, height=ICON_HEIGHT, relief="groove");
Humidity_icon.grid(row=HUMIDITY_ROW, column=ICON_COLUMN, padx = GRID_PADX, pady = GRID_PADY);

Humidity = Button(root, text="    Humidity   ", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=4, height=1);
Humidity.grid(row=HUMIDITY_ROW, column=NAME_COLUMN, columnspan=COLUMNSPAN_NAME, padx = GRID_PADX, pady = GRID_PADY);

Humidity_value = Button(root, text="   Humidity   ", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), command=update_humidity, width=6, height=1);
Humidity_value.grid(row=HUMIDITY_ROW, column=VALUE_COLUMN, columnspan=COLUMNSPAN_VALUE, padx = GRID_PADX, pady = GRID_PADY);

Humidity_status = Button(root, text="GOOD", fg='green', padx = BUTTON_PADX, pady = BUTTON_PADY, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=1, height=1);
Humidity_status.grid(row=HUMIDITY_ROW, column=STATUS_COLUMN, columnspan=COLUMNSPAN_STATUS, padx = GRID_PADX, pady = GRID_PADY);


AirQuality_icon = Button(root, image=IAQ_icon, borderwidth=BORDER_WIDTH, width=ICON_WIDTH, height=ICON_HEIGHT, relief="groove");
AirQuality_icon.grid(row=AIRQUALITY_ROW, column=ICON_COLUMN, padx = GRID_PADX, pady = GRID_PADY);

AirQuality = Button(root, text="  Air Quality  ", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=4, height=1);
AirQuality.grid(row=AIRQUALITY_ROW, column=NAME_COLUMN, columnspan=COLUMNSPAN_NAME, padx = GRID_PADX, pady = GRID_PADY);

AirQuality_value = Button(root, text="  Air Quality  ", padx = BUTTON_PADX, pady = BUTTON_PADY, state=DISABLED, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), command=update_air_quality, width=6, height=1);
AirQuality_value.grid(row=AIRQUALITY_ROW, column=VALUE_COLUMN, columnspan=COLUMNSPAN_VALUE, padx = GRID_PADX, pady = GRID_PADY);

AirQuality_status = Button(root, text="GOOD", fg='red', padx = BUTTON_PADX, pady = BUTTON_PADY, relief="groove", borderwidth=BORDER_WIDTH, font=("Times", "16", "bold"), width=1, height=1);
AirQuality_status.grid(row=AIRQUALITY_ROW, column=STATUS_COLUMN, columnspan=COLUMNSPAN_STATUS, padx = GRID_PADX, pady = GRID_PADY);

###################

cca_team_iconb = Button(root, image=cca_team_icon, borderwidth=BORDER_WIDTH, width=ICON_WIDTH, height=CCA_ICON_HEIGHT, relief="groove", padx = BUTTON_PADX, pady = BUTTON_PADY);
cca_team_iconb.grid(row=CCA_TEAM_ROW, column=ICON_COLUMN, padx = GRID_PADX, pady = GRID_PADY, columnspan=2);

update_temperature();
update_humidity();
update_air_quality();

root.mainloop();
