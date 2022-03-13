from tkinter import *
from tkinter import messagebox
import os
def flashit():
    if dev.get() == "esp8266":
        os.system("python3 esptool.py --chip " + dev.get() + " --port " + com.get() + " --baud " + baud.get() + " write_flash" + " --flash_size=detect 0 " + path.get())
    elif dev.get() == "esp32":
        os.system("python3 esptool.py --chip " + dev.get() + " --port " + com.get() + " --baud " + baud.get() + " write_flash" + " -z 0x1000 " + path.get())
    messagebox.showinfo("Flash complete", "Flash complete")
def clearit():
    os.system("python3 esptool.py --chip " + dev.get() +  " --port " + com.get() + " erase_flash")
    messagebox.showinfo("Clear complete", "Clear complete")
window = Tk()
window.title("Advanced ESP flasher")
win = Canvas(window, width=550, height=550)
win.pack()
win.create_text(68, 15, text="Enter com port:", font=("Helvetica", 17))
com = Entry(width=30)
com.pack()
com.place(x=8, y=30)
win.create_text(150, 63, text="Enter device (esp8266, esp32, eg.):", font=("Helvetica", 17))
dev = Entry(width=30)
dev.pack()
dev.place(x=8, y=80)
win.create_text(66, 111, text="Enter full path:", font=("Helvetica", 17))
path = Entry(width=30)
path.pack()
path.place(x=8, y=130)
win.create_text(128, 159, text="Enter baud rate (460800, eg.):", font=("Helvetica", 17))
baud = Entry(width=30)
baud.pack()
baud.place(x=8, y=180)
flash = Button(window, text="Flash", command=flashit)
flash.pack()
clear = Button(window, text="Clear", command=clearit)
clear.pack()
window.mainloop()