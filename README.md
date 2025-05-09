# DevPulse: A Bot for Real-Time Software Progress Tracking and Discord Reporting

![Banner Image](https://imgur.com/a/YgqgJZx)


DevPulse is an intelligent system that monitors GitHub repository activities and provides real-time updates through Discord.

You can invite the bot to your server by clicking the link below:
[Invite the Discord Bot](https://discord.com/oauth2/authorize?client_id=1370148788571738213&permissions=68608&integration_type=0&scope=bot)

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

2. **Set Up ngrok Configuration**
   Create `ngrok.yml` in the root directory:
   ```yaml
   version: 2
   authtoken: your-ngrok-authtoken
   region: us
   ```

3. **Configure GitHub Webhook**
   - Go to your repository settings
   - Navigate to Webhooks > Add webhook
   - Set Content type to `application/json`
   - Enable SSL verification
   - Select events you want to track

### Step 5: Start the System
```bash
# Start the webhook server
uvicorn webhook.webhook:app --reload --reload-dir webhook
```

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
