from fastapi import FastAPI
from models import CreateProizvod,ResponseProizvod, CreateFilm,ResponseFilm

app = FastAPI()

proizvodi = [
    {
        "id": 1, "naziv": "Miš", "cijena": 50
    },
    {
        "id": 2, "naziv": "Tipkovnica", "cijena": 50
    },
]
@app.get("/proizvodi/{proizvod_id}")
def get_proizvodi(proizvod_id : int):

    trazeni_proizvod = next((proizvod for proizvod in proizvodi if proizvod["id"] == proizvod_id), None)

    #razlicito je od comprehensiona jer cemo dobiti listu i bolje je ovo koristiti

    return {"trazeni_proizvod": trazeni_proizvod}

# HTTP body
@app.post("/proizvodi")
def dodaj_proizvod(proizvod : dict):
    print("Proizvod:", proizvod)
    new_id = len(proizvodi) + 1
    proizvod["id"] = new_id
    proizvodi.append(proizvod)

    return {"status": "OK"} 

# Query parametri - nije dovršeno
@app.post("/proizvodi")
def dodaj_proizvod(proizvod : CreateProizvod):
    print("Proizvod:", proizvod)

    new_id = len(proizvodi) + 1

    proizvod_sa_id = ResponseProizvod(id=new_id, **proizvod.model_dump())

    proizvodi.append(proizvod)

    return {"status": proizvod_sa_id} 


# Moramo znati 3 načina ovo query, body i route




# 2.2 Zadaci za vježbu - Osnove definicije ruta i Pydantic modela

# 1. zadatak
filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

@app.get("/filmovi", response_model=list[ResponseFilm])
def get_filmovi():
    return filmovi

# 3. zadatak
@app.get("/filmovi/{id}", response_model=ResponseFilm)
def get_film(id:int):
    pronadeni_film = next((film for film in filmovi if film["id"]== id), None)
    return pronadeni_film

