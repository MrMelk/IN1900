import numpy as np

class F():
    def __init__(self, a = 1.0, w = 0.1):
        self.a = a
        self.w = w
    def value(self, x):
        pass
        a = self.a
        w = self.w
        return np.exp(-a * x) * np.sin(w * x)

#f = lambda x, a, w: np.exp(-a * x) * np.sin(w * x)

f = F()
print(f.value(np.pi))

f.a = 2
print(f.value(np.pi))

"""
Run example:
0.01335383513703555
0.0005770715401197441
"""