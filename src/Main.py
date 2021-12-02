from tkinter import *
from tkinter.ttk import *

master = Tk()

#main window
#master.geometry("1920x1080")
width = master.winfo_screenwidth()
height = master.winfo_screenheight()
master.geometry('%dx%d+%d+%d' % (width*0.8, height*0.8, width*0.1, height*0.1))


def openNewWindow():

    newWindow = Toplevel(master)

    newWindow.title("New Window")
    newWindow.geometry('1920x1080')

    Label(newWindow,
          text="This is a new window").pack()

label = Label(master,
              text="This is the main window")

label.pack(pady=10)

btn = Button(master,
             text="Click to open a new window",
             command=openNewWindow)
btn.pack(pady=10)

# mainloop, runs infinitely
mainloop()