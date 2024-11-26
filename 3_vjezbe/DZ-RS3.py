# RS3 - Asinkroni Python: Osnove asyncio biblioteke
## Konkurentno izvođenje | Korutine | asyncio.run/gather | Tasks

### Domaća zadaća - Marković Igor

import asyncio

# 1. Definirajte korutinu koja će simulirati dohvaćanje podataka s weba. Podaci neka budu lista
# brojeva od 1 do 10 koju ćete vratiti nakon 3 sekunde. Listu brojeva definirajte comprehensionom.
# Nakon isteka vremena, u korutinu ispišite poruku "Podaci dohvaćeni." i vratite podatke. Riješite bez
# korištenja asyncio.gather() i asyncio.create_task() funkcija.

async def korutina():
    print("Dohvaćam podatke!")
    lista = [i for i in range (1,11)]
    await asyncio.sleep(3)
    print("Podaci dohvaćeni!", "Lista:" ,lista)
    return lista 

asyncio.run(korutina())

#2. Definirajte dvije korutine koje će simulirati dohvaćanje podataka s weba. Prva korutina neka vrati
# listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o korisnicima) nakon 3 sekunde, a druga
# korutina neka vrati listu proizvoljnih rječnika (npr. koji reprezentiraju podatke o proizvodima) nakon 5
# sekundi. Korutine pozovite konkurentno korištenjem asyncio.gather() i ispišite rezultate. Program
# se mora izvršavati ~5 sekundi.

async def korutina_1():
    print("Dohvaćam podatke o korisnicima...")
    await asyncio.sleep(3)
    print("Podaci o korisniku dohvaćeni!")

async def korutina_2():
    print("Dohvaćam podatke o proizvodima...")
    await asyncio.sleep(5)
    print("Podaci o proizvodima dohvaćeni!")


async def main():
    data = await asyncio.gather(korutina_1(), korutina_2())

asyncio.run(main())


# 3. Zadatak
baza_korisnika = [
{'korisnicko_ime': 'mirko123', 'email': 'mirko123@gmail.com'},
{'korisnicko_ime': 'ana_anic', 'email': 'aanic@gmail.com'},
{'korisnicko_ime': 'maja_0x', 'email': 'majaaaaa@gmail.com'},
{'korisnicko_ime': 'zdeslav032', 'email': 'deso032@gmail.com'}
]

baza_lozinka = [
{'korisnicko_ime': 'mirko123', 'lozinka': 'lozinka123'},
{'korisnicko_ime': 'ana_anic', 'lozinka': 'super_teska_lozinka'},
{'korisnicko_ime': 'maja_0x', 'lozinka': 's324SDFfdsj234'},
{'korisnicko_ime': 'zdeslav032', 'lozinka': 'deso123'}
]

async def autentifikacija(korisnicko_ime, email,lozinka):
    print("Kreće provjera podataka o korisniku...")
    await asyncio.sleep(3)

    korisnik = {'korisnicko_ime': korisnicko_ime, 'email': email}

    if (korisnik in baza_korisnika):
        rezultat_autorizacije = await autorizacija(korisnicko_ime, lozinka)
        print(rezultat_autorizacije)
    else:
        print(f"Korisnik {korisnik} nije pronađen!")


async def autorizacija(korisnicko_ime, lozinka):
    print("Autorizacija...")
    await asyncio.sleep(2)

    korisnik_lozinka = [i for i in baza_lozinka if i['korisnicko_ime'] == korisnicko_ime]

    
    if (korisnik_lozinka and korisnik_lozinka[0]['lozinka'] == lozinka):
        print(f"Korisnik {korisnicko_ime}: Autorizacija uspješna.") 
    else:
        print(f"Korisnik {korisnicko_ime}: Autorizacija neuspješna.") 

async def main():
    await autentifikacija('mirko123','mirko123@gmail.com', 'lozinka1523')

asyncio.run(main())


#4. Zadatak
import random

async def provjeri_parnost(n):
    print("Provjera parnosti...")
    asyncio.sleep(2)
    if n % 2 == 0:
        print(f"Broj {n} je paran")
    else:
        print(f"Broj {n} je neparan.")
    

async def main():
    lista = [random.randint(1,100) for i in range(10)]
    zadaci = [asyncio.create_task(provjeri_parnost(n)) for n in lista]

    data = await asyncio.gather(*zadaci)

asyncio.run(main())


# 5. zadatak
lista = [
        {'prezime': 'Marković', 'broj_kartice': '1234', 'CVV': '123'},
        {'prezime': 'Perić', 'broj_kartice': '9876', 'CVV': '456'},
        {'prezime': 'Ivić', 'broj_kartice': '5678', 'CVV': '789'}
    ]


async def secure_data(prezime, broj_kartice, cvv):
    print("Enkripcija podataka započinje...")
    await asyncio.sleep(3)
    return {
        'prezime': prezime,
        'broj_kartice': f"enkriptirano-{hash(broj_kartice)}",
        'CVV': f"enkriptirano-{hash(cvv)}"
    }


async def main():
    zadaci = [secure_data(podaci['prezime'], podaci['broj_kartice'], podaci['CVV']) for podaci in lista]

    data = await asyncio.gather(*zadaci)

    for enkriptirani_podaci in data:
        print(enkriptirani_podaci)

asyncio.run(main())