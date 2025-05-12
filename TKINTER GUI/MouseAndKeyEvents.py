from tkinter import *

class Events(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.geometry("500x500")
        self._button=Button(self,text="Button")
        self._button.grid(row =2, column=2,columnspan=2)
        self._button.bind("<ButtonPress-1>",self._press)
        self._button.bind("<ButtonRelease-1>",self._release)
        self._button.bind("<Enter>",self._enter)
        self._button.bind("<Leave>",self._leave)
        self._button.bind("<B1-Motion>",self._motion)
    
    def _press(self,event):
        print("Mouse 1 Pressed")
    def _release(self,event):
        print("Mouse 1 released")
    def _enter(self,event):
        print("Mouse Entred")
    def _leave(self,event):
        print("Mouse Left")
    def _motion(self,event):
        print("Mouse MOved with 1 pressed")
Events().mainloop()