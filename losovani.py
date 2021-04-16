from Hmm import hmm
import random

def randindex(max_number: int):
    random_index = random.randrange(0, max_number)
    return random_index
def los_jmena():
    jmeno = jmena[randindex(pocet_jmen)]
    hmm.print_without_end_line(jmeno + " má téma: ")
def los_temata():
    tema = temata[randindex(pocet_temat)]
    hmm.print_without_end_line(tema)

jmena = []
temata = []

while True:
    idk = input("Zadejte jméno, ukončete slovem konec")
    if idk.lower() == "konec":
        break
    jmena.append(idk)
while True:
    idk = input("Zadejte téma, ukončete slovem konec")
    if idk.lower() == "konec" and len(temata) > 0:
        break
    temata.append(idk)

pocet_jmen = len(jmena)
pocet_temat = len(temata)

los_jmena()
los_temata()
print(",")
los_jmena()
los_temata()









