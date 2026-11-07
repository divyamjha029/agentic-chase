
from fastapi import FastAPI
import models
from database import engine

# Automatically generates the agentic_chase.db SQLite file and relational tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Agentic Chase AI Backend")

@app.get("/")
def read_root():
    return {
        "status": "Agentic Chase AI Backend is running!",
        "database": "Connected & Isolated Context Ready"
    }
