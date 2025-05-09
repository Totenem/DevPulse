from fastapi import FastAPI, Request
import json
from webhook.ngrokserver import ngrok_start
import threading
import os

app = FastAPI()
DATA_FILE = "data.json"

@app.get("/")
async def root():
    return {"message": "webhook for github tracking"}

@app.post("/webhook")
async def webhook(request: Request):
    try:
        event_type = request.headers.get("X-GitHub-Event", "unknown")
        data = await request.json()

        
        # What this do is it creates a unique event ID for different github events (push, pull_request, issue, etc)
        event_id = (
            data.get("head_commit", {}).get("id") or # for push events
            data.get("pull_request", {}).get("id") or # for pull_request events
            data.get("issue", {}).get("id") or # for issue events
            str(time.time())  # fallback    
        )

        # What this do is it creates a dictionary with the event id, event type, and the data from the github webhook, so taht
        # we can save it to the json file and have a record of the event and the bot will be able to read the event easily
        data_with_event = {
            "event_id": event_id,
            "event": event_type,
            **data
        }

        print("[WEBHOOK] Event received:", event_type)
        with open(DATA_FILE, "w") as f:
            json.dump(data_with_event, f, indent=4)

        return {"message": "Webhook received"}
    except Exception as e:
        print(f"[ERROR] Failed to parse JSON: {e}")
        return {"message": "Invalid JSON"}
# Start ngrok in a background thread
def start_ngrok():
    ngrok_start(8000)

threading.Thread(target=start_ngrok, daemon=True).start()
