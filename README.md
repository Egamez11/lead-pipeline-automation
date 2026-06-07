# Automated Lead Pipeline & CRM Integrator 🚀

Solución robusta de backend diseñada para automatizar la captura, validación y almacenamiento centralizado de prospectos (leads) en tiempo real, eliminando por completo la necesidad de realizar cargas manuales o tareas repetitivas de "Copy-Paste" desde formularios web o campañas de anuncios.

## 🛠️ Tecnologías Utilizadas
* **Python 3.9+** (Base del ecosistema)
* **FastAPI** (Framework asíncrono de alto rendimiento con documentación automática)
* **Pydantic** (Validación estricta de estructuras y esquemas de datos)
* **SQLite 3** (Base de datos relacional ligera, portátil y sin dependencias externas)
* **Docker** (Contenedorización completa lista para producción)

---

## 💻 Instalación y Ejecución Local

Si deseas correr el proyecto directamente en tu entorno local para desarrollo o pruebas, sigue estos pasos:

### 1. Clonar el repositorio y entrar a la carpeta:
git clone https://github.com/egamez11/lead-pipeline-automation.git
cd lead-pipeline-automation

### 2. Crear y activar un entorno virtual:
En Windows:
python -m venv .venv
.venv\Scripts\activate

En Linux/Mac:
python3 -m venv .venv
source .venv/bin/activate

### 3. Instalar dependencias:
pip install -r requirements.txt

### 4. Arrancar el servidor de desarrollo:
uvicorn main:app --reload
"El servidor local encenderá en: http://127.0.0.1:8000

------------------------------------------------------------------------------------------------------------------

🐳 Despliegue Rápido con Docker

### 1. Contruir la imagen del contenedor:
docker build -t webhook-leads .

### 2. Encender el contenedor en segundo plano:
docker run -d -p 8000:8000 --name pipeline-leads-container webhook-leads
El Webhook se levantará automáticamente dentro del contenedor y quedará escuchando en: http://localhost:8000

------------------------------------------------------------------------------------------------------------------

📊 Documentación Interactiva y Pruebas (Swagger API)

Ejemplo de Estructura de Datos (JSON esperado):
Para registrar un nuevo lead a través del endpoint POST /leads/, se debe enviar un cuerpo con el siguiente formato:

{
  "nombre": "Juan Pérez",
  "correo": "juan.perez@example.com",
  "telefono": "8112345678",
  "origen": "Landing Page Paneles Solares"
}
