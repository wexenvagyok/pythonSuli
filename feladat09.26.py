print("Első feladat")

szam = input("adj meg egy számot: ")

# A bekért szám kiíratása
print("A megadott szám:", szam)

print("Második feladat")

# Két szám bekérése
sz1 = float(input("adj meg egy első számot: "))
sz2 = float(input("adj meg egy második számot: "))

# Különbség kiszámítása és kiírása
kulonbseg = 1 - 2
print("A két szám különbsége:", kulonbseg)


print("Harmadik feladat")

# Két tizedestört szám bekérése
t1 = float(input("adj meg egy első tizedestört számot: "))
t2 = float(input("adj meg egy második tizedestört számot: "))

# Szorzat kiszámítása és kiírása
szorzat = t1 * t2
print("A két tizedestört szám szorzata:", szorzat)

print("Negyedik feladat")

# Két szám bekérése
sz1 = float(input("Kérlek adj meg egy első számot: "))
sz2 = float(input("Kérlek adj meg egy második számot: "))

# A nagyobb szám kiválasztása
nsz = max(sz1, sz2)

# A nagyobb szám kiírása
print("A két szám közül a nagyobb:", nsz)

print("Ötödik feladat")

# Két szám bekérése
sz1 = float(input(" adj meg egy első számot: "))
sz2 = float(input(" adj meg egy második számot: "))

# Ellenőrzés, hogy a második szám nem nulla
if sz2 != 0:
    t = f"{sz1} / {sz2} = {sz1 / sz2}"
    print(t)
else:
    print("A második szám nulla, nem lehet osztani.")

print("Hatodik feladat")

# Két szám bekérése
sz1 = int(input("adj meg egy alsó határt: "))
sz2 = int(input("adj meg egy felső határt: "))

# Számok kiírása az intervallumban
for i in range(sz1, sz2):
    print(i, end=' ')
    
print()  # Írjunk ki egy üres sort hogy olvashatóbb legyen

print("Hetedik feladat")

# Két szám bekérése
sz1 = int(input(" adj meg egy alsó határt: "))
sz2 = int(input(" adj meg egy felső határt: "))

# Számok kiírása az intervallumban
print(f"Az intervallum: [{sz1}, {sz2}]")
for i in range(sz1, sz2 + 1):
    print(i, end=' ')
    
print()  # Írjunk ki egy üres sort a jobb olvashatóság érdekében

print("Nyócadik feladat")

# Két szám bekérése
sz1 = int(input(" adj meg egy alsó határt: "))
sz2 = int(input(" adj meg egy felső határt: "))

# Számok négyzetének kiírása két oszlopban az intervallumban
print(f"Az intervallum: [{sz1}, {sz2}]")
for i in range(sz1, sz2 + 1):
    n = i ** 2
    print(f"{i} négyzete: {n}", end='\t')
    if (i - sz1 + 1) % 2 == 0:
        print()  # Új sor minden második szám után

print()  # Írjunk ki egy üres sort a jobb olvashatóság érdekében

print("Kielencedik feladat")

# Három szám bekérése
sz1 = float(input(" adj meg egy első számot: "))
sz2 = float(input(" adj meg egy második számot: "))
sz3 = float(input(" adj meg egy harmadik számot: "))

# A legnagyobb szám kiválasztása
lsz = max(sz1, sz2, sz3)

# A legnagyobb szám kiírása
print("A három szám közül a legnagyobb:", lsz)

print("Tizedik feladat")

# Két szám bekérése
sz1 = int(input("adj meg egy alsó határt: "))
sz2 = int(input(" adj meg egy felső határt: "))

# Páros számok kiírása az intervallumban
print(f"A páros számok az intervallumban [{sz1}, {sz2}]:")
for sz in range(sz1, sz2 + 1):
    if sz % 2 == 0:
        print(sz, end=' ')
    
print()  # Írjunk ki egy üres sort a jobb olvashatóság érdekében

print("Tizenegyedik feladat")

# Két szám bekérése
sz1 = int(input(" adj meg egy alsó határt: "))
sz2 = int(input(" adj meg egy felső határt: "))

# 5-tel osztható számok kiírása az intervallumban
print(f"A 5-tel osztható számok az intervallumban [{sz1}, {sz2}]:")
for sz in range(sz1, sz2 + 1):
    if sz % 5 == 0:
        print(sz, end=' ')
    
print()  # Írjunk ki egy üres sort a jobb olvashatóság érdekében

print("tizenkeddeik feladat")

# Szám bekérése 
sz = int(input(" adj meg egy maximum kétjegyű számot: "))

# Kétjegyűség ellenőrzése
if 10 <= sz <= 99:
    print("A megadott szám kétjegyű.")
else:
    print("A megadott szám nem kétjegyű.")

print("13. feladat")

# Szám bekérése
sz = int(input("adj meg egy háromjegyű pozitív számot: "))

# Háromjegyűség és pozitivitás ellenőrzése
if 100 <= sz <= 999:
    print("A megadott szám háromjegyű és pozitív.")
else:
    print("A megadott szám nem felel meg a követelményeknek.")

print("14. feladat")

# Szám bekérése 
sz = int(input(" adj meg egy maximum kétjegyű számot: "))

# Kétjegyűség ellenőrzése
if -99 <= sz <= 99:
    print("A megadott szám maximum kétjegyű.")
else:
    print("A megadott szám nem felel meg a követelményeknek.")

print("15. feladat")

# Szám bekérése
sz = int(input("Kérlek adj meg egy háromjegyű számot (pozitív vagy negatív): "))

# Háromjegyűség ellenőrzése
if -999 <= sz <= 999:
    print("A megadott szám háromjegyű.")
else:
    print("A megadott szám nem felel meg a követelményeknek.")

print("Done")







