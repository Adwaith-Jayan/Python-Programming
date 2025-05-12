from tkinter import *
from datetime import *

class DOB(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.geometry("200x200")
        self.grid()
        self._labelAge=Label(self,text="AGE:")
        self._labelAge.grid(row=2,column=0)
        self._labelDOB=Label(self,text="DOB:")
        self._labelDOB.grid(row=0,column=0)

        self._dobVar=StringVar()
        self._ageVar=IntVar()
        self._dobEntry=Entry(self,textvariable=self._dobVar)
        self._dobEntry.grid(row=0,column=1)
        self._ageEntry=Entry(self,textvariable=self._ageVar)
        self._ageEntry.grid(row=2,column=1)

        self._but=Button(self,text="Submit",command=self._findAge)
        self._but.grid(row=3,column=2,columnspan=2)

    def _findAge(self):
        dt=datetime.strptime(self._dobVar.get(),"%d-%m-%Y")
        td=datetime.today()
        delta=td-dt

        age=delta.days//365

        self._ageVar.set(age)

DOB().mainloop()