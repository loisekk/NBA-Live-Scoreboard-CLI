<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=4,9,17&height=220&section=header&text=🏀%20NBA%20Live%20Scoreboard&fontSize=46&fontColor=ffffff&fontAlignY=38&desc=Real-Time%20NBA%20Scores%20in%20Your%20Terminal&descAlignY=58&descAlign=50" width="100%"/>

<br/>

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![API](https://img.shields.io/badge/Data-NBA%20Official%20CDN-C8102E?style=for-the-badge)](.)
[![Library](https://img.shields.io/badge/Library-requests-orange?style=for-the-badge)](.)
[![Type](https://img.shields.io/badge/Type-CLI%20Application-blueviolet?style=for-the-badge)](.)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)](.)

<br/>

> *Skip the app. Skip the browser. Get today's NBA scores — live, clean, and right in your terminal.*

<br/>

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Sample Output](#-sample-output)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-getting-started)
- [How It Works](#-how-it-works)
- [API Notes](#-api-notes)
- [Project Structure](#-project-structure)
- [Future Enhancements](#-future-enhancements)
- [Author](#-author)

---

## 🎯 Overview

**NBA Live Scoreboard Tracker** is a lightweight Python CLI tool that pulls real-time game data directly from the **official NBA CDN endpoint** — no API key, no scraping, no browser needed.

It displays today's full slate of games with scores and status in a clean, readable terminal format. Built for speed, reliability, and simplicity — it focuses only on endpoints that are publicly accessible and stable.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🏀 **Live Scores** | Fetches today's NBA games with real-time score data |
| 📊 **Game Details** | Home vs Away teams, current score, and game status |
| 🟢 **Status Indicators** | Live / Final / Scheduled — at a glance |
| ⚡ **Instant Output** | Lightweight request, no overhead, immediate terminal display |
| 🛡️ **Graceful Failures** | Handles blocked or unavailable endpoints without crashing |
| 🔓 **No Auth Required** | Uses publicly accessible NBA CDN — zero setup friction |

---

## 🖥️ Sample Output

```
╔══════════════════════════════════════════════════╗
║          🏀 NBA Live Scoreboard — Today          ║
╠══════════════════════════════════════════════════╣
║  Boston Celtics     112  vs  107  Miami Heat     ║
║  Status: LIVE — Q3 8:42                          ║
╠══════════════════════════════════════════════════╣
║  LA Lakers           98  vs  104  Golden State   ║
║  Status: FINAL                                   ║
╠══════════════════════════════════════════════════╣
║  Chicago Bulls        —  vs    —  Brooklyn Nets  ║
║  Status: SCHEDULED — 8:30 PM ET                  ║
╚══════════════════════════════════════════════════╝
```

---

## 🛠 Tech Stack

| Component | Detail |
|---|---|
| **Language** | Python 3.x |
| **Library** | `requests` — HTTP requests to NBA CDN |
| **Data Source** | NBA Official Live Data (CDN — no key required) |
| **Interface** | Terminal / CLI |

---

## 🚀 Getting Started

**Prerequisites:** Python 3.x — [Download here](https://python.org/downloads)

```bash
# Clone the repository
git clone https://github.com/loisekk/nba-scoreboard-tracker.git
cd nba-scoreboard-tracker

# Install dependency
pip install requests

# Run the tracker
python main.py
```

That's it — live NBA scores in under 5 seconds.

---

## ⚙️ How It Works

```
┌─────────────────────────────────────────────────────┐
│                   Program Flow                      │
├─────────────────────────────────────────────────────┤
│  1. Script sends GET request to NBA CDN endpoint    │
│  2. JSON response parsed for today's scoreboard     │
│  3. Each game extracted: teams, scores, status      │
│  4. Data formatted and printed to terminal          │
│  5. Graceful error handling if endpoint unavailable │
└─────────────────────────────────────────────────────┘
```

The NBA CDN endpoint returns a structured JSON payload updated in near real-time during game hours. No authentication headers, no tokens — just a clean public endpoint that delivers the goods.

---

## 🚫 API Notes

| Endpoint Type | Status | Notes |
|---|---|---|
| ✅ Live Scoreboard (CDN) | **Accessible** | Public endpoint, no auth required |
| ❌ Team PPG / Advanced Stats | **Blocked** | Requires browser-based session headers |
| ❌ Player-level Stats | **Blocked** | Rate-limited for non-browser clients |

> This project deliberately uses only **stable, public-facing endpoints** to ensure consistent performance without workarounds or spoofed headers.

---

## 📂 Project Structure

```
nba-scoreboard-tracker/
│
├── main.py            # Core logic — fetch, parse, and display scoreboard
├── requirements.txt   # Project dependencies
└── README.md          # Project documentation
```

---

## 📈 Future Enhancements

- [ ] 🔄 Auto-refresh mode — live updates every 30 seconds
- [ ] 🏆 Season standings display
- [ ] 🎯 Filter scores by favorite team
- [ ] 📅 Historical game scores by date
- [ ] 🖥️ Rich terminal UI using `rich` or `curses`
- [ ] 📲 Telegram / Discord bot integration for score alerts

---

## 👨‍💻 Author

<div align="center">

**Yash Brahmankar**

*Python Developer · Sports Data Enthusiast · CLI Builder*

<br/>

[![GitHub](https://img.shields.io/badge/GitHub-loisekk-181717?style=for-the-badge&logo=github)](https://github.com/loisekk)
[![Email](https://img.shields.io/badge/Email-yashbrahmankar95%40gmail.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:yashbrahmankar95@gmail.com)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/)

<br/>

⭐ **Found this useful? Star the repo and share it with fellow NBA fans!**

</div>

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=4,9,17&height=120&section=footer" width="100%"/>

*Built with 🏀 and Python by Yash Brahmankar*

</div>
