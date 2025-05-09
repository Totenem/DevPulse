import os
import sys
import discord
from discord.ext import tasks
from dotenv import load_dotenv
import json
import time

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_ID = int(os.getenv("DISCORD_CHANNEL_ID"))

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

last_event_id = None  # To avoid duplicate sends


def read_latest_event():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"[ERROR] Could not read data.json: {e}")
        return None


def format_event(data):
    event_type = data.get("event", "unknown")

    if event_type == "push":
        pusher = data["pusher"]["name"]
        branch = data["ref"].split("/")[-1]
        commits = data.get("commits", [])
        commit_msgs = "\n".join([f"- {c['message']}" for c in commits])
        return f"📦 **Push Event**\n**Pusher:** {pusher}\n**Branch:** {branch}\n**Commits:**\n{commit_msgs}"

    elif event_type == "pull_request":
        pr = data["pull_request"]
        user = pr["user"]["login"]
        title = pr["title"]
        action = data.get("action")
        return f"🔃 **Pull Request {action.title()}**\n**By:** {user}\n**Title:** {title}"

    elif event_type == "issues":
        issue = data["issue"]
        user = issue["user"]["login"]
        title = issue["title"]
        action = data.get("action")
        return f"🐞 **Issue {action.title()}**\n**By:** {user}\n**Title:** {title}"

    elif event_type == "pull_request_review":
        review = data["review"]
        user = review["user"]["login"]
        state = review["state"]
        return f"📝 **Pull Request Review**\n**By:** {user}\n**State:** {state}"

    elif event_type == "deployment":
        user = data["deployment"]["creator"]["login"]
        environment = data["deployment"]["environment"]
        return f"🚀 **Deployment Triggered**\n**By:** {user}\n**Environment:** {environment}"

    elif event_type == "deployment_status":
        status = data["deployment_status"]["state"]
        return f"📡 **Deployment Status Updated**\n**Status:** {status}"

    elif event_type == "member":
        action = data.get("action")
        member = data["member"]["login"]
        return f"👥 **Collaborator {action.title()}**\n**User:** {member}"

    else:
        return f"🔔 **Unhandled GitHub Event**: {event_type}"


@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")
    check_for_event.start()


@tasks.loop(seconds=5)
async def check_for_event():
    global last_event_id
    channel = client.get_channel(CHANNEL_ID) 
    data = read_latest_event()

    if not data or "event_id" not in data:
        return

    if data["event_id"] != last_event_id:
        message = format_event(data)
        await channel.send(message)
        last_event_id = data["event_id"]


client.run(DISCORD_TOKEN)