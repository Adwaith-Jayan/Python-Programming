from tkinter import *

def display():
    filename=entry.get()
    photo=PhotoImage(file=filename)
    imagewindow=Toplevel()
    imagelabel=Label(imagewindow)
    imagelabel.image=photo
    imagelabel.pack()
    imagewindow.mainloop()


window=Tk()

window.title="Image Displayer"
window.geometry("500x500")

textLabel=Label(window,text="Enter name of image file ('example.png')",compound=TOP)
textLabel.pack()

entry=Entry(window)
entry.pack()

button=Button(window,text="display",command=display)
button.pack(side=BOTTOM)



window.mainloop()