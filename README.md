2️⃣ README.md
# OpenAI Status RSS Monitor

A lightweight, modular Python script that **monitors the OpenAI Status Page** for new incidents, outages, or degradations, and prints updates in a **clean, readable format** on the console.

---

## Features

- Monitors OpenAI API status via RSS feed
- Prints **product name** and **status messages**
- Cleans HTML tags from RSS content for readability
- Preserves line breaks and bullet points
- Modular design:
  - `rss_client.py` → RSS fetching
  - `monitor.py` → Monitoring logic
  - `printer.py` → Output formatting
  - `main.py` → Entry point
- Easy to scale for multiple status pages

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/openai-status-monitor.git
cd openai-status-monitor

Create virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

Install dependencies:

pip install -r requirements.txt
Usage

Run the monitor:

python main.py

Sample output:

Monitoring OpenAI Status Page...

[2026-02-22 22:59:30]
Product: Increased latency in ChatGPT for some users
Status: Status: Resolved

All impacted services have now fully recovered.

Affected components
- Conversations (Operational)
Configuration

The RSS feed URL is set in main.py:

rss_url = "https://status.openai.com/history.rss"

Monitoring interval (seconds) can be changed:

monitor = StatusMonitor(rss_url, interval=60)  # default: 60 seconds
Optional Enhancements

Store last seen incident IDs in a file / database

Add colored console output for different status levels

Monitor multiple RSS feeds simultaneously

Send alerts via email, Slack, or Telegram

Dockerize for deployment on VPS / Render / Railway / Heroku