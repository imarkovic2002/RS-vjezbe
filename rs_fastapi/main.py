from fastapi import FastAPI
from models import BaseProizvod,CreateProizvod, CreateFilm, ResponseFilm, Film

app = FastAPI()

## Vjezba 
@app.get("/")
def read_root():
    return {"message": "Hello World!"}

proizvodi = [
    {"id": 1, "naziv": "majica", "boja": "plava", "cijena": 50},
    {"id": 2, "naziv": "hlače", "boja": "crna", "cijena": 100},
    {"id": 3, "naziv": "tenisice", "boja": "bijela", "cijena": 150},
    {"id": 4, "naziv": "kapa", "boja": "smeđa", "cijena": 20}
]

@app.get("/proizvodi")
def get_proizvodi():
    return proizvodi

## ROUTE parameters
@app.get("/proizvodi/{naziv}")
def get_proizvodi_by_name(naziv: str):
    trazeni_proizvod = next((proizvod for proizvod in proizvodi if proizvod["naziv"] == naziv), None)
    return trazeni_proizvod

## REQUEST body
@app.post("/proizvodi", response_model = BaseProizvod)
def add_proizvod(proizvod: CreateProizvod):
    new_id = len(proizvodi) + 1
    proizvod_s_id : BaseProizvod = {"id" : new_id, **proizvod.model_dump()}
    proizvodi.append(proizvod_s_id)
    return proizvod_s_id

## QUERY parametri
@app.get("/proizvodi")
def get_proizvodi_by_query(boja: str, max_cijena: int):
    trazeni_proizvod = [proizvod for proizvod in proizvodi if proizvod["boja"]==boja and proizvod["cijena"] <= max_cijena]
    return trazeni_proizvod
### mozemo imati i više query parametara ili samo jedan

@app.patch("/skladiste/{id_skladiste}")
def update_skladiste(proizvod:dict, id_skladiste: int, kategorija:str = "gradevinski_materijal"):
    pass


# Moramo znati 3 načina ovo query, body i route
## Razlika je: 
### ROUTE parametri -> obavezno se navode u URL putanji (dekoratoru) npr. @app.get("/proizvodi", proizvod_id: int)

### BODY parametri -> ne navode se u URL putanji (dekoratoru), nego u definiciji funkcije hintanjem dict ili Pydantic modela.

### QUERY parametri -> ne navode se u URL putanji (dekoratoru), nego se deklarira kao argument funkcije
# Moguće je kombinirati sva tri pristupa. 



# 2.2 Zadaci za vježbu - Osnove definicije ruta i Pydantic modela

# 1. i 2.  zadatak
filmovi = [
    {"id": 1, "naziv": "Titanic", "genre": "drama", "godina": 1997},
    {"id": 2, "naziv": "Inception", "genre": "akcija", "godina": 2010},
    {"id": 3, "naziv": "The Shawshank Redemption", "genre": "drama", "godina": 1994},
    {"id": 4, "naziv": "The Dark Knight", "genre": "akcija", "godina": 2008}
]

# 1. i 2. zadatak
@app.get("/filmovi", response_model=list[Film])
def get_filmovi():
    return {"Filmovi": filmovi}

# 3. zadatak
@app.get("/filmovi/{id}", response_model=Film)
def get_film_by_id(id:int):
    trazeni_film = next((film for film in filmovi if film["id"] == id), None)
    return trazeni_film

# 4. zadatak
@app.post("/filmovi", response_model=ResponseFilm)
def add_film(film: CreateFilm):
    novi_id = len(filmovi) + 1
    film_s_id : ResponseFilm = {"id" : novi_id, **film.model_dump()}
    filmovi.append(film_s_id)
    return film_s_id

# 5. zadatak
@app.get("/filmoviQuery", response_model=list[Film])
def get_filmovi_by_query(genre : str = None, min_godina : int = 2000):
    pronadeni_filmovi = [film for film in filmovi if (genre is None or film["genre"] == genre and film["godina"] >= min_godina)]
    return pronadeni_filmovi