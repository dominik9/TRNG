import json
import numpy
import matplotlib.pyplot as plt
import scipy.stats as sp

mouse_list_file = []
num_list = []
realNum_list = []

with open('plik.json') as plik:
    mouse_list_file = json.load(plik)

#with open('bin.bin') as bin_file:
out_bin_to_save = 0

for i in range(len(mouse_list_file)-1):
    if mouse_list_file[i][0] == mouse_list_file[i+1][0]:
        o = numpy.pi/2
    else:
        o = numpy.arctan(numpy.absolute((mouse_list_file[i+1][1]-mouse_list_file[i][1])/(mouse_list_file[i+1][0]-mouse_list_file[i][0])))
    r = o/(numpy.pi/2)
    realNum_list.append(r)
    num_list.append(int(r*255))

hist = []
for h in range(0,255+1):
    hist.append(num_list.count(h)/99999)

x = numpy.arange(256)
plt.title("Empirczny rozkład zmiennych losowych generowanych przez ruch myszy")
plt.ylabel("Czestotliwosc wystepowania")
plt.xlabel("Wartosc")
plt.bar(x,hist,width=1,color=(0,0,0))

plt.show()
plt.plot(hist)
plt.show()
entropy = sp.entropy(hist, base=2)
print(entropy)
with open('mouse22.json','w') as file:
    json.dump(num_list,file)

with open('real_num.json','w') as real_file:
    json.dump(realNum_list, real_file)
