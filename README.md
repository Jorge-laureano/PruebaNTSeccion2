# PruebaNT Sección 2 - API Flask

## Descripción
Este proyecto es una API Flask que calcula el número faltante en un conjunto de los primeros 100 números naturales. Permite al usuario ingresar manualmente un número o generar uno aleatorio, y muestra visualmente todos los números resaltando el número faltante.

## Requisitos
- Docker
- Docker Compose

## Archivos principales
- `app.py` - Aplicación Flask principal
- `app_numbers_grid.py` - Clase que representa los números naturales y el número faltante
- `Dockerfile` - Definición de la imagen Docker
- `docker-compose.yml` - Configuración de servicios para levantar la app
- `requirements.txt` - Dependencias de Python

## Ejecución con Docker

1. Clona el repositorio:
```bash
git clone https://github.com/Jorge-laureano/PruebaNTSeccion2.git
cd PruebaNTSeccion2
```

2. Construye y levanta el contenedor con Docker Compose:
```bash
docker-compose up --build
```

3. Accede a la aplicación desde tu navegador:
```
http://localhost:5000
```

## Uso
- Ingresa un número en el input manual y presiona "Calcular" para ver el número faltante.
- Presiona "Número aleatorio" para generar un número aleatorio faltante y visualizarlo.
- Todos los números del 1 al 100 se muestran en una cuadrícula, con el número faltante resaltado.

## Notas
- La aplicación se ejecuta directamente dentro de un contenedor Docker, no requiere configuración adicional de base de datos.
- El contenedor expone el puerto 5000 para acceso desde tu navegador local.
