# efi

# tutorial
1. Construir la aplicacion
```bash
sudo docker-compose build
```

2. Correr la aplicacion
```bash
sudo docker-compose up -d
```

3. Correr la ultima migracion en caso de ser la primera vez
```bash
sudo docker-compose run api flask db upgrade
```