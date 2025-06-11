#!/usr/bin/env python3
# sentinelstack_invoice_profile.py – Skapar faktura PDF från intake.json

from fpdf import FPDF
from datetime import datetime
import argparse
import json
import os

def generate_invoice(json_path, article, amount=4950):
    with open(json_path, "r") as f:
        data = json.load(f)

    client = data.get("client", "Okänd Kund")
    contact = data.get("contact", "")
    email = data.get("email", "")
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"Invoice_{client.replace(' ', '_')}_{article}_{today}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="FAKTURA", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Kund: {client}", ln=True)
    pdf.cell(200, 10, txt=f"Kontakt: {contact}", ln=True)
    pdf.cell(200, 10, txt=f"E-post: {email}", ln=True)
    pdf.cell(200, 10, txt=f"Datum: {today}", ln=True)
    pdf.cell(200, 10, txt=f"Referens: AI Act Rapport - {article}", ln=True)
    pdf.cell(200, 10, txt=f"Belopp: {amount} SEK exkl. moms", ln=True)
    pdf.cell(200, 10, txt="Bankgiro: 123-4567", ln=True)
    pdf.cell(200, 10, txt="Betalningsvillkor: 10 dagar", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, "Tack för att du använder SentinelStack AI Compliance Suite. Rapporten är genererad enligt AI Act Artikel " + article + ".")

    pdf.output(filename)
    print(f"🧾 Faktura skapad: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Skapa faktura PDF från intake.json")
    parser.add_argument("--client", required=True, help="Sökväg till intake JSON-fil")
    parser.add_argument("--article", required=True, help="Artikelnummer (ex: artikel13)")
    parser.add_argument("--amount", type=int, default=4950, help="Fakturabelopp (SEK)")
    args = parser.parse_args()
    generate_invoice(args.client, args.article, args.amount)

if __name__ == "__main__":
    main()
