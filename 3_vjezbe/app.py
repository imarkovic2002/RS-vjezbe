## RS3 - 20.11.2024.
## Kod sa sata 
## Marković Igor

import asyncio
async def korutina():
    lista = [i for i in range(1,11)]
    await asyncio.sleep(3)
    print ('Podaci su dohvaćeni.')
    return lista

asyncio.run(korutina())

# 2. Zadatak
async def korutina_1():
    print('Dohvaćam podatke o korisniku...')
    await asyncio.sleep(3)
    print('Podaci o korisniku dohvaćeni...')
    return {'api_1': 'uspješno'}

async def korutina_2():
    print('Dohvaćam podatke o proizvodu...')
    await asyncio.sleep(5)
    print('Podaci o proizvodu dohvaćeni.')
    return {'api_2': 'uspješno'}

async def main():
    podaci_1, podaci_2 = await asyncio.gather(korutina_1(), korutina_2())

asyncio.run(main())

# 5. Zadatak
async def secure_data(prezime, broj_kartice, cvv):
    print("Enkripcija podataka...")
    zadaci = []
    await asyncio.sleep(3)
    return {'prezime': prezime , 'broj_kartice': broj_kartice,'CVV': cvv}


async def main():
    await asyncio.gather(
        crea
    )