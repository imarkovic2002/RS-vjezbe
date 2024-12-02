## RS5 - 27.11.2024.
## Kod sa sata 
## Marković Igor

from aiohttp import web

# def handler_function(request):
#     return web.Response(status=201,text="Pozdrav RS!")

# app = web.Application()

# app.router.add_get('/', handler_function)

# web.run_app(app,port=8080)

import json 

# def handler_function(request):
     
#     data = {'ime': 'Ivo', 'prezime': 'Ivić', 'godine': 25}
#     return web.json_response(data)


## POST ruta
# async def post_handler(request):
#     data = await request.json()
#     print(data)
#     return web.json_response(data)

# app = web.Application()
# app.router.add_post('/', post_handler)

# web.run_app(app,port=8080)

# 1 Zadatak - GET /proizvodi

# proizvodi = [
#     {"naziv": "PC", "cijena": 500, "količina": 3},
#     {"naziv": "Laptop", "cijena": 300, "količina": 5},
#     {"naziv": "Mobitel", "cijena": 400, "količina": 8},
# ]

# # GET ruta
# async def get_proizvodi(request):
#     return web.json_response(proizvodi)

# ## POST ruta
# async def post_handler(request):
#     data = await request.json()
#     print(data)

#     proizvodi.append(data)

#     return web.json_response(proizvodi)

# app = web.Application()

# app.router.add_get('/proizvodi', get_proizvodi)
# app.router.add_post('/proizvodi', post_handler)

# web.run_app(app, port=8081)


# 2. Zadatak

# korisnici = [
#     {'ime': 'Ivo', 'godine': 25},
#     {'ime': 'Ana', 'godine': 17},
#     {'ime': 'Marko', 'godine': 19},
#     {'ime': 'Maja', 'godine': 16},
#     {'ime': 'Iva', 'godine': 22}
# ]

# async def handler_function(request):
#     punoljetni_korisnici = [korisnik for korisnik in korisnici if korisnik['godine']> 18]
#     return web.json_response(punoljetni_korisnici)


# app = web.Application()

# app.router.add_get('/punoljetni', handler_function)
# app.router.add_get('/stariji_korisnici', handler_function)


# web.run_app(app, port=8082)


## Klijent - poslužitelj komunikacija unutar aiohttp


import asyncio, aiohttp

# Klijent 
async def get_users(request):
    return web.json_response({'korisnici': ['Ivo', 'Ana', 'Marko', 'Maja', 'Iva', 'Ivan']})

app = web.Application()

app.router.add_get('/korisnici', get_users)

# Poslužitelj
async def main():
    async with aiohttp.ClientSession() as session:
        print("Klijentska sesija otvorena")
        pass

if __name__ == '__main__':
    print("Direktno pokrenuta skripta...")
    web.run_app(app, host='localhost', port=8080) # pokreće poslužitelj
    asyncio.run(main()) 


## AppRunner klasa

# Ne blokira izvođenje ostatka koda, kao web.run_app()

from aiohttp.web import AppRunner
import aiohttp

async def get_users(request):
    return web.json_response({'korisnici': ['Ivo', 'Ana', 'Marko', 'Maja', 'Iva', 'Ivan']})

app = web.Application()

app.router.add_get('/korisnici', get_users)

async def start_server():
    runner = AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, 'localhost', 8080)
    await site.start()
    print("Poslužitelj sluša na http://localhost:8080")
    
async def main():
    await start_server() # Prvo pokreni poslužitelj
    async with aiohttp.ClientSession() as session: # Zatim otvori klijentsku sesiju
        print("Klijentska sesija otvorena")
        pass


asyncio.run(main()) # Pokreni main korutinu


