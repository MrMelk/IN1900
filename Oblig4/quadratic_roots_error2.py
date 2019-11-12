import numpy as np
import sys as sys 



class Quadratic:
    def __init__(self,a_2,a_1,a_0):
        self.a_2 = a_2
        self.a_1 = a_1
        self.a_0 = a_0
        self.coeffs = a_2,a_1,a_0
    
    def __call__(self,x):
        a_2 = self.a_2
        a_1 = self.a_1
        a_0 = self.a_0
        f = (a_2*x**2 + a_1*x + a_0)
        return f

    def roots(self):
        
        a_2 = self.a_2
        a_1 = self.a_1
        a_0 = self.a_0
        x1 = (-a_1-np.sqrt(a_1**2 - 4*a_2*a_0))/(2*a_2)
        x2 = (-a_1+np.sqrt(a_1**2 - 4*a_2*a_0))/(2*a_2)
        
        if a_1**2 - 4*a_2*a_0 < 0:
           return ()
        elif x1==x2:
            return (x1,x1)
            
        else:
            return (x1,x2)

try:
    a = int(sys.argv[1])
except IndexError:
    a = int(input("give value for a: "))
try:
    b = int(sys.argv[2])
except IndexError:
    b = int(input("give value for b: "))
try:
    c = int(sys.argv[3])
except IndexError:
    c = int(input("give value for c: "))

this = Quadratic(a,b,c)


if this.roots() == ():
    raise ValueError("Gimme some real roots son")
else:
    print(this.roots())