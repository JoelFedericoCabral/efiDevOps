# Base de Python
FROM python:3.10-slim 

# Se establece el directorio de trabajo dentro del contenedor en /app.
WORKDIR /app  

# Se copia el archivo "requirements.txt" desde el contexto local al directorio actual del contenedor.
COPY requirements.txt ./  

RUN pip install -r requirements.txt  # Se ejecuta "pip install" para instalar las dependencias definidas en "requirements.txt".

# Se copia todo el contenido del directorio actual del contexto local al directorio actual del contenedor.
COPY . .  

# Se expone el puerto 5000 del contenedor para que sea accesible desde el exterior.
EXPOSE 5000  

# Comando para ejecutar la aplicación
CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]

# Se define el comando que se ejecutará cuando se inicie el contenedor. En este caso, se inicia la aplicación Flask y se especifica el host y el puerto en el que escuchará.
