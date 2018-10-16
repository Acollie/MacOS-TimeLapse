from tkinter import *
from tkinter import messagebox
import time
import os
import cv2


def loop():
    frame=w2.get()
    screenshot_count = 1
    if not os.path.exists('screenshots'):
        messagebox.showinfo("Information", "Since there is no Screenshots folder. A file has been generated.")
        os.makedirs('screenshots')
    messagebox.showinfo("Information", "Please note, if you are done with taking screenshots, force quit the program.")

    if frame==0:
        while True:
            frame = frame + 1
            n = w1.get()
            time.sleep(n)
            T.insert(END, "Screenshot " + str(screenshot_count) + "\n")
            screenshot(int(screenshot_count))
            screenshot_count = screenshot_count + 1
            master.update()
    else:
        print("else")
        n = w2.get()
        x=0
        while x<n:
            print("n=",n,"frame=",x)
            x=x+1
            time.sleep(w1.get())
            T.insert(END, "Screenshot " + str(screenshot_count) + "\n")
            screenshot(int(screenshot_count))
            screenshot_count = screenshot_count + 1
            master.update()


def screenshot(n):
    os.system("screencapture -x screenshots/Screenshot_" + str(n) + ".png")

def movie_gen():
    print("movi gen")
    image_folder = 'screenshots'
    video_name = 'video.mov'

    images = [img for img in os.listdir(image_folder) if img.endswith(".png")]
    frame = cv2.imread(os.path.join(image_folder, images[0]))
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, -1, 1, (width, height))

    for image in images:
        video.write(cv2.imread(os.path.join(image_folder, image)))

    cv2.destroyAllWindows()
    video.release()

master = Tk()
master.geometry("330x300")
master.title("MacOS-TimeLapse")
w1 = Scale(master, from_=1, to=100,orient=HORIZONTAL)
w1.set(50)
w1.pack()
Label(master, text="Stating Loop Scale is in seconds").pack()

w2 = Scale(master, from_= 0, to =1000, orient=HORIZONTAL)
w2.set(50)
w2.pack()
Label(master, text="Number of frames (if 0 then will run indefinitely)").pack()

Button(master, text='Start Screenshot', command=loop).pack()
Button(master, text='Quit', command=quit).pack()
Button(master, text='Movie Generate', command=movie_gen).pack()


T = Text(master, height=4, width=50)
S = Scrollbar(master)

S.pack(side=RIGHT, fill=Y)
T.pack(side=LEFT, fill=Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """"""
T.insert(END, quote)

mainloop()