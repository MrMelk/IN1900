import numpy as np

class Line():
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    
    def value(self, x):
        a = (self.p2[1] - self.p1[1])/float(self.p2[0] - self.p1[0])
        b = self.p2[1] - a * x
        return a + b



def test_Line():
    line = Line((0, -1), (2, 4))
    computed = line.value(0.5)
    expected = 0.25
    tol = 1e9
    assert (np.abs(computed - expected) <= tol)


"""
brukte pytest og fikk:

C:\Users\areto\Documents\Høst2019\IN1900\oblig9>pytest Line.py
================================================= test session starts =================================================
platform win32 -- Python 3.6.1, pytest-5.1.2, py-1.8.0, pluggy-0.12.0
rootdir: C:\Users\areto\Documents\Høst2019\IN1900\oblig9
plugins: cov-2.7.1
collected 1 item

Line.py .                                                                                                        [100%]

================================================== 1 passed in 0.37s ==================================================
"""