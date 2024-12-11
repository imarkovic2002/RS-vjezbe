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
async def fetch_data1():
    print('Dohvaćam podatke s API_1...')
    await asyncio.sleep(2)
    print('Podaci s API-a 1 dohvaćeni.')
    return{'api_1': 'uspjesno'}

async def fetch_data2():
    print('Dohvaćam podatke s API_2...')
    await asyncio.sleep(4)
    print('Podaci s API-a 2 dohvaćeni.')
    return{'api_2': 'uspjesno'}

async def main():

    podaci_1, podaci_2 = await asyncio.gather(fetch_data1(), fetch_data2())

    print(f'Podaci s API-ja 1: {podaci_1} ')
    print(f'Podaci s API-ja 2: {podaci_2}')

asyncio.run(main())


## 1.3 asyncio tasks
