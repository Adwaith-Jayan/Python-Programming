from tkinter import *

class ImageDemo(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Image Viewer")
        self.grid()
        self.label=Label(self,text="IMAGE VIEWER")
        self.label.grid()
        self.img=PhotoImage(file="pooh.gif")
        self.imgLabel=Label(self,image=self.img)
        self.imgLabel.grid()
        self.imageText=Label(self,text="Winnie The Pooh")
        self.imageText.grid()

def main():
    ImageDemo().mainloop()
main()