#!/usr/bin/env python3
# sentinelstack_intake.py – Samla in kundinfo till .json-fil

import argparse
import json
import os
from datetime import datetime

def run_intake(args):
    data = {
        "client": args.name,
        "contact": args.contact,
        "email": args.email,
        "ai_usage": args.ai,
        "business_type": args.usage,
        "created": datetime.now().isoformat()
    }

    filename = f"{args.name.replace(' ', '_')}_intake.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"✔️ Kundinfo sparad i: {filename}")
    print("📄 Nu kan du köra: auto, invoice, bundle, etc baserat på denna input.")

def main():
    parser = argparse.ArgumentParser(description="Intake CLI – samla kunddata")
    parser.add_argument("--name", required=True, help="Företagsnamn")
    parser.add_argument("--contact", required=True, help="Kontaktperson")
    parser.add_argument("--email", required=True, help="E-postadress")
    parser.add_argument("--ai", required=True, help="Hur används AI?")
    parser.add_argument("--usage", required=True, help="Typ av verksamhet")
    args = parser.parse_args()
    run_intake(args)

if __name__ == "__main__":
    main()
