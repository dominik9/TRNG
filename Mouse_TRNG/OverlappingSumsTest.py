

import json
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sps
#zamiana liczb na 32 bitowe zmiennoprzecinkowe od 0 do 1 ok
#dodać po sto liczb
#porównać z rozkładem normalnym

with open('liczbylosowe.json') as plik:
    losowe_liczby = json.load(plik)

def getfloat(cztery_liczby):
    liczba32 = (cztery_liczby[0] << 24) | (cztery_liczby[1] << 16) | (cztery_liczby[2] << 8) | (cztery_liczby[3])
    float32liczba = (liczba32/(4294967296+1))
    return float32liczba

liczby_zmiennoprzecinkowe = []
for i in range(4,len(losowe_liczby),4):
    liczby_zmiennoprzecinkowe.append(getfloat(losowe_liczby[i-4:i]))

print(liczby_zmiennoprzecinkowe)

suma_100 = []
s = 0
for i in range(len(liczby_zmiennoprzecinkowe)):
    s = s + liczby_zmiennoprzecinkowe[i]
    if i%100 == 99:
        suma_100.append(s-50)
        s=0

print(suma_100)
print(len(suma_100))
plt.title("Rozkład sumy")
plt.ylabel("Suma")
plt.xlabel("Wartosc")
plt.hist(suma_100,color=(0,0,0))
plt.show()
print(sps.kstest(suma_100,'norm'))