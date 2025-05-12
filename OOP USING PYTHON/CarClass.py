class Car():
    def __init__(self,register_number,color,mileage,year):
        self.register_number=register_number
        self.color=color
        self.mileage=mileage
        self.year=year
    
    def __str__(self):
        data= self.register_number + "\n"
        data+= self.color + "\n"
        return data
    def setColor(self,color):
        self.color=color

c=Car("KLXXXXX","Black",25,2020)
print(c)        
c.setColor("Red")
print(c)