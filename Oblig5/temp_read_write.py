import numpy as np


#a
def extract_data(filename):
    file = open(filename, "r")
    newlist = []
    stats = file.readlines()[1:]

    for line in stats:
        splitting = line.split()
        newlist.extend(splitting)
    
    return newlist
#b
oct_1945 = extract_data("temp_oct_1945.dat")
oct_1945 = list(map(float, oct_1945))
oct_2014 = extract_data("temp_oct_2014.dat")
oct_2014 = list(map(float, oct_2014))


mean_1945 = np.mean(oct_1945)
mean_2014 = np.mean(oct_2014)
max_1945 = np.max(oct_1945)
max_2014 = np.max(oct_2014)
min_1945 = np.min(oct_1945)
min_2014 = np.min(oct_2014)

print("mean1945 = ", mean_1945)
print("mean2014 = ", mean_2014)
print("min1945 = ", min_1945)
print("min2014 = ", min_2014)
print("max1945 = ", max_1945)
print("max2014 = ", max_2014)
#c

def write_formatting(filename, list1, list2):
    file = open(filename, "w")
    file.write("oct_1945:   oct_2014:\n")
    for i in range(len(list1)):
        file.write(f"{list1[i]}             {list2[i]}\n")
        #file.write("{:.f}       {:.f}".format(list1[i], list2[i]))
    file.close

write_formatting("temp_formatted.txt", oct_1945, oct_2014)


