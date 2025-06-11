#!/usr/bin/env python3
# sentinelstack_fullpipeline.py – Intake → Rapport → Faktura → Bundle

import argparse
import os
import subprocess

def run_pipeline(name, contact, email, ai, usage, article):
    json_filename = f"{name.replace(' ', '_')}_intake.json"

    # 1. Intake
    print("📝 Steg 1: Skapar intake...")
    intake_cmd = f'python3 sentinelstack_intake.py --name "{name}" --contact "{contact}" --email {email} --ai "{ai}" --usage "{usage}"'
    os.system(intake_cmd)

    # 2. Rapport
    print("📄 Steg 2: Skapar rapport från intake...")
    report_cmd = f'python3 sentinelstack_auto_profile.py --type {article} --client {json_filename}'
    os.system(report_cmd)

    # 3. Faktura
    print("🧾 Steg 3: Skapar faktura...")
    invoice_cmd = f'python3 sentinelstack_invoice_profile.py --client {json_filename} --article {article}'
    os.system(invoice_cmd)

    # 4. Bundle
    print("📦 Steg 4: Skapar leveranspaket...")
    bundle_cmd = f'python3 sentinelstack_bundle.py --client {json_filename} --article {article}'
    os.system(bundle_cmd)

def main():
    parser = argparse.ArgumentParser(description="Full auto-pipeline: intake → rapport → faktura → zip")
    parser.add_argument("--name", required=True, help="Företagsnamn")
    parser.add_argument("--contact", required=True, help="Kontaktperson")
    parser.add_argument("--email", required=True, help="E-postadress")
    parser.add_argument("--ai", required=True, help="Hur används AI?")
    parser.add_argument("--usage", required=True, help="Typ av verksamhet")
    parser.add_argument("--article", required=True, help="Vilken AI Act-artikel (t.ex. artikel13)")
    args = parser.parse_args()

    run_pipeline(args.name, args.contact, args.email, args.ai, args.usage, args.article)

if __name__ == "__main__":
    main()
