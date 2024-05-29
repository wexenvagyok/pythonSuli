#kérjetek be számokat, pozitiv negativ 0 végjelig 
szamLista = []

bekert = 1
i = 0

while True: 
    bekert = int(input("Adj meg egy számot: "))
    i = bekert + i
    if bekert == 0:
        print("A bekérés lezárult.")
        break
    if bekert / bekert:
        szamLista.append(bekert)

print(szamLista)

#osszeadas = sum(szamLista)
#print(f"A számok összeadva: {osszeadas}")
    
#összegezzétek a pozitiv és negativ számokat

#Melyik van távolabb a nullától?

#A lista első felében melyik számból volt több? + vagy - ha páratlan akkor az első fele legyen nagyobb