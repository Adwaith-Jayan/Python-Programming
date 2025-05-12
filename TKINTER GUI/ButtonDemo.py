from tkinter import *

class ButtonDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Button Demo")
        self._label=Label(self,text="WELCOME")
        self.grid()
        self._label.grid()
        self._button=Button(self, text="Click On Me", command=self._clicked)
        self._button.grid()

    def _clicked(self):
        if self._label["text"]== "WELCOME" :
            self._label["text"]= "BYE"
        else:
            self._label["text"]="WELCOME"

def main():
    ButtonDemo().mainloop()
main()