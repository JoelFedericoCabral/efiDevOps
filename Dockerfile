# Base de Python
FROM python:3.10-slim

# Crear app directorio
WORKDIR /app

# Instalar app dependencias
COPY requirements.txt ./

RUN pip install -r requirements.txt

# Mover el código base dentro del contenedor
COPY . .

EXPOSE 5000
CMD [ "flask", "run","--host","0.0.0.0","--port","5000"]

