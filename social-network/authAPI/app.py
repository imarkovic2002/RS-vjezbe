from aiohttp import web
import hashlib

app = web.Application()

korisnici = [
    {"korisnicko_ime": "admin", "lozinka_hash": "8d43d8eb44484414d61a18659b443fbfe52399510da4689d5352bd9631c6c51b"},
    {"korisnicko_ime": "markoMaric", "lozinka_hash": "5493c883d2b943587ea09ab8244de7a0a88d331a1da9db8498d301ca315d74fa"},
    {"korisnicko_ime": "ivanHorvat", "lozinka_hash": "a31d1897eb84d8a6952f2c758cdc72e240e6d6d752b33f23d15fd9a53ae7c302"},
    {"korisnicko_ime": "Nada000", "lozinka_hash": "492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d"}
]

def hash_data(data: str) -> str:
    return hashlib.sha256(data.encode()).hexdigest()

async def register(request):
    try:
        data = await request.json()
    except Exception:
        return web.json_response({'error': 'Neispravan JSON format'}, status=400)
    if 'korisnicko_ime' not in data or 'lozinka' not in data:
        return web.json_response({'error': 'Nedostaju korisnicko_ime ili lozinka'}, status=400)
    korisnicko_ime = data['korisnicko_ime']
    lozinka = data['lozinka']
    if korisnicko_ime in [korisnik["korisnicko_ime"] for korisnik in korisnici]:
        return web.json_response({'error': 'Korisnik već postoji'}, status=400)
    lozinka_hash = hash_data(lozinka)
    novi_korisnik = {
        "korisnicko_ime": korisnicko_ime,
        "lozinka_hash": lozinka_hash,
    }
    korisnici.append(novi_korisnik)
    return web.json_response(novi_korisnik, status=201)

async def login(request):
    data = await request.json()
    korisnicko_ime = data.get("korisnicko_ime")
    lozinka = data.get("lozinka")
    hashed_lozinka = hash_data(lozinka)

    for korisnik in korisnici:
        if korisnik["korisnicko_ime"] == korisnicko_ime and korisnik["lozinka_hash"] == hashed_lozinka:
            return web.json_response({"authorized": True})
    
    return web.json_response({"authorized": False}, status=401)

app.router.add_post("/register", register)
app.router.add_post("/login", login)

if __name__ == "__main__":
    web.run_app(app, host="0.0.0.0", port=9000)
