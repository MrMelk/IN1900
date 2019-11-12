import numpy as np




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
    
this = Quadratic(int(input("a value = ")), int(input("b value = ")), int(input("c value = ")))
if this.roots() == ():
    print("Give me some real roots son")
else:
    print(this.roots())