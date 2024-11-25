# Vježbe sa sata 
# Srijeda -> 13.11.2024

lista = [1,2,3,4,5,6,7,8,9,10]


lista_2 = list(filter(lambda x: x % 2 == 0, lista))

print(lista_2)

studenti = [
    {"ime":"Ivan", "godiste":1987},
    {"ime":"Marko", "godiste":2000}
]

studenti_2 = list(filter(lambda student: student["godiste"] > 2000, studenti))
print(studenti_2)

lista = [2, 4, 6, 8]

parnost = list(map(lambda broj : broj %2 == 0, lista)) ## radi provjeru i prebacuje u [True, True, True, False]
print(parnost)

svi_parni = all(parnost)
print(svi_parni) # True



## Comprehension sintaksa - list comprehension jer krećemo izraz s []

brojevi = [i**2 for i in range(1,11)]

print(brojevi)

nizovi = ["jabuka", "banana", "kruška", "naranča"]

novi_niz = [len(i) for i in nizovi]
novi_niz2 = {len(i) for i in nizovi} # - skup (razlika: {})
print(novi_niz)
print(novi_niz2)

lista_brojeva = [52,23,54,64,64,213,421]

parni = [i for i in lista_brojeva if i % 2 == 0]
print(parni)


# ako je paran stavi kvadrat, ako je neparan stavi kub
paran_neparan = [i**2 if i % 2 == 0 else i**3 for i in lista_brojeva]
print(paran_neparan)


# Lista imena koji su rođeni prije 1999:
imena_rodenih_prije_1999 = [student["ime"] for student in studenti if student["godiste"] < 1999]

print(imena_rodenih_prije_1999)



## Dictionary comprehension
#zadatak: napraviti dict sa comp gdje je kljuc naziv voca a vrijednost duljina stringa toga voća
fruits = ["apple", "banana", "kiwi"]
fruits_dict = {voce: len(voce) for voce in fruits}
print(fruits_dict)

## 4
pomnozi_i_pontenciraj = (lambda x,y: y * 5**x)
print(pomnozi_i_pontenciraj)

# Koristeći funkcije all i map, provjerite jesu li svi studenti punoljetni:
studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19},
    {"ime": "Marko", "prezime": "Marković", "godine": 22},
    {"ime": "Ana", "prezime": "Anić", "godine": 21},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17},
    {"ime": "Mate", "prezime": "Matić", "godine": 18}
]

punoljetni = list(map(lambda student: student["godine"] >= 18, studenti))
print(punoljetni)
svi_punoljetni = all(punoljetni)

print(svi_punoljetni) # False


kubovi = [i**3 for i in range(1,11)]
kubovi_dict = {i: i**3 for i in range(1,11)}
print(kubovi_dict)

