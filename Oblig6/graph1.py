import numpy as np
import matplotlib.pyplot as plt
praise_the_sun = np.linspace(0, 1, 100000)
def jeg_er_trott(tuppelupp1,tuppelupp2,t = praise_the_sun):
    
    swaggy_boy_jesus = t * tuppelupp1[0] + (1 - t) * tuppelupp2[0]
    swaggy_boy_judas = t * tuppelupp1[1] + (1 - t) * tuppelupp2[1]
    return (swaggy_boy_jesus, swaggy_boy_judas)


plt.plot(jeg_er_trott((1,1),(1,2))[0],jeg_er_trott((1,1),(1,2))[1], label = "VERTIKAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL")
plt.plot(jeg_er_trott((1,1),(2,1))[0],jeg_er_trott((1,1),(2,1))[1], label = "HORISONTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAL")
plt.legend()
plt.xlabel("OH LAWD HE COMIN (x-posisjon)")
plt.ylabel("HERE COME DAT BOI. OH SHIT WADDUP! (y-posisjon)")
plt.show()

"""
running example:
I get that gucci graph
"""
"""
I'm brutally tired and can't really get my head to do the b assignment.
To do it I would make a loop that would traverse a list of tuples of points and plot them.
"""