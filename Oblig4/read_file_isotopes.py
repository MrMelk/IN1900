
file = open("Oxygen.txt", "r")
weight = []
Isotope = []
Natural_abundance = []
table = file.readlines()[1:]
for line in table:
    noe = line.split()
    weight.append(noe[1])
    Isotope.append(noe[0])
    Natural_abundance.append(noe[2])
for i in range(len(Isotope)):

    print("{:.4f}".format(float(weight[i])))
    print("{:.4f}".format(float(Natural_abundance[i])))
    print(Isotope[i])
    

