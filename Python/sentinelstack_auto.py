#!/usr/bin/env python3
# sentinelstack_auto.py – Kombinerar prompt + GPT + export i ett steg

import argparse
import os
import openai
from dotenv import load_dotenv
from datetime import datetime

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

# Ladda API-nyckel
load_dotenv(dotenv_path=os.path.expanduser("~/.sentinelstack.env"))
openai.api_key = os.getenv("OPENAI_API_KEY")

def run_auto(args):
    prompt_key = args.type.lower()
    if prompt_key not in PROMPTS:
        print("❌ Ogiltig prompttyp. Tillgängliga är:", ", ".join(PROMPTS.keys()))
        return

    prompt = PROMPTS[prompt_key]
    print(f"📚 Prompt ({args.type}):\n{prompt}\n")

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

        timestamp = datetime.now().strftime("%Y%m%d_%H%M")
        filename = f"{args.client}_AIAct_{prompt_key}_{timestamp}.txt"
        with open(filename, "w") as f:
            f.write("Fråga:\n" + prompt + "\n\nSvar:\n" + answer)
        print(f"✔️ Svar sparat i: {filename}")
    except Exception as e:
        print(f"❌ GPT-fel: {e}")

def main():
    parser = argparse.ArgumentParser(prog="sentinelstack auto", description="Auto-prompt till GPT och export")
    parser.add_argument("--type", required=True, help="Prompttyp (artikel9–artikel15)")
    parser.add_argument("--client", required=True, help="Klientnamn")
    args = parser.parse_args()
    run_auto(args)

if __name__ == "__main__":
    main()
