# YouTube Download Bot (ytdlbot) 🌐🎥🔽

![Docker Image Status](https://github.com/tgbot-collection/ytdlbot/actions/workflows/builder.yaml/badge.svg)

## 🚀 Overview
This is a powerful and fast Telegram bot that lets you download videos from YouTube and other supported platforms like Instagram and Twitter.

## Features
- 🌟 **Fast Downloads and Uploads**
- 🔊 **Audio Conversion**
- 🔦 **Playlist Downloads**
- 🔁 **YouTube Channel Subscriptions**
- 🎲 **Progress Bar**
- 🏦 **Payments Supported**: Afdian, Buy Me a Coffee, Telegram Payment, Tron (TRX)
- 🌐 **Instagram Post and Reels Support**
- 🔍 **Multiple Resolutions**
- ✅ **Ad-Free**
- ⏬ **Cache Mechanism** for repeated downloads
- 🌐 **4 GiB File Support** (with Telegram Premium)

---

## 📂 Usage
- Add the bot: [z_tubedlbot](https://t.me/z_tubedlbot)
- Join the updates channel: [Telegram Channel](https://t.me/Zpotify1)
- Send any video link directly to the bot. Supported websites include:
  [yt-dlp Supported Sites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md).

## Limitations
- Free Users: 10 downloads/day.
- File size > 2 GiB requires a download token.
- Subscriptions limited to 3 channels per user.

---

## 🔧 Deployment

### Run Natively
1. **Install Dependencies**
   ```bash
   apt update && apt upgrade -y
   apt install git ffmpeg python3 python3-pip -y
   sudo apt install aria2 # optional
   ```
2. **Clone Repository**
   ```bash
   git clone https://github.com/zasasamar2129/ytdlbot.git
   cd ytdlbot/
   ```
3. **Set Up Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # Linux
   pip install -r requirements.txt
   ```
4. **Configure Environment Variables**
   ```bash
   export APP_ID=111 APP_HASH=111 TOKEN=123
   ```
5. **Run the Bot**
   ```bash
   python3 ytdl_bot.py
   ```

### Docker Deployment
Run with one command:
```bash
docker run -e APP_ID=111 -e APP_HASH=111 -e TOKEN=370FXI zasasamar2129/ytdlbot
```

### Deploy to Heroku
[![Deploy to Heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

### Docker-Compose
1. Download `docker-compose.yml` and create environment variables in `env/ytdl.env`.
2. Run the service:
   ```bash
   docker-compose up -d
   ```

---

## 🎥 Demo
### Normal Download
![Normal Download](assets/1_resized.jpeg)

### Instagram Post Download
![Instagram Download](assets/instagram_resized.png)

### Celery Worker Overview
![Celery Workers](assets/2_resized.jpeg)

---

## 🕐 Commands
- `/start`: Start the bot.
- `/about`: Learn about the bot.
- `/ping`: Check bot status.
- `/help`: Get usage instructions.
- `/ytdl`: Download videos in a group.
- `/settings`: Update preferences.
- `/buy`: Purchase download tokens.
- `/sub`: Subscribe to a YouTube channel.
- `/unsub`: Unsubscribe from a YouTube channel.
- `/sub_count`: View subscription status (admin only).
- `/purge`: Delete all tasks (admin only).

---

## 🛒 Donation
### Platforms
- [Buy Me a Coffee](https://www.buymeacoffee.com/zasasamar)

### Cryptocurrency
- **TRX or USDT (TRC20)**: `TFmzFJWf7t53G1f5voT1Lvsb2CSr4nfubF`

![Wallet QR Code](assets/wallet_resized.jpeg)

---

## 🔒 License
This project is licensed under the Apache License 2.0.

---

### 📊 Test Data
#### Test Video
- [YouTube Video](https://www.youtube.com/watch?v=BaW_jenozKc)

#### Test Playlist
- [YouTube Playlist](https://www.youtube.com/playlist?list=PL1Hdq7xjQCJxQnGc05gS4wzHWccvEJy0w)

#### Test Instagram
- **Single Image**: [Example](https://www.instagram.com/p/CXpxSyOrWCA/)
- **Single Video**: [Example](https://www.instagram.com/p/Cah_7gnDVUW/)
- **Reels**: [Example](https://www.instagram.com/p/C0ozGsjtY0W/)
- **Image Carousel**: [Example](https://www.instagram.com/p/C0ozPQ5o536/)
- **Video Carousel**: [Example](https://www.instagram.com/p/C0ozhsVo-m8/)

---

## 🌍 Community
Join our [Telegram Channel](https://t.me/Zpotify1) for updates and support.

---

### 🔧 Note
For resized images, replace placeholders (`assets/1_resized.jpeg`, etc.) with optimized versions of your current images (recommended size: 800px width).

