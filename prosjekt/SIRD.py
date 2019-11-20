import numpy as np
import matplotlib.pyplot as plt
from ODESolver import RungeKutta4

class Region:
    def __init__(self, name, S0, I0, R0, D0):
        self.name = name
        self.S0 = S0
        self.I0 = I0
        self.R0 = R0
        self.D0 = D0
        self.population = S0 + I0 + R0 - D0

    
    def set_SIRD_values(self, u, t):
        """self.S = u[0]
        self.I = u[1]
        self.R = u[2]
        self.D = u[3]
        self.t = t
        """
        self.S = []
        self.I = []
        self.R = []
        self.D = []
        for i in range(len(u)):
            self.S.append(u[i][0])
            self.I.append(u[i][1])
            self.R.append(u[i][2])
            self.D.append(u[i][3])
        self.S = np.array(self.S)
        self.I = np.array(self.I)
        self.R = np.array(self.R)
        self.D = np.array(self.D)

        self.t = t
        
        #Fikse dette med en løkke? skal jeg returne verdier? mest sannsynlig? nei skal jo plotte i denne klassen

    
    def plot(self, x_label):
        plt.title(self.name)
        plt.plot(self.t, self.S, label = "Susceptible", color = "Blue")
        plt.plot(self.t, self.I, label = "Infected", color = "Green")
        plt.plot(self.t, self.R, label = "Immune", color = "Yellow")
        plt.plot(self.t, self.D, label = "Deceased", color = "Black")
        plt.xlabel(x_label)
        plt.ylabel("Population")


class ProblemSIRD:
    def __init__(self, region, alpha, beta, gamma):
        self.region = region
        self.alpha = self.wrap_as_function(alpha)
        self.beta = self.wrap_as_function(beta)
        self.gamma = self.wrap_as_function(gamma)

        self.set_initial_condition()
    
    def wrap_as_function(self, arg):
        if isinstance(arg, (float, int)):
            return lambda t: arg
        elif callable(arg):
            return arg

    
    def set_initial_condition(self):
        self.S0 = self.region.S0
        self.I0 = self.region.I0
        self.R0 = self.region.R0
        self.D0 = self.region.D0
        self.U0 = (self.S0, self.I0, self.R0, self.D0)
    
    def get_population(self):
        population = self.region.population
        return population
    
    def solution(self, u, t):
        self.region.set_SIRD_values(u, t)
    
    def __call__(self, u, t):
        """
        S0 = self.S0
        I0 = self.I0
        R0 = self.R0
        D0 = self.D0
        """
        S0 = u[0]
        I0 = u[1]
        R0 = u[2]
        D0 = u[3]
        alpha = self.alpha(t)
        beta = self.beta(t)
        gamma = self.gamma(t)
        ds = (-1) * alpha*S0*I0
        di = alpha*S0*I0 - beta*I0 - gamma*I0
        dr = beta*I0
        dd = gamma*I0
        return(ds, di, dr, dd)

class SolverSIRD:
    def __init__(self, problem, T, dt):
        self.problem = problem
        self.T = T
        self.dt = dt
        self.total_population = problem.get_population()
        #print(self.total_population)
        self.t = np.linspace(0, self.T, self.T/self.dt)
    
    def terminate(self, u, t, k):#k er tidsstek mah BOI/GRILL
        u_k = u[k, :]
        #u_k_minus_1 = u[k-1, :]
        test = np.abs(self.total_population - np.sum(u_k))#np.sum(u_k_minus_1)
        tol = 1e-9

        msg = "They aint the same bro. THEY AINT THE SAME"
        if test < tol:
            return False
        else:
            print(msg)
            return True

    def solve(self, method = None):
        
        if not method:
            method = RungeKutta4
        print(method)
        print(RungeKutta4)
        solver = method(self.problem)
        solver.set_initial_condition(self.problem.U0)
        
        u, t = solver.solve(self.t)#, self.terminate)
        self.problem.solution(u, t)

if __name__ == "__main__":
    #U0 = (7000, 30, 0, 0)
    alpha = 6.5e-5
    beta = 0.1/4
    gamma = 0.9/4

    Adventure_Land = Region("Adventure Land",7000, 30, 0, 0)

    Adventure_Land_Disease = ProblemSIRD(Adventure_Land, alpha, beta, gamma)

    Adventure_Land_Solution = SolverSIRD(Adventure_Land_Disease, 63, 1)
    Adventure_Land_Solution.solve()

    Adventure_Land_Solution.problem.region.plot("TIME MAFAKKA")


    plt.legend()
    plt.show()
