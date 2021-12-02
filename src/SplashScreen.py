import subprocess;
import tkinter as tk;
import winsound;
from tkinter import *
from PIL import Image, ImageTk;
root = tk.Tk()


root.overrideredirect(True)
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))

#DONT USE JPG IT DOESNT WORK
image_file = "assets/images/mountain.png"


#use .wav preferably.
winsound.PlaySound("assets/sounds/windows11.wav", winsound.SND_ASYNC)

image = tk.PhotoImage(file=image_file)
canvas = tk.Canvas(root, height=height*1, width=width*1, bg="white")
canvas.create_image(width*0.8/2, height*0.8/2, image=image)
canvas.pack()


root.after(3000, root.destroy)
root.mainloop()
subprocess.call("Main.py", shell=True)
print ("Done!")