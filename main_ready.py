
from fastapi import FastAPI, Request
import requests

app = FastAPI()

BOT_TOKEN = "7821174026:AAFTVtiYtG24mjUvK_h3ahF4MmpbILRmQ3Q"
CHAT_ID = "8079328122"

@app.post("/webhook")
async def telegram_webhook(request: Request):
    data = await request.json()
    message = data.get("message", "🚨 Сигнал получен, но без текста.")
    send_message(message)
    return {"status": "ok"}

def send_message(text: str):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text
    }
    requests.post(url, json=payload)
