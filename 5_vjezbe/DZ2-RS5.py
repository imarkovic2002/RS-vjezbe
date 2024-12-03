# RS5 - Mikroservisna arhitektura
#Interna Klijent-Poslužitelj komunikacija

# Marković Igor

# 3.3 Interna Klijent-Poslužitelj komunikacija

import asyncio, aiohttp
from aiohttp import  web
import json

# 4. zadatak: Dohvaćanje proizvoda
proizvodi = [
    {"id": 1, "naziv": "Laptop", "cijena": 5000},
    {"id": 2, "naziv": "Miš", "cijena": 100},
    {"id": 3, "naziv": "Tipkovnica", "cijena": 200},
    {"id": 4, "naziv": "Monitor", "cijena": 1000},
    {"id": 5, "naziv": "Slušalice", "cijena": 50}
]

async def get_proizvodi(request):
    return web.json_response(proizvodi,status=200)

async def get_proizvod_id(request):
    proizvod_id = request.match_info.get('id')
    if proizvod_id is None:
        return web.json_response(proizvodi, status=200)

    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvod_id):
            return web.json_response(proizvod, status=200)

    return web.json_response({'error':'Proizvod s traženim ID-em ne postoji'}, status=404)


narudzbe = []

async def post_handler(request):
    data = await request.json()
    proizvod_id = data.get('proizvod_id')
    kolicina = data.get('kolicina')

    if not proizvod_id or not kolicina:
        return web.json_response({'error': 'Trebaju biti cijeli podaci napisani.'}, status=400)
    
    for proizvod in proizvodi:
        if proizvod['id'] == int(proizvod_id):
            narudzba = {'id':proizvod_id, 'naziv': proizvod['naziv'], 'kolicina': kolicina}
            narudzbe.append(narudzba)
            return web.json_response(narudzbe, status=200)
        
    return web.json_response({'error':'Proizvod s traženim IDem ne postoji!'}, status=404)



app = web.Application()
app.router.add_get('/proizvodi', get_proizvodi)
app.router.add_get('/proizvodi/{id}', get_proizvod_id)
app.router.add_post('/narudzbe', post_handler)

if __name__ == "__main__":
    web.run_app(app,port=8081)


