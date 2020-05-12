import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chisquare
#pobrać pięć bajtow
#do kazdego bajtu przypisac litere
#utworzyc slowo
#wyznaczyc ilosc powtarzajacych sie slow
#test chi-kwadrat


with open('liczbylosowe.json') as plik:
    losowe_liczby = json.load(plik)

def getlitera(liczba):
    ile = 0
    for i in range(8):
        b = (liczba >> i) & 1
        if b == 1:
            ile += 1
    if ile <= 2:
        return "A"
    elif ile == 3:
        return "B"
    elif ile == 4:
        return "C"
    elif ile == 5:
        return "D"
    elif ile >= 6:
        return "E"

def getslowo(liczby):
    slowo = ""
    for i in range(5):
        slowo = slowo + getlitera(liczby[i])
    return slowo

slowa = []
for i in range(5,15630,5):
    slowa.append(getslowo(losowe_liczby[i-5:i]))


lista_znakow = ["A", "B", "C", "D", "E"]

zliczanie_slow = []
for i_0 in lista_znakow:
    for i_1 in lista_znakow:
        for i_2 in lista_znakow:
            for i_3 in lista_znakow:
                for i_4 in lista_znakow:
                    slowo_do_zliczenia = i_0 + i_1 + i_2 + i_3 + i_4
                    #print(slowo_do_zliczenia)
                    zliczanie_slow.append(slowa.count(slowo_do_zliczenia))

print(zliczanie_slow)
print(len(zliczanie_slow))
hist = []
for h in range(0,10):
    hist.append(zliczanie_slow.count(h)/3125)
add = 0
for i in zliczanie_slow:
    add = add + i
print(add)
x = np.arange(10)
plt.title("Rozkład zliczeń ")
plt.ylabel("Czestotliwosc wystepowania")
plt.xlabel("Wartosc")
plt.bar(x,hist,width=1,color=(0,0,0))
plt.show()

z = chisquare(zliczanie_slow,f_exp=1)
print(z)