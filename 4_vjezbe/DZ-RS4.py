# RS4 - Asinkroni Python: Slanje konkurentnih HTTP zahtjeva
# HTTP protokol | Sinkrono slanje zahtjeva kroz requests \ Konkurentno slanje zahtjeva kroz aiohttp

# DZ - Marković Igor

# 3. Zadaci za vježbu - Slanje konkurentnih HTTP zahtjeva

## 1. Zadatak

import aiohttp
import time
import asyncio

async def fetch_users(session):
    async with session.get("https://jsonplaceholder.typicode.com/users") as response:
        return await response.json()

async def main():
    start = time.time()

    async with aiohttp.ClientSession() as session:
        user_korutina = [fetch_users(session) for i in range(5)]
        rezultat = await asyncio.gather(*user_korutina)

    users = rezultat[0]

    imena = [user['name'] for user in users]
    print("Imena:", imena)

    emailovi = [user['email'] for user in users]
    print("Email adrese:", emailovi)

    username = [user['username'] for user in users]
    print("Korisnička imena:", username)

    end = time.time()
    print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")

asyncio.run(main())


# 2. Zadatak

async def get_cat_fact(session):
    async with session.get("https://catfact.ninja/fact") as response:
        data = await response.json()
        return data.get("fact", "")
    
async def filter_cat_facts(cat_facts):
        filt_fact = [
            fact for fact in cat_facts if "cat" in fact.lower() or "cats" in fact.lower()
        ]
        return filt_fact

async def main():
    async with aiohttp.ClientSession() as session:
        cat_fact_tasks = [get_cat_fact(session) for _ in range(20)]
        cat_facts = await asyncio.gather(*cat_fact_tasks)
        filt_fact = await filter_cat_facts(cat_facts)

        print("Filtrirane činjenice o mačkama:")
        print(filt_fact)

asyncio.run(main())


# 3. Zadatak

async def get_dog_fact(session):
    async with session.get("https://dogapi.dog/api/v2/facts") as response:
        data = await response.json()
        return data["data"][0]["attributes"]["body"]

async def get_cat_fact(session):
    async with session.get("https://catfact.ninja/fact") as response:
        data = await response.json()
        return data.get("fact")

async def mix_facts(dog_facts, cat_facts):
    return [
        dog_fact if len(dog_fact) > len(cat_fact) else cat_fact
        for dog_fact, cat_fact in zip(dog_facts, cat_facts)
    ]

async def main():
    async with aiohttp.ClientSession() as session:

        dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]

        rezultat = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

        dog_facts = rezultat[:5]
        cat_facts = rezultat[5:]

        filtrirano = await mix_facts(dog_facts, cat_facts)

        print("Mixane činjenice o psima i mačkama:")
        for fact in filtrirano:
            print(fact)


asyncio.run(main())