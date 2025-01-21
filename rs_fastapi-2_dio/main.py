## Nastavak FastAPI-ja - RS06
## 15.1.2025.

from fastapi import FastAPI, HTTPException, Path
import random
from datetime import datetime

from models import FilmResponse, Korisnik, BaseProizvod, RequestProizvod, ResponseProizvod, KorisnikBase, KorisnikCreate, KorisnikResponse, Korisnik, Knjiga, KnjigaRequest, KnjigaResponse

app = FastAPI()


filmovi = [
    {
    "id": 1,
    "naziv": "Titanic",
    "genre": "drama",
    "godina": 1997
    },
    {
    "id": 2,
    "naziv": "Inception",
    "genre": "akcija",
    "godina": 2010
    }
]

proizvodi = [
    {"id": 1, "naziv": "majica", "boja": "plava", "cijena": 50},
    {"id": 2, "naziv": "hlače", "boja": "crna", "cijena": 100},
    {"id": 3, "naziv": "tenisice", "boja": "bijela", "cijena": 150},
    {"id": 4, "naziv": "kapa", "boja": "smeđa", "cijena": 20}
]

korisnici = [
    { "id": 1, "ime": "Ivan", "prezime": "Horvat", "email": "ivan.horvat@example.com", "dob": 25, "racun_aktivan": True },
    { "id": 2, "ime": "Ana", "prezime": "Kovačić", "email": "ana.kovacic@example.com", "dob": 30, "racun_aktivan": False },
    { "id": 3, "ime": "Marko","prezime": "Perić","email": "marko.peric@example.com", "dob": 28, "racun_aktivan": True },
    { "id": 4, "ime": "Lucija", "prezime": "Jurić", "email": "lucija.juric@example.com", "dob": 22, "racun_aktivan": True }
]



@app.get("/filmovi", response_model=list[FilmResponse])
def get_filmovi():
    return filmovi

@app.get("/proizvodi", response_model=ResponseProizvod)
def get_proizvodi(proizvod: RequestProizvod):
    PDV_MULTIPLIER = 1.25
    some_id = random.randrange(1,100)
    cijena_pdv = proizvod.cijena + PDV_MULTIPLIER
    proizvod_spreman_za_pohranu : ResponseProizvod = {**proizvod.model_dump(), "id": some_id, "cijena_pdv": cijena_pdv}
    proizvodi.append(proizvod_spreman_za_pohranu)
    return proizvod_spreman_za_pohranu

## Ruta za registraciju korisnika
@app.post("/korisnici", response_model=KorisnikResponse)
def registracija_korisnika(korisnik: KorisnikCreate):
    lozinka_hash = str(hash(korisnik.lozinka_txt))
    datum_registracije = datetime.now()
    korisnik_spreman_za_pohranu = KorisnikResponse(
        ime = korisnik.ime,
        prezime = korisnik.prezime,
        email = korisnik.email,
        lozinka_hash = lozinka_hash,
        datum_registracije = datum_registracije
    )
    
    print(f"Korisnik spreman za pohranu: {korisnik_spreman_za_pohranu}")

    korisnici.append(korisnik_spreman_za_pohranu)
    return korisnik_spreman_za_pohranu

@app.get("/korisnici",response_model=Korisnik)
def get_korisnici():
    return korisnici



### 3. Obrada grešaka

knjige = [
{"id": 1, "naslov": "Ana Karenjina", "autor": "Lav Nikolajevič Tolstoj", "broj_stranica": 864, "godina_izdavanja": 1877},
{"id": 2, "naslov": "Kiklop", "autor": "Ranko Marinković", "broj_stranica": 488, "godina_izdavanja": 1965},
{"id": 3, "naslov": "Proces", "autor": "Franz Kafka", "broj_stranica": 208, "godina_izdavanja": 1925}
]

@app.get("/knjige/{naslov}", response_model=Knjiga)
def dohvati_knjige(naslov: str):
    for knjiga in knjige:
        if knjiga["naslov"] == naslov:
            return knjiga
    raise HTTPException(status_code=404, detail="Knjiga nije pronađena.")

@app.post("/knjige", response_model=KnjigaResponse)
def dodaj_knjigu(knjiga_request: KnjigaRequest):
    for pohranjena_knjiga in knjige:
        if pohranjena_knjiga["naslov"] == knjiga_request.naslov:
            raise HTTPException(status_code = 400, detail = "Knjiga već postoji.")
    new_id = knjige[-1]["id"] + 1 
    nova_knjiga : KnjigaResponse = {"id": new_id, **knjiga_request.model_dump()}
    knjige.append(nova_knjiga)
    return nova_knjiga

@app.get("/knjige")
def dohvati_knjige(min_stranice: int = 0, max_stranice: int = 1000, godina_izdavanja: int = 0):
    filtrirane_knjige = []
    for knjiga in knjige:
        if knjiga["broj_stranica"] >= min_stranice and knjiga["broj_stranica"] <= max_stranice and knjiga["godina_izdavanja"] == godina_izdavanja:
            filtrirane_knjige.append(knjiga)
    return filtrirane_knjige
