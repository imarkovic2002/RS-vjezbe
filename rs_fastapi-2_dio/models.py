from pydantic import BaseModel
from typing import Optional, Literal,TypedDict
from datetime import datetime


class FilmResponse(BaseModel):
    id: int
    naziv: str
    genre: str
    godina: int

class Korisnik(BaseModel):
    id: int
    ime: str
    prezime: str
    email: str
    dob: int 
    racun_aktivan: bool = True

class Proizvod(BaseModel):
    id: int
    naziv: str
    cijena: float
    kategorija: str
    boja: str
    
class StavkaNarudzbe(BaseModel):
    id: int
    proizvod: Proizvod
    narucena_kolicina: int
    ukupna_cijena: float

class Narudzba(BaseModel):
    id: int
    ime_kupca: str
    prezime_kupca: str
    stavke: list[StavkaNarudzbe]
    ukupna_cijena: float

class Loto(BaseModel):
    id: int
    rezultati: dict[int, int]

class GeoLokacija(BaseModel):
    id: int
    koordinate: tuple[float, float]

class Inventura(BaseModel):
    id:int
    naziv_skladista: str
    proizvodi: dict[str, int]

class Kolegij(BaseModel):
    id: int
    naziv: str
    semestar: Literal[1,2,3,4,5,6]
    ECTS: Optional[int] = 6
    opis: str
    profesor: str

class Automobil(BaseModel):
    id: int
    marka: str
    model: str
    boja: Literal["crvena", "plava", "zelena", "bijela", "crna"]
    godina_proizvodnje: Optional[int]
    snaga_motora: dict[str,int]
    cijena: dict[str,float]

class BaseProizvod(BaseModel):
    naziv: str
    cijena: float
    kategorija: str
    boja: str

class RequestProizvod(BaseProizvod): # nasljeđujemo atribute iz BaseProizvod modela
    pass # ne dodajemo niti jedan novi atribut

class ResponseProizvod(BaseProizvod): # nasljeđujemo atribute iz BaseProizvod modela
    id: int
    cijena_pdv: float

class KorisnikBase(BaseModel):
    ime: str
    prezime: str
    email: str

class KorisnikCreate(KorisnikBase):
    lozinka_txt: str

class KorisnikResponse(KorisnikBase):
    lozinka_hash: str
    datum_registracije: datetime

## 2.5 Zadaci za vježbu: Definicija složenijih Pydantic modela

# 1. zadatak
class Izdavač(BaseModel):
    naziv: str
    adresa: str

class Knjiga(BaseModel):
    naslov: str
    ime_autora: str
    prezime_autora: str
    godina_izdavanja: int = datetime.now().year
    broj_stranica: int
    izdavač: Izdavač

# 2. zadatak
class Admin(BaseModel):
    ime: str
    prezime: str
    korisnicko_ime: str
    email: str
    ovlasti: list[Literal["dodavanje", "brisanje", "azuriranje", "citanje"]] = []

# 3. zadatak
class stolInfo(TypedDict):
    broj: int
    lokacija: str

class Jelo(BaseModel):
    id: int
    naziv: str
    cijena: float

class RestaurantOrder(BaseModel):
    id: int 
    ime_kupca: str
    stol_info:stolInfo
    jelo: list[Jelo]

# 4. zadatak
class CCTV_frame(BaseModel):
    id: int
    vrijeme_snimanja: datetime
    koordinate: tuple[float,float] = (0.0, 0.0)