from tkinter import *

class LabelDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Lable Demo")
        self._label=Label(self,text="Adwaith Jayan")
        self.grid()
        self._label.grid()

def main():
    LabelDemo().mainloop()

main()