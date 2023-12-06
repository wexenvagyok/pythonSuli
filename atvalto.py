# mértékegység átváltó
# wexen 2023.10.06.
# projektfeladat

tipusok=["Hosszúság","Terület","Térfogat","Tömeg","Űrmérték","Űrmérték és térfogat"]
egysegek=[["mm","cm","dm","m","km"],
          ["mm2","cm2","dm2","m2","km2"],
          ["mm3","cm3","dm3","m3","km3"]]

valtok=[[10,10,10,1000,1],
            [100,100,100,100000,1],
            [1000,1000,1000000000],
            [],
            []]

print("===============MENÜ===============")
#for elem in tipusok:
#   print (elem)

for i,elem in enumerate(tipusok):
    print ("\t"+str(i+1)+".",elem)

print ("\t0. Kilépés")
print("===============MENÜ===============")

tipusId="alma"
while tipusId=="alma" or tipusId not in range(len(tipusok)+1):
    try:
        tipusId=int(input("Válassz a listából:"))
        if tipusId not in range(len(tipusok)+1):
            raise
    except:
        print("Nem sikerült..")

egysegId2="alma"
print("Típus:",tipusok[tipusId])
print("Mértékegységek:")

for i,elem in enumerate(egysegek[egysegId]):
    print ("\t"+str(i+1)+":",elem)


print ("\t0. Vissza")

while egysegId=="alma" or tipusId not in range(len(egysegek[tipusId])+1):
    try:
        egysegId=int(input("Válassz a listából:"))
        if egysegId not in range(len(tipusok)+1):
            raise
    except:
        print("Nem sikerült..")
