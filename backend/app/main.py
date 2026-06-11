from fastapi import FastAPI
from database import get_connection
from pydantic import BaseModel
from datetime import datetime

class Event(BaseModel):
    user_id: str
    type: str

app = FastAPI()
"""
@app.get("/events")
def get_events():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM events")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows
"""

@app.post("/events")
def create_event(user_id: str, type: str):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO events (user_id, type) VALUES (%s, %s)",
        (user_id, type)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Event created"}