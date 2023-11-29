#12 fős osztály, 1 évben kap 8-12db jegyet, jegyek 1-5-ig
import random

jegyek=[]
for i in range(12):
	egyDiak=[]
	for l in range(random.randrange(8, 13)):
		jegy=random.range(1, 6)
		egyDiak.append(jegy)
	jegyek.append(egyDiak)
#Jegyek generálása 
random.randint(8, 12)
random.randint(1, 5)