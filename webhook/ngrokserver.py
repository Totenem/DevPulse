from http.server import BaseHTTPRequestHandler, HTTPServer
import logging
from pyngrok import ngrok, conf
from dotenv import load_dotenv
import os
import requests
import json
import time

# get neccessary variables from .env file
load_dotenv()

REPO_URL = os.getenv("REPO")
HOOK_ID = os.getenv("GITHUB_HOOK_ID")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


def ngrok_start(port=8000):
    
    # Get the absolute path to ngrok.yml (assumed to be in project root)
    config_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "ngrok.yml")

    # Load the local configuration
    pyngrok_config = conf.PyngrokConfig(config_path=config_path)

    # Connect to ngrok using local config
    tunnel = ngrok.connect(port, pyngrok_config=pyngrok_config)
    public_url = tunnel.public_url  # Get the public URL string
    
    # --- Update GitHub webhook ---
    url = f"https://api.github.com/repos/{REPO_URL}/hooks/{HOOK_ID}"
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    payload = {
        "config": {
            "url": f"{public_url}/webhook",
            "content_type": "json"
        }
    }
    response = requests.patch(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("[GITHUB] Webhook updated successfully.")
    else:
        print(f"[GITHUB] Failed to update webhook: {response.status_code}")
        print(response.text)

    # --- Save public URL to file for Discord bot to read ---
    with open("ngrok_url.txt", "w") as f:
        f.write(public_url)

    # --- Keep the process alive so ngrok doesn't close ---
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n[SHUTDOWN] ngrok server stopped.")

