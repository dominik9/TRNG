#zamiana na 256 bitową liczbę i pobranie 8 bitowych wartości
#wygenerowanie całego wykresu
import json
from struct import pack, unpack
import numpy
import matplotlib.pyplot as plt
import scipy.stats as sp

file = open('step3.json')
data = json.load(file)
file.close()

data_out = []

def getOne256bitNum(num):
    fs = pack('d', num[0][0])
    bval = unpack('Q', fs)
    #print(bin(bval[0])[9:49])
    num_bin = bin(bval[0])[10:50]
    fs = pack('d', num[0][1])
    bval = unpack('Q', fs)
    num_bin =  num_bin + bin(bval[0])[10:50]
    #print(num_bin)
    fs = pack('d', num[1][0])
    bval = unpack('Q', fs)
    num_bin = num_bin + bin(bval[0])[10:58]
    #print(num_bin)
    fs = pack('d', num[1][1])
    bval = unpack('Q', fs)
    num_bin = num_bin + bin(bval[0])[10:58]
    #print(num_bin)
    fs = pack('d', num[2][0])
    bval = unpack('Q', fs)
    num_bin = num_bin + bin(bval[0])[10:50]
    #print(num_bin)
    fs = pack('d', num[2][1])
    bval = unpack('Q', fs)
    num_bin = num_bin + bin(bval[0])[10:50]
    print(num_bin)
    data_out.append(num_bin)

for i in range(len(data)):
    getOne256bitNum(data[i])

transform8bit = []
for i in data_out:
    for j in range(32):
        transform8bit.append(int(i[j*8:j*8+8],2))

hist = []
for h in range(0,255+1):
    hist.append(transform8bit.count(h)/len(transform8bit))

x = numpy.arange(256)
plt.title("Empirczny rozkład zmiennych losowych po post-procesingu")
plt.ylabel("Czestotliwosc wystepowania")
plt.xlabel("Wartosc")
plt.bar(x,hist,width=1,color=(0,0,0))

plt.show()
plt.plot(hist)
plt.show()
entropy = sp.entropy(hist, base=2)
print(entropy)


