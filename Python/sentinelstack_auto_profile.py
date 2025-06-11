#!/usr/bin/env python3
# sentinelstack_auto_profile.py – Använder intake.json + prompttyp → GPT + PDF

import argparse
import os
import json
import openai
from dotenv import load_dotenv
from datetime import datetime
from fpdf import FPDF

# Promptbibliotek
PROMPTS = {
    "artikel9": "Vad behöver ett företag dokumentera enligt AI Act Artikel 9 om riskhantering?",
    "artikel10": "Hur ska ett företag beskriva datastyrning enligt AI Act Artikel 10?",
    "artikel11": "Vad ska ingå i den tekniska dokumentationen enligt AI Act Artikel 11?",
    "artikel12": "Vilken typ av loggning krävs enligt AI Act Artikel 12?",
    "artikel13": "Vilken information måste ges till användare enligt AI Act Artikel 13?",
    "artikel14": "Hur uppfyller man kravet på mänsklig kontroll enligt Artikel 14?",
    "artikel15": "Vilka robusthets- och cybersäkerhetsåtgärder krävs enligt AI Act Artikel 15?"
}

load_dotenv(dotenv_path=os.path.expanduser("~/.sentinelstack.env"))
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_pdf(client_data, prompt, answer, tag):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"AI Act Compliance Rapport – {client_data['client']}", ln=True, align='C')
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Kontakt: {client_data['contact']} | {client_data['email']}")
    pdf.multi_cell(0, 10, f"AI-användning: {client_data['ai_usage']}")
    pdf.multi_cell(0, 10, f"Verksamhetstyp: {client_data['business_type']}")
    pdf.ln(5)
    pdf.multi_cell(0, 10, f"Fråga ({tag}):\n{prompt}")
    pdf.multi_cell(0, 10, f"\nSvar:\n{answer}")
    filename = f"{client_data['client'].replace(' ', '_')}_AIAct_{tag}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf"
    pdf.output(filename)
    return filename

def run_auto(args):
    with open(args.client, "r") as f:
        client_data = json.load(f)

    tag = args.type.lower()
    if tag not in PROMPTS:
        print("❌ Ogiltig prompttyp. Tillgängliga är:", ", ".join(PROMPTS.keys()))
        return

    prompt = PROMPTS[tag]
    print(f"📚 Prompt ({tag}) skickas till GPT...")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Du är en AI-expert som hjälper företag att följa EU:s AI-förordning."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.3
        )
        answer = response.choices[0].message["content"].strip()
        print("\n📄 GPT-4 svar:\n")
        print(answer)

        pdf_file = generate_pdf(client_data, prompt, answer, tag)
        print(f"📄 Rapport sparad som: {pdf_file}")
    except Exception as e:
        print(f"❌ GPT-fel: {e}")

def main():
    parser = argparse.ArgumentParser(prog="sentinelstack auto-profile", description="Auto GPT + PDF från intake.json")
    parser.add_argument("--type", required=True, help="Prompttyp (artikel9–artikel15)")
    parser.add_argument("--client", required=True, help="JSON-fil med kunddata")
    args = parser.parse_args()
    run_auto(args)

if __name__ == "__main__":
    main()
