# Dolgozat megoldásai:
#Készíts egy listát, ami 500 db 5 jegyű számot tartalmaz véletlenszerűen
import random

szamok = []

for a in range(500):
    veletlenSzam = random.randint(10000, 99999)
    szamok.append(veletlenSzam)

#Készíts egy függvényt, ami visszaadja a páros számokat
def parosSzamok(szamok):
    paros = 0
    for b in szamok:
        if b % 2 == 0:
            paros += 1
    return paros

eredmeny =  parosSzamok(szamok)
print(eredmeny,"darab páros szám van a listában.")

#Számold ki a páratlan számok összegét
def paratlanSzam(szamok):
    paratlan = 0
    for c in szamok:
        if c % 2 != 0:
            paratlan += c
    return paratlan

eredmeny = paratlanSzam(szamok)
print(eredmeny,"a páratlan számok összege.")

#Az első vagy a második fele nagyobb összeadásnál?
def osszegSzamitas(szamok):
    darabszam = len(szamok)
    osztas = darabszam // 2

    elsoFel = sum(szamok[:osztas])
    masodikFel = sum(szamok[osztas:])

    return elsoFel, masodikFel

elsoFel, masodikFel = osszegSzamitas(szamok)

if elsoFel > masodikFel:
    print("Az első felének az összege nagyobb.")
elif elsoFel < masodikFel:
    print("A második felének az összege nagyobb.")
else:
    print("A mindkét oldal összege  megegyezik.")