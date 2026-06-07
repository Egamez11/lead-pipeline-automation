

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import sqlite3

app = FastAPI()

# Modelo de Pydantic para validar los datos del Lead (Nombre, Correo, Telefono, Origen)
class Lead(BaseModel):
    nombre: str
    correo: str
    telefono: str
    origen: str

# Conexión a la base de datos SQLite
def get_db_connection():
    conn = sqlite3.connect('leads.db')
    conn.row_factory = sqlite3.Row
    return conn
# Crear la tabla de leads si no existe
def create_leads_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            correo TEXT NOT NULL,
            telefono TEXT NOT NULL,
            origen TEXT NOT NULL,
            fecha_creacion TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
# Endpoint para crear un nuevo Lead
@app.post("/leads/")
def create_lead(lead: Lead):
    conn = get_db_connection()
    cursor = conn.cursor()
    fecha_creacion = datetime.now().isoformat()
    cursor.execute('''
        INSERT INTO leads (nombre, correo, telefono, origen, fecha_creacion)
        VALUES (?, ?, ?, ?, ?)
    ''', (lead.nombre, lead.correo, lead.telefono, lead.origen, fecha_creacion))
    conn.commit()
    conn.close()
    return {"message": "Lead creado exitosamente"}

# Evento de FastAPI para crear la  tabla al iniciar la aplicacion
@app.on_event("startup")
def startup_event():
    create_leads_table()

