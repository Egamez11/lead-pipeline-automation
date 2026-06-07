
# 1. Usar una imagen oficial de Python ligera como base
FROM python:3.9-slim

2. Configurar el directorio de trabajo, copiar el requirements.txt e instalar las dependencias
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#. Copiar el resto del código y exponer el puerto 8000 para FastAPI con Uvicorn
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
