from pydantic import BaseModel

# Pydantic klase su read-only
class BaseProizvod(BaseModel):
    id: int
    naziv: str
    boja: str
    cijena: float

class Film(BaseModel):
    id: int
    naziv: str
    genre: str
    godina: int

class CreateProizvod(BaseModel):
    naziv: str
    boja: str
    cijena: float

class ResponseProizvod(CreateProizvod):
    id: int


class CreateFilm(BaseModel):
    naziv: str
    genre: str
    godina: int

class ResponseFilm(CreateFilm):
    id: int