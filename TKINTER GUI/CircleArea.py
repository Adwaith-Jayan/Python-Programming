from tkinter import *
from tkinter import messagebox
import math

class CircleArea(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Circle Area")
        self.grid()
        self._labelRadius=Label(self,text="Radius:" )
        self._labelArea=Label(self,text="Area: ")
        self._labelRadius.grid(row=1,column=0)

        self._radius=DoubleVar()
        self._radiusEntry=Entry(self, justify="center",textvariable=self._radius)
        self._radiusEntry.bind("<KeyPress-Return>",self._enter)
        self._radiusEntry.grid(row=1,column=1)

        self._areaVar=DoubleVar()
        self._areaEntry=Entry(self,textvariable=self._areaVar,state="readonly")
        self._labelArea.grid(row=2,column=0)
        self._areaEntry.grid(row=2,column=1)

        self._CalcButton=Button(self,text="Calculate",command=self.FindArea)
        self._CalcButton.grid(row=4,column=1,columnspan=3,rowspan=2)

    def FindArea(self):
        try:
            r=self._radius.get()
            area=math.pi * (r**2)
            self._areaVar.set(area)
        except Exception:
            messagebox.showerror(title="ERROR",message="Invalid Input", parent=self)
    
    def _enter(self,event):
        """Event Handler to Display Output(area) when enter is clicked"""
        self.FindArea()
        

CircleArea().mainloop()

