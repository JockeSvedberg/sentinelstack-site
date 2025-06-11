#!/usr/bin/env python3
# sentinelstack_bundle.py – Skapa ZIP med rapport + faktura + säljblad

import argparse
import json
import os
import zipfile
from glob import glob
from datetime import datetime

def bundle_files(json_path, article):
    with open(json_path, "r") as f:
        data = json.load(f)

    client = data.get("client", "Okand Kund").replace(" ", "_")
    today = datetime.now().strftime("%Y-%m-%d")
    zip_filename = f"{client}_Bundle_{article}_{today}.zip"

    # Sök efter genererade filer
    pdf_report = glob(f"{client}_AIAct_{article}_*.pdf")
    invoice_pdf = glob(f"Invoice_{client}_{article}_*.pdf")
    sales_pdf = glob("SentinelStack_Saljmall_AIAct_ASCII.pdf")

    files_to_include = pdf_report + invoice_pdf + sales_pdf

    if not files_to_include:
        print("❌ Inga filer hittades att paketera.")
        return

    with zipfile.ZipFile(zip_filename, 'w') as zipf:
        for file in files_to_include:
            zipf.write(file, arcname=os.path.basename(file))

    print(f"📦 Skapat leveranspaket: {zip_filename}")

def main():
    parser = argparse.ArgumentParser(description="Bundle rapport, faktura och säljblad till ett ZIP")
    parser.add_argument("--client", required=True, help="Sökväg till intake JSON")
    parser.add_argument("--article", required=True, help="Artikelnummer, t.ex. artikel13")
    args = parser.parse_args()
    bundle_files(args.client, args.article)

if __name__ == "__main__":
    main()
