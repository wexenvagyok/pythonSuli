import random
import string

def get_random_string(hossz):
    betuk = string.ascii_lowercase
    eredmeny = ''.join(random.choice(betuk) for i in range(hossz))
    print("*"*80)
    print("Véletlenszerű ötbetűs:", eredmeny)
    print("*"*80)
get_random_string(5)