import pyautogui
import time
import tkinter as tk
from tkinter import *


def screenshot():
    root.withdraw()
    name = int(round(time.time()*1000))
    name = '{}.png'.format(name)
    time.sleep(0.5)
    img = pyautogui.screenshot(name)
    img.show()
    root.deiconify()


root = Tk()
root.title("SCREENSHOT")
root.geometry('500x300+288+88')
root.config(bg='black')
root.resizable(False,False)

canvas = Canvas(root, width = 500, height = 300,bg="black")      
canvas.pack()      
img = PhotoImage(file="snap.png")      
canvas.create_image(0,0,anchor=NW, image=img)

button = tk.Button(root,text="CAPTURE",font =("new roman",11,"bold"),bg = "black",fg ="white",command=screenshot)
button.pack()
button.place(x=126,y=195)

quit_button= tk.Button(root,text="QUIT",font =("new roman",9,"bold"),bg = "black",fg ="white",command=quit)
quit_button.place(x=150,y=237)

root.mainloop()