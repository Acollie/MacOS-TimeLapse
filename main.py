from tkinter import *
from tkinter import messagebox
import time
import os

def loop():
    screenshot_count = 1
    if not os.path.exists('screenshots'):
        messagebox.showinfo("Information", "Since there is no Screenshots folder. A file has been generated.")
        os.makedirs('screenshots')
    messagebox.showinfo("Information", "Please note, if you are done with taking screenshots, force quit the program.")
    while True:

        n = w1.get()
        time.sleep(n)
        T.insert(END, "Screenshot "+ str(screenshot_count)+"\n")
        os.system("screencapture -x screenshots/Screenshot_"+str(screenshot_count) + ".png")
        screenshot_count = screenshot_count + 1
        master.update()


master = Tk()
master.geometry("250x250")
master.title("MacOS-TimeLapse")
w1 = Scale(master, from_=1, to=100,orient=HORIZONTAL)
w1.set(50)
w1.pack()

Label(master, text="Stating Loop Scale is in seconds").pack()

Button(master, text='Start Screenshot', command=loop).pack()
Button(master, text='Quit', command=quit).pack()

T = Text(master, height=4, width=50)
S = Scrollbar(master)

S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """"""
T.insert(END, quote)

mainloop()