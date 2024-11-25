## Vježbe od doma - Marković Igor
#19.11.2024.


kvadriraj = lambda x: x**2
print(kvadriraj(5))

zbroji = lambda x,y: x + y 
print(zbroji(3,5))

zbroji_kvadrate = lambda x,y: x **2 + y**2
print(zbroji_kvadrate(3,4))

pozdrav = lambda ime = "Igor": f"Pozdrav, {ime}!"

print(pozdrav("Marko"))

circle_area = lambda r = 1, pi = 3.14: pi * r ** 2
print(circle_area(2))

multiplier = lambda x, factor = 2: factor * x
print(multiplier(5,5))

def primijeni_na_sve(lista, funkcija):
    rezultat = []
    for element in lista:
        rezultat.append(funkcija(element))
    return rezultat

uvecaj_za_5 = lambda broj: broj + 5
print(primijeni_na_sve([1,2,3,4], uvecaj_za_5))

kvadriraj_parne = lambda x: x **2 if x % 2 == 0 else x

print(kvadriraj_parne(4))

paran_neparan = lambda x: "paran" if x % 2 == 0 else "neparan"

print(paran_neparan(4))


# 1.2 Funkcije višeg reda 

## 1.2.1. Funkcija map()

lista = [1,2,3,4,5]
kvadriraj = lambda x: x ** 2
kvadrirana_lista = list(map(kvadriraj,lista))

print(kvadrirana_lista)

###     ILI KRAĆE  
kvadrirana_lista = list(map(lambda x: x ** 2, lista))

print(kvadrirana_lista)

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889"},
{"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878"},
{"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777"}
]

jmbagovi = list(map(lambda student: student["jmbag"], studenti))

print(jmbagovi)

## 1.2.2. Filter funkcija

lista = [1,2,3,4,5,6,7,8,9,10]

parni = list(filter(lambda x: x % 2 == 0, lista))

print (parni)


studenti = [
{"ime": "Ivan", "prezime": "Ivić", "jmbag": "0303077889", "godina_rodenja" : 2000},
{"ime": "Marko", "prezime": "Marković", "jmbag": "0303099878", "godina_rodenja" : 1999},
{"ime": "Ana", "prezime": "Anić", "jmbag": "0303088777", "godina_rodenja" : 2003},
{"ime": "Petra", "prezime": "Petrić", "jmbag": "0303088777", "godina_rodenja" : 2001}
]

rodeni_prije_2000 = list(filter(lambda student: student["godina_rodenja"] < 2000, studenti))
print(rodeni_prije_2000)

## 1.2.3 Funkcije any i all

putnici = [
{"ime": "Ivan", "prezime": "Ivić", "uplata": True},
{"ime": "Marko", "prezime": "Marković", "uplata": True},
{"ime": "Ana", "prezime": "Anić", "uplata": False}
]

print(any(map(lambda putnik: putnik["uplata"], putnici)))

# Pogledati još funkcije sorted, reduce, zip i slične!!!



# 2. Comprehension sintaksa


### 4 vrste comprehension sintakse:
##### 1. List comprehension (izgradnja liste)
##### 2. Dictionary comprehension (izgradnja rječnika)
##### 3. Set comprehension (izgradnja skupa)
##### 4. Generator comprehension (izgradnja generatora)


## 2.1. List comprehension


## Želimo izgraditi listu kvadrata brojeva od 1 do 10.
# Uz pomoć map funkcije:
kvadrati = list(map(lambda x: x**2,range(1,11)))
print(kvadrati)

# Korištenjem list comprehension:
kvadrati = [x**2 for x in range(1,11)]
print(kvadrati)


# želimo izgraditi listu duljina nizova:
nizovi = ["jabuka", "kruška", "banana", "naranča"]
duljine = [len(niz) for niz in nizovi]
print(duljine)


# Kako izgraditi listu kvadrata brojeva od 1 do 10, ali samo za neparne brojeve
kvadrati_neparnih = [x**2 for x in range(1,11) if x % 2 != 0]
print(kvadrati_neparnih)


# Kako ovo koristiti sa strukturama? Imamo listu rječnika gdje želimo izgraditi listu imena studenata koji su rođeni prije 1999. godine:
studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godina_rodenja": 2000},
{"ime": "Marko", "prezime": "Marković", "godina_rodenja": 1990},
{"ime": "Ana", "prezime": "Anić", "godina_rodenja": 2003},
{"ime": "Petra", "prezime": "Petrić", "godina_rodenja": 2001}
]

rodeni_prije_1999 = [student["ime"] for student in studenti if student["godina_rodenja"] < 1999]
print(rodeni_prije_1999)

# Želimo izgraditi listu kvadrata brojeva od 1 do 10, ali za neparne brojeve kvadrat, a za parne brojeve sam broj:
neparni_kvadrati_parni_broj = [x ** 2 if x % 2 != 0 else x  for x in range(1, 11)]
print(neparni_kvadrati_parni_broj)



# Želimo izgraditi listu voća, ali samo prva tri slova svakog voća:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
prva_tri_slova = [fruit[:3] for fruit in fruits]
print(prva_tri_slova)


## 2.2 Dictionary comprehension


# Recimo da imamo listu voća fruits i želimo izgraditi rječnik gdje su ključevi voća, a vrijednosti duljina tih voća:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
duljina_voca = {fruit:len(fruit) for fruit in fruits}
print(duljina_voca)


# Možemo napraviti i rječnik gdje su ključevi i vrijednosti brojevi, a petlja ide od 1 do 5:

kvadrati_brojeva = {x: x**2 for x in range(1,6)} 
print(kvadrati_brojeva)