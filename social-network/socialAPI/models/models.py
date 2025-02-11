from pydantic import BaseModel, Field
from datetime import datetime

class ObjavaCreate(BaseModel):
    korisnik: str = Field(..., max_length=20)
    tekst: str = Field(..., max_length=280)

class Objava(ObjavaCreate):
    id: int
    vrijeme: datetime

class AuthRequest(BaseModel):
    korisnicko_ime: str
    lozinka: str
