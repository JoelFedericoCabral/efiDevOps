# MINIBLOG API (EFI)

Bienvenido a la API Miniblog, una plataforma diseñada para permitir a los usuarios compartir posteos y comentarios.

## Con esta API podras:

- **Registrarte y Autenticarte:** Crea tu cuenta y accede de forma segura para comenzar a interactuar con la plataforma.

- **Publicar Contenido:** Comparte tus ideas y pensamientos mediante publicaciones que pueden ser vistas y comentadas por otros usuarios.

- **Interactuar con la Comunidad:** Comenta las publicaciones de otros usuarios, participa en discusiones y comparte tus opiniones.

- **Seguridad y Privacidad:** Mantenemos tus datos seguros y respetamos tu privacidad.

# Tutorial

1. Construir la aplicacion
```bash
sudo docker-compose build
```
2. Una vez que la aplicación esté construida, puedes ejecutarla con el siguiente comando:
```bash
sudo docker-compose up -d
```
Tambien podemos hacer esto en una sola linea de comando:
```bash
sudo docker-compose up --build -d
```
3. Ejecutar la última migración (Primera vez)
Si estás ejecutando la aplicación por primera vez, debes realizar la última migración. Utiliza el siguiente comando:
```bash
sudo docker-compose run api flask db upgrade
```
## Uso de la API
Puedes acceder a la API a través de las rutas definidas en tu aplicación Flask. Asegúrate de revisar la documentación de la API para conocer las rutas disponibles y cómo interactuar con ellas.

## Requisitos
Asegúrate de tener instalados los siguientes componentes antes de ejecutar la aplicación:

[DOCKER](https://www.docker.com/)
  