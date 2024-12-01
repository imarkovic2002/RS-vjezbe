## RS4 - 22.11.2024.
## Kod sa sata 
## Marković Igor


import aiohttp
import asyncio
import time


# 2.2.3 Konkurentno slanje kroz asyncio.gather

# async def get_cat_fact(session):
#     start = time.time()
#     print("Šaljemo zahtjev za mačji fact...")
#     response = await session.get("https://catfact.ninja/fact")
#     fact_dict = await response.json()
#     print(fact_dict['fact'])
#     end = time.time()
#     print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")

# async def main():
#     async with aiohttp.ClientSession() as session:
#         cat_fact_korutine = [get_cat_fact(session) for i in range(5)]
#         await asyncio.gather(*cat_fact_korutine)

# asyncio.run(main())


# 2.2.4 Konkurentno slanje kroz asyncio.Task

# Sintaksa: 
#   task = asyncio.create_task(korutina)

async def get_cat_fact(session):
    response = await session.get("https://catfact.ninja/fact")
    fact_dict = await response.json()
    return fact_dict['fact']

async def main():
    start = time.time()
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks = [asyncio.create_task(get_cat_fact(session)) for _ in range(5)] #pohranjujemo Taskove u listu
        actual_cat_facts = await asyncio.gather(*cat_fact_tasks)

end = time.time()
print(actual_cat_facts)
print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")

asyncio.run(main())