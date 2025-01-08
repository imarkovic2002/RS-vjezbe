from pydantic import BaseModel

# Pydantic klase su read-only
class BaseProizvod(BaseModel):
    naziv: str
    boja: str
    cijena: float

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