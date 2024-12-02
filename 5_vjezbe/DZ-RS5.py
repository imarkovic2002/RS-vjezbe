# RS5 - Mikroservisna arhitektura
# Definiranje jednostavnih aiohttp poslužitelja

# Marković Igor

import asyncio, aiohttp
from aiohttp import  web
import json

# 1. i 2. zadatak - GET /proizvodi i POST /proizvodi

proizvodi = [
    {"naziv": "PC", "cijena": 500, "količina": 3},
    {"naziv": "Laptop", "cijena": 300, "količina": 5},
    {"naziv": "Mobitel", "cijena": 400, "količina": 8},
]

# GET ruta
async def get_proizvodi(request):
    return web.json_response(proizvodi)

## POST ruta
async def post_handler(request):
    data = await request.json()
    print(data)

    proizvodi.append(data)

    return web.json_response(proizvodi)

app = web.Application()

app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_post('/proizvodi', post_handler)

web.run_app(app, port=8081)


# 3. Zadatak - GET /punoljetni

korisnici = [
    {'ime': 'Ivo', 'godine': 25},
    {'ime': 'Ana', 'godine': 17},
    {'ime': 'Marko', 'godine': 19},
    {'ime': 'Maja', 'godine': 16},
    {'ime': 'Iva', 'godine': 22}
]

async def handler_function(request):
    punoljetni_korisnici = [korisnik for korisnik in korisnici if korisnik['godine']> 18]
    return web.json_response(punoljetni_korisnici)


app = web.Application()

app.router.add_get('/punoljetni', handler_function)
app.router.add_get('/stariji_korisnici', handler_function)


web.run_app(app, port=8082)