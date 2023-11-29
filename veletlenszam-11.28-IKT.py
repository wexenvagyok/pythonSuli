print("Szia világ")
import random
import math
#Véletlenszám generálása
#Lépés, darab, eltolás

#ceil -> felfelé kerekítés
#[0;10[ -> 10

def veletlen(mettol, meddig, lepes=1):
	darab = math.ceil((meddig-mettol)/lepes)
	eltolas = mettol
    
	szam = math.floor(random.random()*darab)*lepes+eltolas
	return szam

print(veletlen(10, 20))
szamok=[]
for i in range(100):
	szamok.append(veletlen(10,20))

print(szamok)

#masodik feladat
#készítsetek egy listát, ami véletlenszerű darabszámú, 10-20-ig tartalmaz listákat, ezek a listák tartalmazzanak 10-20 közötti testmagasságokat
#magasság 160-200 között
szamok=[]
r=veletlen(10,21)
for _ in range(r):
	r2=veletlen(10,21)
	temp=[]
	for _ in range(r2):
		temp.append(veletlen(160,201))
		szamok.append(temp)
print("Második f:")
print(szamok)

szamok=[[]]

#Házi feladat: Egy nyári nap hőmérséklet adatait készítsétek el öt különböző Mo.-i városban véletlenszerűen, óránkénti bontásban
#+ figyeljünk a napszakra