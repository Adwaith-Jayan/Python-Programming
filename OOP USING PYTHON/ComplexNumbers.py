class Complex():
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def __str__(self):
        return str(self.real) + "+" + str(self.imag) + "i"
    
    def __add__(self,other):
        real=self.real+ other.real
        imag=self.imag + other.imag
        return Complex(real,imag)
    
    def __mul__(self,other):
        real=self.real * other.real + self.imag * other.imag * -1
        imag=self.real * other.imag + self.imag * other.real
        return Complex(real,imag)

c1=Complex(3,4)
c2=Complex(2,5)
print(c1,c2)
print(c1 + c2)
print(c1 * c2)