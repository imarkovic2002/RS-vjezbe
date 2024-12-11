## RS2 - vježba


# 1. Lambda funkcije

kvadriraj = lambda a: a**2
print(kvadriraj(5))

zbroji = lambda a,b: a+b    
print(zbroji(3,5))

# 1.1 Lambda funkcije kao argumenti drugim funkcijama
def primijeni_na_sve(lista, funkcija):
    rezultat = []
    for element in lista:
        rezultat.append(funkcija(element))
    return rezultat

print(primijeni_na_sve([1,2,3,4], lambda broj: broj + 5))



paran_neparan = lambda x: "paran" if x % 2 == 0 else "neparan"

print(paran_neparan(845))


# 1.2 Funkcije višeg reda

## 1.2.1 Funkcija map
lista = [1,2,3,4,5]
kvadrirana_lista = list(map(lambda x: x**2, lista))

print(kvadrirana_lista)




# MAP objekt

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889", "godina_rodenja" : 2000},
    {"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878", "godina_rodenja" : 1998},
    {"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777", "godina_rodenja" : 2003},
    {"ime": "Petra", "prezime": "Petrić", "jmbag": "0303088777", "godina_rodenja" : 2001}
]

# Primjer: Imamo listu studenata s imenom, prezimenom i JMBAG-om. Želimo izvući samo JMBAG-ove:
## Klasično:
jmbagovi = []
for student in studenti:
    jmbagovi.append(student["jmbag"])

# Map:
jmbagovi = list(map(lambda student: student["jmbag"], studenti))
print(jmbagovi)

def zbroji(a, b):
    return a + b

print(list(map(zbroji, [1, 2, 3], [4, 5, 6])))

# ili kraće:
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]
print(list(map(lambda a, b: a + b, lista_1, lista_2)))

# 1.2.2 Funkcija filter

# Želimo filtrirati samo parne brojeve iz liste

# Klasično: 
parni = []
for broj in lista:
    if broj % 2 == 0:
        parni.append(broj)

print(parni)

# ili kraće:
parni = list(filter(lambda broj: broj % 2 == 0, lista))

print(parni)



# Klasično:
rodeni_prije_2000 = []
for student in studenti:
    if student["godina_rodenja"] < 2000:
        rodeni_prije_2000.append(student)

print(rodeni_prije_2000)

# ili kraće:

rodeni_prije_2000 = list(filter(lambda student: student["godina_rodenja"] < 2000, studenti))
print(rodeni_prije_2000)



# 1.2.3 Funkcije any i all

# Primjer korištenja funkcije any:
print(any([False, False, True]))
print(any([False, False, False, False]))

# Primjer korištenja funkcije all:
print(all([True, True, True]))
print(all([False, True, True]))


# Želimo provjeriti jesu li svi brojevi u listi parni:
lista = [2,4,6]
parni = (all(map(lambda broj: broj % 2 == 0, lista)))
print(parni)

# Želimo provjeriti jesu li svi putnici uplatili aranžman:
putnici = [
    {"ime": "Ivan", "prezime": "Ivić", "uplata": True},
    {"ime": "Marko", "prezime": "Marković", "uplata": True},
    {"ime": "Ana", "prezime": "Anić", "uplata": False}
]
placeno = all(map(lambda putnik: putnik["uplata"], putnici))
print(placeno)

def svi_uplatili(putnici):
    for putnik in putnici:
        if not putnik["uplata"]:
            return False
    return True

print(svi_uplatili(putnici)) # False



# 2. COMPREHENSION sintaksa

# 2.1 List comprehension

# Želimo izgraditi listu kvadrata brojeva od 1 do 10:

# Klasično 
nova_lista = []
for broj in range(1,11):
    nova_lista.append(broj ** 2)

print(nova_lista)

# ili kraće:
nova_lista = list(map(lambda broj: broj ** 2, range(1,11)))
print(nova_lista)

# ili sa list comprehension:
kvadrati = [x ** 2 for x in range(1,11)]
print(kvadrati)
print([broj ** 2 for broj in range(1,11)])



# Želimo izgraditi listu duljina nizova:

# Klasično:
nizovi = ["jabuka", "kruška", "banana", "naranča"]
duljine = []

for rijec in nizovi:
    duljine.append(len(rijec))

print(duljine)

# List comprehension:
duljine2 = [len(rijec) for rijec in nizovi]
print(duljine2)


