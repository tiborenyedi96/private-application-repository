from fastapi import FastAPI
from sqlalchemy import create_engine, text
from pydantic import BaseModel
from enum import Enum
from datetime import datetime
import os

DB_HOST = os.getenv("DB_HOST", "mysql")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASSWORD = os.getenv("DB_PASSWORD", "appsecret")
DB_NAME = os.getenv("DB_NAME", "incident_db")

engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

class Severity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"

class Status(str, Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    RESOLVED = "RESOLVED"

class Incident(BaseModel):
    id: int
    title: str
    description: str
    severity: Severity
    status: Status
    created_at: datetime

class IncidentCreate(BaseModel):
    title: str
    description: str
    severity: Severity

app = FastAPI()

@app.get("/incidents", response_model=list[Incident])
def read_incidents():
    with engine.connect() as mysql_connection:
        result = mysql_connection.execute(text("SELECT * FROM incidents ORDER BY created_at DESC;"))
        rows = result.mappings().all()
        return rows

@app.get("/health", status_code=200)
def check_health():
    return {"Status" : "OK"}

@app.post("/incidents", response_model=Incident, status_code=201)
def create_incident(payload: IncidentCreate):
    with engine.begin() as conn:
        res = conn.execute(
            text("""
                INSERT INTO incidents (title, description, severity, status, created_at)
                VALUES (:title, :description, :severity, :status, NOW())
            """),
            {
                "title": payload.title,
                "description": payload.description,
                "severity": payload.severity.value,
                "status": Status.OPEN.value
            }
        )
        new_id = res.lastrowid

        row = conn.execute(
            text("""
                SELECT id, title, description, severity, status, created_at
                FROM incidents WHERE id = :id
            """),
            {"id": new_id}
        ).mappings().one()

        return row
