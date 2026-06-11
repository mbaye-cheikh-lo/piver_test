from fastapi import FastAPI
from database import get_connection
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



class Event(BaseModel):
    user_id: str
    type: str

"""
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


"""
@app.get("/events")
def get_events(user_id: str = None, type: str = None):

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM events WHERE 1=1"
    params = []

    if user_id:
        query += " AND user_id = %s"
        params.append(user_id)

    if type:
        query += " AND type = %s"
        params.append(type)

    cursor.execute(query, tuple(params))
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows