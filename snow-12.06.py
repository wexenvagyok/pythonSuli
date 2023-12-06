import random

maxWidth=80
maxHeight=25

minFlakes=0
maxFlakes=5

rows=[]
for _ in range(maxHeight):
    actFlakes=random.randint(minFlakes,maxFlakes)
    actRow=" "*maxWidth

    flakes=random.sample(range(0,maxWidth),actFlakes)

    for i in flakes:
        actRow=actRow[:i]+"*"+actRow[i+1:]
    rows.append(actRow)
print("\n".join(rows))
 
#actRow=str(list=(actRow))
#temp=[5]="@"

#actRow="".join(temp)

#HÁZI FELADAT: 1. Legyen több féle hópehely, 2. Fájlba iratás