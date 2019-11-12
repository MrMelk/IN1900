import numpy as np

class Line():
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1
    def __call__(self, x):
        print("Calling Line...")
        return self.c0 + self.c1*x
    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ""
        for x in np.linspace(L, R, n):
            y = self(x)
            s += "%12g %12g\n" % (x, y)
        return s

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)
        self.c2 = c2
        
    def __call__(self, x):
        print("Calling Parabola...")
        return self.c2*x**2 + Line.__call__(self, x)

class Cubic(Parabola):
    def __init__(self, c0, c1 ,c2, c3,):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3
    def __call__(self, x):
        print("Calling Cubic...")
        return self.c3 * x **3 + Parabola.__call__(self, x)

class Poly4(Cubic):
    def __init__(self, c0, c1 ,c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4
    def __call__(self, x):
        print("calling Poly4")
        return self.c4 * x ** 4 + Cubic.__call__(self, x)

    



p = Poly4(1, 2, 3, 4, 5)
p_table = p.table(1,10,10)
print(p_table)

"""
Run example with the print statements
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
calling Poly4
Calling Cubic...
Calling Parabola...
Calling Line...
           1           15
           2          129
           3          547
           4         1593
           5         3711
           6         7465
           7        13539
           8        22737
           9        35983
          10        54321
"""