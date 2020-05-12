
import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ks_2samp
import scipy
#n losowych wartości posortować
#zdefiniować odstępy
#posortować odstępy
#zliczanie równych liczb
#zebranie 1531 próbek z po 16 urodzin
#wyliczenie i przedstawienie rozkładu Poissona

k = 256
n = 16
y = [] #losowe wartości dla testu

with open('liczbylosowe.json') as plik:
    losowe_liczby = json.load(plik)

def getJ(k, n, y):
    print(y)
    y.sort()
    #print(y)
    Y = []
    Y.append(y[0])
    for i in range(1, len(y)):
        Y.append(y[i] - y[i-1])
    #print(Y)
    Y.sort()
    #print(Y)
    J = 0
    for i in range(1, len(Y)):
        if (Y[i] - Y[i-1]) == 0:
            J += 1
    print(J)
    return J

licznik_J = []



for i in range(16,len(losowe_liczby),16):
    y = losowe_liczby[i-16:i]
    licznik_J.append(getJ(k, n, y))

hist = []
for h in range(0,16):
    hist.append(licznik_J.count(h)/1561)
x = np.arange(16)
plt.title("Rozklad Poissona dla 4")
plt.ylabel("Czestotliwosc wystepowania")
plt.xlabel("Wartosc")
s = np.random.poisson(4, 1561)

plt.hist(s,color=(0,0,0))
plt.show()
plt.bar(x,hist,width=1,color=(0,0,0))
plt.show()
print(licznik_J)
print(len(licznik_J))

test = []

for i in range(100):
    s = np.random.poisson(4,1561)
    test.append(ks_2samp(hist, s))

print(test)
