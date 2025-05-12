class Distance:
    def get_distance(self):
        val=int(input("Enter Distance in KM: "))
        self.dist=val
    
    def print_distance(self):
        return 1000 * self.dist

d=Distance()
d.get_distance()
print(d.print_distance() , "m")