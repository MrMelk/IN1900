import numpy as np
import matplotlib.pyplot as plt

def f(u, t):
    dudt = u/10
    return dudt

#initial condistions
u0 = 0.2

#derivative of u
u_deriv = u0/10

#time
t = np.linspace(0, 20)
T = 20
#steps
dt = 5
n = 200

class ForwardEuler_v1():
    def __init__(self, f, U0, T, n):
        self.f, self.U0, self.T, self.n = f, U0, T, n
        self.dt = T/float(n)
        self.u = np.zeros(n+1)
        self.t = np.zeros(n+1)
    def solve(self):
        """Compute solution for 0 <= t <= T."""
        self.u[0] = float(self.U0)
        self.t[0] = float(0)
        for k in range(self.n):
            self.k = k
            self.t[k+1] = self.t[k] + self.dt
            self.u[k+1] = self.advance()
        return self.u, self.t
    def advance(self):
        """Advance the solution one time step."""
        u, dt, f, k, t = \
        self.u, self.dt, self.f, self.k, self.t
        u_new = u[k] + dt*f(u[k], t[k])
        return u_new

def analytic(t):
    anal = np.zeros(len(t))
    for i in range(len(t)):
        anal[i] = 0.2 * np.exp(0.1*t[i])
    return anal



lei_av_samme_type_oppgave_igjen_og_igjen_as_blir_litt_ensformig = ForwardEuler_v1(f, u0, T, 10)
uwu2 = lei_av_samme_type_oppgave_igjen_og_igjen_as_blir_litt_ensformig.solve()
hvorfor_kopierer_vi_bare_kode_det_er_mad_kjedelig = ForwardEuler_v1(f, u0, T, n)
uwu = hvorfor_kopierer_vi_bare_kode_det_er_mad_kjedelig.solve() #UwU er staalet fra Morten Berg siden det er morsomt med slike variabel navn
a = analytic(uwu[1])

plt.plot(uwu[1], a, label = "analytic")
plt.plot(uwu[1], uwu[0], label = f"n = {n}", ls = "--")
plt.plot(uwu2[1], uwu2[0], label = f" n = {10}", ls = "-.")
plt.show()

feuc_u = uwu[0]
feuc_t = uwu[1]

f = open("ForwardEulerODE_Class.txt","w+")
f.write("U(t) t\n")
for i in range(n+1):
    f.write(f"{feuc_u[i]:.3f} {feuc_t[i]:.3f}\n")

"""
run example:
Testet med store og små tidssteg, gir samme resultat som simple_oDE_func.py

Måtte endre noe i koden siden den vi skulle kopiere siden den ga en error pga 
for faa ting i forste linjen av init var = for mange elementer

"""