# Kako izgraditi listu kvadrata brojeva od 1 do 10, ali samo za neparne brojeve:
neparniBrojevi = [broj for broj in range(1,11) if broj % 2 == 0]
print(neparniBrojevi)



# Želimo izgraditi listu imena studenata koji su rođeni prije 1999. godine:

rodeni_prije_1999 = [student["ime"] for student in studenti if student["godina_rodenja"] < 1999]
print(rodeni_prije_1999)


# Želimo izgraditi listu kvadrata brojeva od 1 do 10, ali za neparne brojeve kvadrat,
# a za parnebrojeve sam broj:
kvadrati_neparnih_a_parne_brojevi = [x ** 2 if x % 2 != 0 else x for x in range(1, 11) ]
print(kvadrati_neparnih_a_parne_brojevi)


# Želimo izgraditi listu voća, ali samo prva tri slova svakog voća:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

samo_prva_tri_slova = [voce[:3] for voce in fruits]
print(samo_prva_tri_slova)

sa_slovom_a = [voce for voce in fruits if "a" in voce]

print(sa_slovom_a)



newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) 




# Dictionary comprehension

# Recimo da imamo listu voća fruits i želimo izgraditi rječnik gdje su ključevi voća, 
# a vrijednosti duljina tih voća:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

duljine_voca = {voce: len(voce) for voce in fruits}
print(duljine_voca)



kvadrati_brojeva = {broj: broj ** 2 for broj in range(1,6)}
print(kvadrati_brojeva)


paran_neparan = {i: "paran" if i % 2 == 0 else "neparan" for i in range(1, 11)}
print(paran_neparan)



# Zadaci za vježbu - lambda izrazi, funkcije
# višeg reda i comprehension sintaksa 

# 1. zadatak
kvadriraj = lambda x: x ** 2
print(kvadriraj(5))

# 2. zadatak
zbroji_pa_kvadriraj = lambda a,b: (a+b) ** 2
print(zbroji_pa_kvadriraj(3,4))


# 3. zadatak
niz = 1,2,3
print(niz)
kvadriraj_duljinu = lambda niz: len(niz) ** 2
print(kvadriraj_duljinu(niz))


# 4. zadatak
pomnozi_pa_potenciraj = lambda x, y: (y*5) ** x
print(pomnozi_pa_potenciraj(1,5))

# 5. zadatak
paran_broj = lambda x: "Paran" if x % 2 == 0 else "Neparan" 
print(paran_broj(35))





# Zadatak 2: Funkcije višeg reda

# 1. zadatak
nizovi = ["jabuka", "kruška", "banana", "naranča"]
kvadriraj_duljine = list(map(lambda niz: len(niz) ** 2, nizovi ))
print(kvadriraj_duljine)

# 2. zadatak
brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]
veci_od_5 = list(filter(lambda broj: broj > 5, brojevi))
print(veci_od_5)

# 3. zadatak
brojevi = [10, 5, 12, 15, 20]

transform = dict(map(lambda x: (x,x**2), brojevi))
print(transform)

# 4. zadatak
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

svi_punoljetni = all(map(lambda student: student["godine"] > 18, studenti))
print(svi_punoljetni)

# 5. zadatak
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

min_duljina = int(input("Unesite minimalnu duljinu riječi:"))

duge_rijeci = list(filter(lambda rijec: len(rijec) > min_duljina, rijeci))

print(duge_rijeci)


# Zadatak 3: Comprehension sintaksa

# 1. Zadatak

parni_kvadrati = [broj ** 2 for broj in range (20,51) if broj % 2 == 0]
print(parni_kvadrati)

# 2. Zadatak
rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"]

duljine_sa_slovom_a = [len(rijec) for rijec in rijeci if "a" in rijec]
print(duljine_sa_slovom_a)

# 3. zadatak
kubovi = [{broj: broj ** 3} if broj % 2 != 0 else {broj: broj} for broj in range(1,11)]
print(kubovi)

# 4. zadatak
import math 
korijeni = {broj: round(math.sqrt(broj), 2) for broj in range(50,501, 50)}
print(korijeni)

# 5. zadatak
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]
zbrojeni_bodovi = [{student["prezime"]: sum(student["bodovi"])} for student in studenti]
print(zbrojeni_bodovi)


# 4. Klase i objekti

class Osoba():
    def __init__(self, ime, prezime, godine):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine

    def pozdrav(self):
        return f"Pozdrav, ja sam {self.ime} {self.prezime} i imam {self.godine} godine."

osoba = Osoba("Igor", "Marković", 22)

print(osoba.pozdrav())