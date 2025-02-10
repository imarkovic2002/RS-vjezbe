from fastapi import FastAPI, HTTPException
from models.models import Objava, ObjavaCreate
from datetime import datetime
from typing import List

app = FastAPI()

objave = []

@app.post("/objava", response_model=Objava)
def dodaj_objavu(objava: ObjavaCreate):
    nova_objava = Objava(id=len(objave) + 1, vrijeme=datetime.utcnow(), **objava.dict())
    objave.append(nova_objava)
    return nova_objava

@app.get("/objava/{id}", response_model=Objava)
def dohvati_objavu(id: int):
    for objava in objave:
        if objava.id == id:
            return objava
    raise HTTPException(status_code=404, detail="Objava nije pronađena")

@app.get("/korisnici/{korisnik}/objave", response_model=List[Objava])
def dohvati_objave_korisnika(korisnik: str):
    return [objava for objava in objave if objava.korisnik == korisnik]

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=3500)