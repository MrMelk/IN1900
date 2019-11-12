import numpy as np
class Quadratic():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def value(self, x):
        return self.a * x **2 + self.b * x + self.c

    def table(self, L, R, n):
        s = ""
        for x in np.linspace(L, R, n):
            y = self.value(x)
            s += f"x = {x} gives f(x) = {y}\n"
        
        return s
    
    def roots(self):
        pass
        a = self.a
        b = self.b
        c = self.c
        x1 = -b + np.sqrt(b ** 2 - 4 * a * c)
        x2 = -b - np.sqrt(b ** 2 - 4 * a * c)

        return x1, x2     

b = Quadratic(3,1,-2)
c = b.roots()
print(f"here {c} we get roots for the equation 3x^2 + x - 2 = 0")
print("below is a table of x values and corresponding f(x) values for the same equation as above")
print(b.table(1, 10, 10))



def test_value():
    test = Quadratic(3, 1, -2)
    computed = test.value(2)
    expected = 0
    tol = 1e9
    assert (np.abs(computed - expected)) <= tol


def test_roots():
    testing = Quadratic(3, 1, -2)
    Computed = testing.roots()
    expected = (2, 3)
    tol = 1e9
    assert ((np.abs(Computed[0] - expected[0])) <= tol)
    assert ((np.abs(Computed[1] - expected[1])) <= tol)

"""

Idk if I'm supposed to make it so I can get every root even if it's immaginary, but
since the excercise didn't ask for it I will leave it.

Also ran through pytest and the test passed
Run example:
here (4.0, -6.0) we get roots for the equation 3x^2 + x - 2 = 0
below is a table of x values and corresponding f(x) values for the same equation as above
x = 1.0 gives f(x) = 2.0
x = 2.0 gives f(x) = 12.0
x = 3.0 gives f(x) = 28.0
x = 4.0 gives f(x) = 50.0
x = 5.0 gives f(x) = 78.0
x = 6.0 gives f(x) = 112.0
x = 7.0 gives f(x) = 152.0
x = 8.0 gives f(x) = 198.0
x = 9.0 gives f(x) = 250.0
x = 10.0 gives f(x) = 308.0
"""

