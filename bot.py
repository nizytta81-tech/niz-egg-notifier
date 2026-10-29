import os
import requests

# NIZ EGG NOTIFIER
# Mengirim notifikasi melalui API Telegram.

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

def send_notification(message):
    if not TOKEN or not CHAT_ID:
        print("Token atau Chat ID Telegram belum diatur.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    try:
        response = requests.post(
            url,
            json={"chat_id": CHAT_ID, "text": message},
            timeout=15
        )
        response.raise_for_status()
        print("Notifikasi berhasil dikirim.")
    except requests.RequestException as error:
        print(f"Gagal mengirim notifikasi: {error}")

if __name__ == "__main__":
    send_notification(
        "NIZ EGG NOTIFIER aktif! "
        "Bot siap menerima integrasi sumber informasi Egg."
    )
