## RS3 - vježba
import requests
import time


## 2.1. SLanje HTTP zahtjeva sinkrono

# response = requests.get("https://catfact.ninja/fact")

# print(response.text)

# print(response.status_code)

# def send_requests():
#     response = requests.get("https://catfact.ninja/fact")
#     fact = response.json()["fact"]
#     print(fact)

# start = time.time()
# print('Šaljemo 1. zahtjev...')
# send_requests()

# print('Šaljemo 2. zahtjev...')
# send_requests()

# print('Šaljemo 3. zahtjev...')
# send_requests()

# print('Šaljemo 4. zahtjev...')
# send_requests()

# print('Šaljemo 5. zahtjev...')
# send_requests()

# print('Šaljemo 6. zahtjev...')
# send_requests()

# print('Šaljemo 7. zahtjev...')
# send_requests()

# print('Šaljemo 8. zahtjev...')
# send_requests()

# print('Šaljemo 9. zahtjev...')
# send_requests()

# print('Šaljemo 10. zahtjev...')
# send_requests()

# end = time.time()

# print(f'Izvršavanje programa traje {end-start:.2f} sekundi.')


## Asinkrono slanje zahtjeva
import aiohttp
import asyncio

#### 2.2.2 ClientSession klasa

# async def main():
#     async with aiohttp.ClientSession() as session:
#         for i in range(5):
#             response = await session.get("https://catfact.ninja/fact")
#             fact_dict = await response.json()

#             print(f"{i + 1}:{fact_dict["fact"]}")

# asyncio.run(main())



#### 2.2.3 Konkurentno slanje kroz asyncio.gather

# async def get_cat_fact(session):
#     print("Šaljemo zahtjev za mačji fact")
#     response = await session.get("https://catfact.ninja/fact")
#     fact_dict = await response.json()
#     print(fact_dict['fact'])

# async def main():
#     async with aiohttp.ClientSession() as session:
#         cat_fact_korutine = [get_cat_fact(session) for i in range(5)]
#         await asyncio.gather(*cat_fact_korutine)

# asyncio.run(main())


# 3. Zadaci za vježbu - Slanje konkurentnih HTTP zahtjeva

## 1. zadatak
# async def fetch_users(session):
#     response = await session.get("https://jsonplaceholder.typicode.com/users")
#     return await response.json()

# async def main():
#     start = time.time()

#     async with aiohttp.ClientSession() as session:
#         fetch_users_korutine = [fetch_users(session) for i in range(3)]
#         rezultat = await asyncio.gather(*fetch_users_korutine)

#     users = rezultat[0]

#     imena = [user['name'] for user in users]
#     print("Imena:", imena)

#     email = [user['email'] for user in users]
#     print("Emailovi:", email)

#     username = [user['username'] for user in users]
#     print('Usernames:', username)
    
#     end = time.time()
#     print(f"\nIzvršavanje programa traje {end - start:.2f} sekundi.")

# asyncio.run(main())


# 2. zadatak

# async def get_cat_fact(session):
#     async with session.get("https://catfact.ninja/fact") as response:
#         data = await response.json()
#         return data.get("fact", "")
    
# async def filter_cat_facts(cat_facts):
#         filt_fact = [
#             fact for fact in cat_facts if "cat" in fact.lower() or "cats" in fact.lower()
#         ]
#         return filt_fact

# async def main():
#     async with aiohttp.ClientSession() as session:
#         cat_fact_tasks = [get_cat_fact(session) for _ in range(20)]
#         cat_facts = await asyncio.gather(*cat_fact_tasks)
#         filt_fact = await filter_cat_facts(cat_facts)

#         print("\nFiltrirane činjenice o mačkama:")
#         print(filt_fact)

# asyncio.run(main())

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
    return [cat_facts if len(dog_facts) > len(cat_facts) else dog_facts for dog_fact, cat_fact in zip(dog_facts, cat_facts)]

async def main():
    async with aiohttp.ClientSession() as session:

        dog_facts_tasks = [get_dog_fact(session) for _ in range(5)]
        cat_facts_tasks = [get_cat_fact(session) for _ in range(5)]

        dog_cats_facts = await asyncio.gather(*dog_facts_tasks, *cat_facts_tasks)

        dog_facts = dog_cats_facts[:5]
        cat_facts = dog_cats_facts[5:]

        filtrirano = await mix_facts(dog_facts, cat_facts)

        print("Mixane činjenice o psima i mačkama:")
        for fact in filtrirano:
            print(fact)
        
asyncio.run(main())