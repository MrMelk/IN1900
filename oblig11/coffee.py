import numpy as np
import matplotlib.pyplot as plt
from ODESolver import ForwardEuler

class Problem:
    def __init__(self, h, T_s):
        self.h = h
        self.T_s = T_s

    def __call__(self, T, t):
        dTdt = -self.h*(T - self.T_s)
        return dTdt
    
    def terminate(self, u, t, end_point):
        tol = self.T_s *0.01
        return np.abs(u[end_point] - self.T_s) < tol

#dTdt = 

def estimate_h(t1, Ts, T0, T1):
    pass
    h = (T1 - T0)/(t1*(Ts - T0))
    return h


if __name__ == "__main__":
    def test_Problem():
        h = estimate_h(15, 20, 95, 92)
        swaggyBoi = Problem(h, 20)
        bruh = ForwardEuler(swaggyBoi)
        tp = (0, 15)
        bruh.set_initial_condition(95)
        u, t = bruh.solve(tp)
        swaggyBoi.terminate(u, t, len(u)-1)
        tol = 1e-6
        expected = 92
        computed = u[1]
        print(np.abs(expected- computed))
        assert np.abs(expected - computed) < tol



    test_Problem()

    tp = np.linspace(0, 60*60, 60*5)

    kaffe_h = estimate_h(15, 20, 95, 92)


    for i in [20, 25]:
        kaffelaffe = Problem(kaffe_h, i)
        kaffelaffedaffe = ForwardEuler(kaffelaffe)
        kaffelaffedaffe.set_initial_condition(95)
        u, t = kaffelaffedaffe.solve(tp, terminate = kaffelaffe.terminate)
        plt.plot(t, u, label = f"Ts = {i}", ls = "--")
    
    plt.legend()
    plt.xlabel("t[s]")
    plt.ylabel("u(t)")
    plt.show()




"""
From calling the test function I see that we get a timetable, I see that I was off by a little bit
when thinking what time and decrease would be appropriate. Would prefferto use pytest to test though.
I don't know if my test is good enough, because in my mind the test is returning true, with it running terminate
at the end points and therefore it working. Is there a way to improve it?


from running this I get the plot with them converging and I have managed to get it to terminate soon(TM)


"""