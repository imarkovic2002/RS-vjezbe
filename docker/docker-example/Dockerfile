# koristi Python 3 kao bazni predložak
FROM python:3

# postavlja radni direktorij na /app
WORKDIR /app

# kopira sve datoteke i direktorije iz trenutnog direktorija u /app direktorij kontejnera
COPY main.py /app

# pokreće Python aplikaciju prilikom pokretanja kontejnera
CMD ["python", "main.py"]

# instalira Python paket requests prilikom izgradnje predloška
RUN pip install requests

# dokumentira port 8080 na kojem će kontejner slušati
EXPOSE 8080