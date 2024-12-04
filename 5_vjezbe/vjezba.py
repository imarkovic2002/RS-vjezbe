korisnici = [
    {"id": 1, "ime": "Ana", "email": "ana@example.com", "lozinka": "tajna123"},
    {"id": 2, "ime": "Ivan", "email": "ivan@example.com", "lozinka": "lozinka456"},
    {"id": 3, "ime": "Maja", "email": "maja@example.com", "lozinka": "maja789"},
    {"id": 4, "ime": "Marko", "email": "marko@example.com", "lozinka": "marko1234"},
    {"id": 5, "ime": "Petra", "email": "petra@example.com", "lozinka": "petra5678"}
]

import aiohttp, asyncio
import json 
from aiohttp import web

async def get_users(request):
    return web.json_response(korisnici, status=200)

async def get_users_id(request):
    users_id = request.match_info.get('id')
    if users_id is None:
        return web.json_response(korisnici, status=200)
    
    for korisnik in korisnici:
        if korisnik['id'] == int(users_id):
            return web.json_response(korisnik, status=200)
        
    return web.json_response({'error': 'Korisinik s tim ID-em ne postoji'}, status=404)

async def post_korisnici(request):
    data = await request.json()

    korisnici_id = 

app = web.Application()
app.router.add_get('/korisnici', get_users)
app.router.add_get('/korisnici/{id}', get_users_id)

if __name__ == "__main__":
    web.run_app(app,port=8080)