# DevPulse: A Bot for Real-Time Software Progress Tracking and Discord Reporting

DevPulse is an intelligent system that monitors GitHub repository activities and provides real-time updates through Discord.

## 🌟 Key Features

- **Real-Time GitHub Event Tracking**
  - Monitors push events, pull requests, issues, and more
  - Automatically captures and processes repository activities
  - Uses webhook system for instant notifications

- **Intelligent Discord Integration**
  - Sends formatted updates to designated Discord channels
  - Provides context-aware summaries of development activities
  - Supports custom notification preferences

- **Secure Communication**
  - Uses ngrok for secure webhook tunneling
  - Implements GitHub webhook authentication
  - Maintains secure token management

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- A GitHub account with repository admin access
- A Discord server with admin privileges
- ngrok account (for webhook tunneling)

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/DevPulse.git
cd DevPulse
```

### Step 2: Set Up Virtual Environment
```bash
python -m venv .venv
# For Windows
.venv\Scripts\activate
# For Unix or MacOS
source .venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configuration

1. **Create Environment Variables**
   Create a `.env` file in the root directory with:
   ```env
   REPO=your-username/your-repo
   GITHUB_HOOK_ID=your-webhook-id
   GITHUB_TOKEN=your-github-token
   DISCORD_TOKEN=your-discord-token
   DISCORD_CHANNEL_ID=your-channel-id
   ```

2. **Set Up Discord Bot**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and give it a name
   - Go to the "Bot" section and click "Add Bot"
   - Copy the bot token and add it to your `.env` file as `DISCORD_TOKEN`
   - Under "Privileged Gateway Intents", enable:
     - Presence Intent
     - Server Members Intent
     - Message Content Intent
   - Go to OAuth2 > URL Generator
     - Select "bot" under Scopes
     - Select required permissions: 
       - Send Messages
       - Read Message History
       - View Channels
   - Use the generated URL to invite the bot to your server
   - Enable Developer Mode in Discord:
     - Open Discord Settings > App Settings > Advanced
     - Toggle on "Developer Mode"
   - Right-click the channel where you want updates and copy the Channel ID
   - Add the Channel ID to your `.env` file as `DISCORD_CHANNEL_ID`

3. **Set Up GitHub Access**
   - Go to GitHub Settings > Developer settings > Personal access tokens
   - Click "Generate new token" (classic)
   - Give it a descriptive name
   - Select scopes:
     - `repo` (full control of private repositories)
     - `admin:repo_hook` (for webhook management)
   - Copy the generated token and add it to your `.env` file as `GITHUB_TOKEN`

4. **Set Up ngrok Configuration**
   - Sign up for a free account at [ngrok](https://ngrok.com)
   - Get your authtoken from the ngrok dashboard
   - Create `ngrok.yml` in the root directory:
   ```yaml
   version: 2
   authtoken: your-ngrok-authtoken
   region: us
   ```

5. **Configure GitHub Webhook**
   - Start ngrok first:
     ```bash
     ngrok http 8000
     ```
   - Copy the generated HTTPS URL (e.g., https://xxxx-xx-xx-xxx-xx.ngrok.io)
   - Go to your repository settings
   - Navigate to Webhooks > Add webhook
   - Payload URL: `<ngrok-url>/webhook`
   - Set Content type to `application/json`
   - Set Secret (optional but recommended)
   - Enable SSL verification
   - Select events to track:
     - Push events
     - Pull requests
     - Issues
   - Save the webhook
   - Copy the webhook ID from the URL and add it to your `.env` file as `GITHUB_HOOK_ID`

### Step 5: Start the System
1. Start ngrok in a separate terminal:
```bash
ngrok http 8000
```

2. Start the webhook server in another terminal:
```bash
uvicorn webhook.webhook:app --reload --reload-dir webhook
```

The system should now be running and ready to:
- Receive GitHub webhook events
- Process repository activities
- Send updates to your Discord channel

## 🤝 How to Contribute

We welcome contributions to DevPulse! Here's how you can help:

1. **Fork the Repository**
   - Create your feature branch (`git checkout -b feature/AmazingFeature`)
   - Commit your changes (`git commit -m 'Add some AmazingFeature'`)
   - Push to the branch (`git push origin feature/AmazingFeature`)
   - Open a Pull Request

2. **Report Issues**
   - Use the GitHub issue tracker
   - Include detailed descriptions and steps to reproduce
   - Tag issues appropriately

3. **Suggest Improvements**
   - Open discussions for major changes
   - Share ideas in the project's discussion board
   - Help improve documentation

## 📝 Code Style Guidelines

- Follow PEP 8 guidelines for Python code
- Write meaningful commit messages
- Include comments for complex logic
- Add docstrings for functions and classes

## 📄 License

This project is licensed under the MIT License - see below for details:

```
MIT License

Copyright (c) 2024 DevPulse

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
``` 
