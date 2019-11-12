import numpy as np

class Diff():
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)



class Forward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x))/h

class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h))/h

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return ((f(x - 2 * h) - 4 * f(x - h) + 3 * f(x))/(2 * h))

def g(x):
    return np.exp(-x)



def table(self, start, end, n):
        space = ""
        for x in np.linspace(start, end, n):
            g = self(x)
            s += "%12g %12g\n" % (x, y)
        return s


class Central2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)



for x in np.linspace(0,14,15):
    space = ""
    B1 = Backward1(g)
    B2 = Backward2(g)
    print(f"Backward1 = {B1(x)}, Backward2 = {B2(x)}, error: |B2 - B1| = {np.abs(B2(1) - B1(1))}")

"""
Run example:
Backward1 = -1.000005000006965, Backward2 = -0.9999999999621422, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.3678812805718578, Backward2 = -0.3678794411543506, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.13533595991377378, Backward2 = -0.13533528323006472, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.04978731730428953, Backward2 = -0.0497870683666135, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.018315730467358127, Backward2 = -0.018315638888183328, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.0067379806886758145, Backward2 = -0.006737946998437715, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.0024787645703811673, Backward2 = -0.0024787521763890846, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.0009118865249382358, Backward2 = -0.0009118819654452616, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.00033546430520600684, Backward2 = -0.00033546262785850983, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -0.00012341042113196091, Backward2 = -0.00012340980407455748, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -4.540015676092077e-05, Backward2 = -4.539992975880141e-05, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -1.670178429829779e-05, Backward2 = -1.6701700788980707e-05, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -6.144243074241074e-06, Backward2 = -6.144212352949e-06, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -2.2603407086087957e-06, Backward2 = -2.2603294068599387e-06, error: |B2 - B1| = 1.8394175071989594e-06
Backward1 = -8.315328767355208e-07, Backward2 = -8.315287190531234e-07, error: |B2 - B1| = 1.8394175071989594e-06

We can see the error is the same always, and also it's not too big, but big enough to not get a precise answer
"""
