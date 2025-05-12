""" A python Tkinter GUI program which loads an image in current folder based on user input"""
from tkinter import *

class ImageLoader(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Image Loader")
        self._filename=StringVar()
        self._fileEntry=Entry(self,textvariable=self._filename)
        self.grid()
        self._fileEntry.grid(row=0,column=1)

        self._but=Button(self,text="GET",command=self.view)
        self._but.grid(row=1,column=1,columnspan=2)

    def view(self):
        filename=self._filename.get()
        self._img=PhotoImage(file=filename)
        self._imgLabel=Label(self,image=self._img)
        self._imgLabel.grid()

ImageLoader().mainloop()