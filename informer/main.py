from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import time
from pydantic import BaseModel

messages = []
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class MessageModel(BaseModel):
    username: str
    text: str


@app.post("/messages")
def post_message(a: MessageModel):
    timestamp = time.time()
    messages.append([timestamp, a.username, a.text])
    return {"status": "ok"}


@app.get("/messages")
def get_messages():
    global messages
    current_time = time.time()
    # Фильтруем сообщения старше 120 секунд в самом списке
    messages = [msg for msg in messages if current_time - msg[0] <= 120]
    return [{"username": msg[1], "text": msg[2]} for msg in messages]


@app.get("/excuse")
def get_excuse():
    try:
        response = requests.get("https://excuser-three.vercel.app/v1/excuse")
        data = response.json()
        return {"excuse": data[0]['excuse']}
    except Exception:
        return {"excuse": "something went wrong :("}
