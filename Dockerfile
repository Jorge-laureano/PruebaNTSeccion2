# Usamos Python 3.11
FROM python:3.11-slim

# Establecemos directorio de trabajo
WORKDIR /app

# Copiamos archivos del proyecto
COPY . /app

# Instalacion dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponemos el puerto
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "app.py"]
