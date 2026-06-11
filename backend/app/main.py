from fastapi import FastAPI
from database import get_connection
from pydantic import BaseModel

app = FastAPI()

class Event(BaseModel):
    user_id: str
    type: str


@app.post("/events")
def create_event(event: Event):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO events (user_id, type) VALUES (%s, %s)",
        (event.user_id, event.type)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Event created"}


