import os
import requests
import time

WEBHOOK = os.getenv("DISCORD_WEBHOOK")

def wyslij_alert(nazwa, cena, srednia, link):
    prog = srednia * 0.70

    if cena < prog:
        wiadomosc = (
            f"🔥 OKAZJA VINTED!\n"
            f"Produkt: {nazwa}\n"
            f"Cena: {cena} zł\n"
            f"Średnia: {srednia} zł\n"
            f"Link: {link}"
        )

        requests.post(
            WEBHOOK,
            json={"content": wiadomosc}
        )

print("Vinted Deals Bot uruchomiony!")