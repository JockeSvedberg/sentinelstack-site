#!/usr/bin/env python3
# sentinelstack_invoice_fixed.py – Skapar PDF-faktura utan Unicode-fel

from fpdf import FPDF
from datetime import datetime
import argparse

def generate_invoice(client, article, amount=4950):
    today = datetime.now().strftime("%Y-%m-%d")
    filename = f"Invoice_{client}_{article}_{today}.pdf"

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="FAKTURA", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Kund: {client}", ln=True)
    pdf.cell(200, 10, txt=f"Datum: {today}", ln=True)
    pdf.cell(200, 10, txt=f"Referens: AI Act Rapport - {article}", ln=True)
    pdf.cell(200, 10, txt=f"Belopp: {amount} SEK exkl. moms", ln=True)
    pdf.cell(200, 10, txt="Bankgiro: 123-4567", ln=True)
    pdf.cell(200, 10, txt="Betalningsvillkor: 10 dagar", ln=True)
    pdf.ln(10)
    pdf.multi_cell(0, 10, "Tack for att du anvander SentinelStack AI Compliance Suite. Rapporten ar genererad enligt AI Act Artikel " + article + ".")

    pdf.output(filename)
    print(f"🧾 Faktura skapad: {filename}")

def main():
    parser = argparse.ArgumentParser(description="Skapa faktura for AI Act Compliance-rapport")
    parser.add_argument("--client", required=True, help="Klientnamn")
    parser.add_argument("--article", required=True, help="Artikelnummer (ex: artikel13)")
    parser.add_argument("--amount", type=int, default=4950, help="Fakturabelopp (SEK)")
    args = parser.parse_args()
    generate_invoice(args.client, args.article, args.amount)

if __name__ == "__main__":
    main()
