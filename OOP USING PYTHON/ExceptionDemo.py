"""ExceptionDemo.py creates a user defined exception 
that raises error when the age entred is below 18
"""
class AgeError(Exception):
    def __init__(self,age,message=" Age should not be less than 18"):
        self.age=age
        self.message=message
        super().__init__(self.message)


a=int(input("Enter Age:"))
if a<18:
    raise AgeError(a)