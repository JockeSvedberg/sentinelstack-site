#!/usr/bin/env python3
# sentinelstack_draft_email.py – Skapa e-postutkast (.txt) från kunddata

import argparse
import json
from datetime import datetime

def generate_email(json_path, article):
    with open(json_path, "r") as f:
        data = json.load(f)

    client = data.get("client", "Kund")
    contact = data.get("contact", "")
    email = data.get("email", "")
    today = datetime.now().strftime("%Y-%m-%d")

    subject = f"Leverans: AI Act-granskning för {client}"
    body = f"""Hej {contact},

Här kommer din AI Act-granskning enligt överenskommelse.

I bifogad ZIP-fil hittar du:
- PDF-rapport enligt Artikel {article}
- Faktura (4950 SEK exkl. moms)
- Säljblad med sammanfattning av tjänsten

Betalning sker via faktura (10 dagar) – QR för Swish finns i PDF:en eller som separat bild.

Om du har frågor eller vill ta nästa steg (t.ex. full compliance-paket), hör gärna av dig.

Tack för förtroendet!

Med vänliga hälsningar,  
Joakim Svedberg  
Joakim@sentinelstack.tech  
SentinelStack Compliance Suite
"""

    filename = f"{client.replace(' ', '_')}_email_draft_{article}_{today}.txt"
    with open(filename, "w") as f:
        f.write("Till: " + email + "\n")
        f.write("Ämne: " + subject + "\n\n")
        f.write(body)

    print(f"📧 Utkast sparat som: {filename}")
    print("✉️ Du kan nu öppna, läsa igenom och manuellt skicka mejlet.")

def main():
    parser = argparse.ArgumentParser(description="Skapa e-postutkast från intake + artikel")
    parser.add_argument("--client", required=True, help="Sökväg till intake JSON")
    parser.add_argument("--article", required=True, help="Artikelnummer (ex: artikel13)")
    args = parser.parse_args()
    generate_email(args.client, args.article)

if __name__ == "__main__":
    main()
