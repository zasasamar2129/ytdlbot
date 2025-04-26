#!/usr/local/bin/python3
# coding: utf-8

# ytdlbot - constant.py
# 8/16/21 16:59
#

__author__ = "ZACO <zasasamar2129@gmail.com>"

import os

from config import (
    AFD_LINK,
    COFFEE_LINK,
    ENABLE_CELERY,
    FREE_DOWNLOAD,
    REQUIRED_MEMBERSHIP,
    TOKEN_PRICE,
)
from database import InfluxDB
from utils import get_func_queue


class BotText:
    start = """
    🎬 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗬𝗼𝘂𝗧𝘂𝗯𝗲 𝗗𝗼𝘄𝗻𝗹𝗼𝗮𝗱 𝗕𝗼𝘁  �
    
    ✦ Type /help for guidance 
    ✦ Backup bot: @z_tubedlbot
    ✦ Join our channel: 𝙩.𝙢𝙚/𝙕𝙥𝙤𝙩𝙞𝙛𝙮1
    
    ✧･ﾟ: *✧･ﾟ:*  *:･ﾟ✧*:･ﾟ✧
    """

    help = """
    🆘 𝗛𝗲𝗹𝗽 𝗖𝗲𝗻𝘁𝗲𝗿 🆘

1️⃣ If the bot isn't responding, please retry or join:
   🔗 𝘵.𝘮𝘦/𝘡𝘱𝘰𝘵𝘪𝘧𝘺1 for updates

2️⃣ Source code available at:
   🌟 𝗴𝗶𝘁𝗵𝘂𝗯.𝗰𝗼𝗺/𝘇𝗮𝘀𝗮𝘀𝗮𝗺𝗮𝗿𝟮𝟭𝟮𝟵/𝘆𝘁𝗱𝗹𝗯𝗼𝘁
   
   ✦ ⋆ ⋆ ✦
    """

    about = """
    𝖄𝖔𝖚𝖙𝖚𝖇𝖊 𝕯𝖔𝖜𝖓𝖑𝖔𝖆𝖉 𝕭𝖔𝖙 𝕴𝖓𝖋𝖔
    
    ✧ Developed by @Itachi2129
    ✧ Open source on GitHub:
      𝓰𝓲𝓽𝓱𝓾𝓫.𝓬𝓸𝓶/𝔃𝓪𝓼𝓪𝓼𝓪𝓶𝓪𝓻2129/𝔂𝓽𝓭𝓵𝓫𝓸𝓽
    
    ✦･ﾟ✧･ﾟ✦･ﾟ✧･ﾟ✦
    """
    buy = f"""
**Terms:**
1. You can use this bot to download video for {FREE_DOWNLOAD} times within a 24-hour period.

2. You can buy additional download tokens, valid permanently.

3. Refunds are possible, contact me if you need that @Itachi2129

4. Download for paid user will be automatically changed to Local mode to avoid queuing.

5. Paid user can download files larger than 2GB.

**Price:**
valid permanently
1. 1 USD == {TOKEN_PRICE} tokens
2. 7 CNY == {TOKEN_PRICE} tokens
3. 10 TRX == {TOKEN_PRICE} tokens

**Payment options:**
Pay any amount you want. For example you can send 20 TRX for {TOKEN_PRICE * 2} tokens.
1. AFDIAN(AliPay, WeChat Pay and PayPal): {AFD_LINK}
2. Buy me a coffee: {COFFEE_LINK}
3. Telegram Bot Payment(Stripe), please click Bot Payment button.
4. TRON(TRX), please click TRON(TRX) button.

**After payment:**
1. Afdian: attach order number with /redeem command (e.g., `/redeem 123456`).
2. Buy Me a Coffee: attach email with /redeem command (e.g., `/redeem 123@x.com`). **Use different email each time.**
3. Telegram Payment & Tron(TRX): automatically activated within 60s. Check /start to see your balance.

Want to buy more token with Telegram payment? Let's say 100? Here you go! `/buy 123`
    """

    private = "This bot is for private use"

    membership_require = f"You need to join this group or channel to use this bot\n\nhttps://t.me/{REQUIRED_MEMBERSHIP}"

    settings = """
Please choose the preferred format and video quality for your video. These settings only **apply to YouTube videos**.

High quality is recommended. Medium quality aims to 720P, while low quality is 480P.

If you choose to send the video as a document, it will not be possible to stream it.

Your current settings:
Video quality: **{0}**
Sending format: **{1}**
"""
    custom_text = os.getenv("CUSTOM_TEXT", "")

    premium_warning = """
    Your file is too big, do you want me to try to send it as premium user? 
    This is an experimental feature so you can only use it once per day.
    Also, the premium user will know who you are and what you are downloading. 
    You may be banned if you abuse this feature.
    """

    @staticmethod
    def get_receive_link_text() -> str:
        reserved = get_func_queue("reserved")
        if ENABLE_CELERY and reserved:
            text = f"Your tasks was added to the reserved queue {reserved}. Processing...\n\n"
        else:
            text = "Your task was added to active queue.\nProcessing...\n\n"

        return text

    @staticmethod
    def ping_worker() -> str:
        from tasks import app as celery_app

        workers = InfluxDB().extract_dashboard_data()
        # [{'celery@BennyのMBP': 'abc'}, {'celery@BennyのMBP': 'abc'}]
        response = celery_app.control.broadcast("ping_revision", reply=True)
        revision = {}
        for item in response:
            revision.update(item)

        text = ""
        for worker in workers:
            fields = worker["fields"]
            hostname = worker["tags"]["hostname"]
            status = {True: "✅"}.get(fields["status"], "❌")
            active = fields["active"]
            load = "{},{},{}".format(fields["load1"], fields["load5"], fields["load15"])
            rev = revision.get(hostname, "")
            text += f"{status}{hostname} **{active}** {load} {rev}\n"

        return text
