import random

f=open("ember.txt","r",encoding="utf-8")
nevek = []
for elem in f:
    print(elem)
    nevek.append(elem.strip().split("\n"))
f.close()
print(nevek)
sorsolt=[]
for a in range(2):
    sorsolt.append(str(random.choice(nevek)))

f=open("sorsolt.txt","r",encoding="utf-8")
het=[]
for elem in f:
    print(elem)
    het.append(elem.strip().split("\n"))
f.close()

f=open("sorsolt.txt","w",encoding="utf-8")
for i in range(len(sorsolt)):
    f.write(str(sorsolt[i])+"\n")
print(het)
het[2]=int(het[2][0])+1
f.write(str(het[2]))

f.close()