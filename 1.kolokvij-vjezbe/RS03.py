## RS3 - vježba


# 1. asyncio biblioteka

## 1.1. Korutine (eng. Coroutines)

import asyncio 
# async def  main():
#     print('Hello')
#     await asyncio.sleep(5)
#     print('World')

# asyncio.run(main())

## 1.2. Konkurentno izvršavanje više korutina

### Primjer dohvaćanja podataka sa weba:
# async def fetch_data():
#     print('Dohvaćam podatke...')
#     data = {'iznos': '3000', 'stanje': 'izvrsno' }
#     await asyncio.sleep(3)
#     print('Podaci dohvaćeni!')
#     return data

# async def main():
#     data = await fetch_data()
#     print(f'Podaci: {data}')

# asyncio.run(main())


### Primjer dohvaćanja podataka sa različitih API-a:
# async def fetch_data1():
#     print('Dohvaćam podatke s API_1...')
#     await asyncio.sleep(2)
#     print('Podaci s API-a 1 dohvaćeni.')
#     return{'api_1': 'uspjesno'}

# async def fetch_data2():
#     print('Dohvaćam podatke s API_2...')
#     await asyncio.sleep(4)
#     print('Podaci s API-a 2 dohvaćeni.')
#     return{'api_2': 'uspjesno'}

# async def main():

#     podaci_1, podaci_2 = await asyncio.gather(fetch_data1(), fetch_data2())

#     print(f'Podaci s API-ja 1: {podaci_1} ')
#     print(f'Podaci s API-ja 2: {podaci_2}')

# asyncio.run(main())


## 1.3 asyncio tasks

# async def fetch_data_1():
#     print('Dohvaćam podatke s API-ja 1...')
#     await asyncio.sleep(2)
#     print('Podaci s API-ja 1 dohvaćeni.')
#     return {'api_1': 'uspješno'}

# async def fetch_data_2():
#     print('Dohvaćam podatke s API-ja 2...')
#     await asyncio.sleep(4)
#     print('Podaci s API-ja 2 dohvaćeni.')
#     return {'api_2': 'uspješno'}

# async def main():
#     task_1 = asyncio.create_task(fetch_data_1())
#     task_2 = asyncio.create_task(fetch_data_2())

#     podaci_1 = await task_1
#     podaci_2 = await task_2

#     print(f'Podaci s API-ja 1: {podaci_1}')
#     print(f'Podaci s API-ja 2: {podaci_2}')

# asyncio.run(main())

### 2. Zadaci za vježbu - Korutine, Task objekti, asyncio.gather()

#### 1. i 2. Zadatak 

# async def fetch_korisnici():
#     print('Dohvaćam podatke o korisnicima...')
#     await asyncio.sleep(3)
#     print('Podaci o korisnicima dohvaćeni.')

# async def fetch_proizvodi():
#     print('Dohvaćam podatke o proizvodima...')
#     await asyncio.sleep(5)
#     print('Podaci o proizvodima dohvaćeni.')


# async def main():
#     izvodenje = asyncio.gather(fetch_korisnici(), fetch_proizvodi())
#     await izvodenje

# asyncio.run(main())


#### 3. Zadatak
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
    await autentifikacija('mirko123','mirko123@gmail.com', 'lozinka123')

asyncio.run(main())