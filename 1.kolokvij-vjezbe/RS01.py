## RS01 - vježba

# print("Hello world!")

# a = 5
# b = "Hello World!"
# c = 5.4


# x = str(3)
# y = int(3)
# z = float(3)

# print(x)
# print(y)
# print(z)

# print(type(x))
# print(type(y))
# print(type(z))

# a = int(input("Unesite broj:"))

# if a % 2 == 0:
#     print("Broj je paran")
# elif a % 2 == 1:
#     print("Broj je neparan.")
# else:
#     print("Broj nije niti paran niti neparan.")


# a = float(input("Unesite prvi broj:"))
# b = float(input("Unesite drugi broj:"))
# operator = input("Unesite operator:")

# if operator == "+":
#     print("Rezultat operacije", a ,"+", b, " je:", a+b)

# elif operator == "-":
#     print("Rezultat operacije", a ,"-", b ," je:",a-b)

# elif operator == "*":
#     print("Rezultat operacije", a ,"*", b ," je:",a*b)

# elif operator == "/":
#     print("Rezultat operacije", a ,"/", b ," je:",a/b)

# else:
#     print("Nepodržani operatori!")

# prijestupna_godina = int(input("Upišite godinu:"))

# if prijestupna_godina % 4 == 0 or prijestupna_godina / 400 == 0 or prijestupna_godina % 2 != 0:
#     print("Godina", prijestupna_godina, "je prijestupna!")
# else:
#     print("Godina", prijestupna_godina, " nije prijestupna!")

# rjecnik = {"ime": "Igor", "prezime": "Marković", "dob": 22, "ime": "Petar"}
# print(rjecnik["ime"])

# skup = {1,2,3,4,5}

# skup_2 = {"jabuka", "banana", "rajčica", "kelj"}
# print(skup_2)

# skup.add(6)
# print(skup)

# skup.remove(3)
# print(skup)

# def zbroj(a, b):
#     return a+b


# print(zbroj(3,5))

# import time

# def točnoVrijeme():
#     vrijeme = time.localtime() # funkcija (metoda) koja vraća trenutno vrijeme
#     sati = vrijeme.tm_hour # funkcija (metoda) koja vraća trenutni sat
#     minute = vrijeme.tm_min # funkcija (metoda) koja vraća trenutnu minutu
#     sekunde = vrijeme.tm_sec # funkcija (metoda) koja vraća trenutnu sekundu
#     return f"{sati}:{minute}:{sekunde}"

# print(točnoVrijeme())

# lozinka = str(input("Unesite lozinku:"))
# if len(lozinka) < 8 or len(lozinka) > 15:
#     print("Lozinka mora sadržavati između 8 i 15 znakova")
# elif not any(char.isupper() for char in lozinka) or not any(char.isdigit() for char in lozinka):
#     print ("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj.")
# elif "password" in lozinka.lower() or lozinka in lozinka.lower():
#     print ("Lozinka ne smije sadržavati riječi password ili lozinka.")
# else:
#     print("Lozinka je dovoljno jaka!")


def filtriraj_parne(lista):
    nova_lista = []
    for i in lista:
        if i % 2 == 0:
            nova_lista.append(i)
    return nova_lista

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filtriraj_parne(lista))