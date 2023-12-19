# Usa una imagen de Python como base
FROM python:3.8-slim

# Establece el directorio de trabajo en /app
WORKDIR /app

# Copia el contenido actual al contenedor en /app
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto 5000
EXPOSE 9090

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]