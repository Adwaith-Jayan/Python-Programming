class Rational():
    def __init__(self,num,denom):
        self._num=num
        self._denom=denom
        self._reduce()
    
    def numerator(self):
        return self._num
    
    def denominator(self):
        return self._denom
    
    def __str__(self):
        return str(self._num).rstrip('0').rstrip('.') + " / " + str(self._denom).rstrip('0').rstrip('.')
    
    def _reduce(self):
        divisor=self._gcd(self._num,self._denom)
        self._num/=divisor
        self._denom/=divisor
    
    def _gcd(self,a,b):
        (a,b)=(max(a,b),min(a,b))
        while b>0:
            a,b=b,a%b
        return a
    
    #Arithmetic Operations

    def __add__(self,other):
        _n=self._num * other._denom + other._num * self._denom
        _d= self._denom * other._denom
        return Rational(_n,_d)

    def __lt__(self,other):
        extremes=self._num * other._denom
        mean=self._denom * other._num
        return extremes < mean
    
    def __gt__(self,other):
        extremes=self._num * other._denom
        mean=self._denom * other._num
        return extremes > mean
    
    def __eq__(self,other):
        if self is other:
            return True
        elif (type(self) != type(other)):
            return False
        else:
            if self._num==other._num and self._denom == other._denom:
                return True
            else:
                return False




r1=Rational(5,2)
print(r1)
r2=Rational(2,4)
print(r2)
print(r1==r1)