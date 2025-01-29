FROM python:3.11-slim

# Postavljanje radnog direktorija
WORKDIR /app

# Kopiranje svih datoteka
COPY . /app

# Instalacija ovisnosti
RUN pip install -r requirements.txt

# Izlaganje porta
EXPOSE 9000

# Pokretanje aplikacije
CMD ["python", "app.py"]
