from fastapi import FastAPI, HTTPException
import requests
from models.models import Objava, ObjavaCreate, AuthRequest
from datetime import datetime
from typing import List

app = FastAPI()

objave = []

@app.post("/objava", response_model=Objava)
def dodaj_objavu(objava: ObjavaCreate):
    nova_objava = Objava(id=len(objave) + 1, vrijeme=datetime.utcnow(), **objava.dict())
    objave.append(nova_objava)
    return nova_objava

@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
def dohvati_objave_korisnika(auth: AuthRequest):
    # Pozivamo authAPI za provjeru prijave
    auth_response = requests.post("http://authapi:9000/login", json=auth.dict())

    if auth_response.status_code != 200 or not auth_response.json().get("authorized"):
        raise HTTPException(status_code=401, detail="Neispravni korisnički podaci")

    return [objava for objava in objave if objava.korisnik == auth.korisnicko_ime]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3500)