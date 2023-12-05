f=open("bela.txt","w")

#f.write("1")
for a in range(100):
    f.write(str(a)+"\n")
f.close()

#open("béla2.txt","w") "\n".join(range(100))

open("béla2.txt","w").write("\n".join([str(a) for a in range(100)]))

f=open("bela.txt","r")
#r (read) nem kötelező ^
lista=[]
for egySor in f:
    lista.append(egySor.strip())
f.close()
print(lista)

f=open("bela.txt","r")
lista=[egySor.strip() for egySor in f.readlines()]
f.close()
print(lista)

f=open("bela.txt","r")
lista2 = map(lambda x: x.strip(), f.readlines())
print(list(lista2)) 
f.close

lista=[]
f=open("bela.txt","r")
lista=f.read().strip().split("\n")
print(lista)
f.close()