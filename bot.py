import os
import requests

WEBHOOK_URL = os.environ.get("DISCORD_WEBHOOK")

def send_alert(message):
    requests.post(
        WEBHOOK_URL,
        json={"content": message}
    )

if __name__ == "__main__":
    send_alert("Vinted Deals Bot został uruchomiony!")
