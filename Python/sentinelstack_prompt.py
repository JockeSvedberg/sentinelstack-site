#!/usr/bin/env python3
# sentinelstack_prompt.py – Promptmallar för AI Compliance

import argparse
from datetime import datetime

PROMPTS = {
    "artikel9": "Vad behöver ett företag dokumentera enligt AI Act Artikel 9 om riskhantering?",
    "artikel10": "Hur ska ett företag beskriva datastyrning enligt AI Act Artikel 10?",
    "artikel11": "Vad ska ingå i den tekniska dokumentationen enligt AI Act Artikel 11?",
    "artikel12": "Vilken typ av loggning krävs enligt AI Act Artikel 12?",
    "artikel13": "Vilken information måste ges till användare enligt AI Act Artikel 13?",
    "artikel14": "Hur uppfyller man kravet på mänsklig kontroll enligt Artikel 14?",
    "artikel15": "Vilka robusthets- och cybersäkerhetsåtgärder krävs enligt AI Act Artikel 15?"
}

def run_prompt(args):
    prompt_key = args.type.lower()
    if prompt_key in PROMPTS:
        print(f"📚 Prompt för {prompt_key.capitalize()} ({args.client}):\n")
        print(PROMPTS[prompt_key])
        filename = f"{args.client}_prompt_{prompt_key}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
        with open(filename, "w") as f:
            f.write(PROMPTS[prompt_key])
        print(f"✔️ Prompt sparad som: {filename}")
    else:
        print("❌ Ogiltig prompttyp. Använd --list för att visa tillgängliga.")

def list_prompts(args):
    print("📂 Tillgängliga prompttyper:")
    for key in PROMPTS:
        print(f"- {key}")

def main():
    parser = argparse.ArgumentParser(prog="sentinelstack prompt", description="Promptgenerator för AI Compliance")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_gen = subparsers.add_parser("generate", help="Generera en promptmall")
    p_gen.add_argument("--type", required=True, help="Vilken artikel/frågetyp (t.ex. artikel13)")
    p_gen.add_argument("--client", required=True, help="Klientnamn")
    p_gen.set_defaults(func=run_prompt)

    p_list = subparsers.add_parser("list", help="Lista tillgängliga prompts")
    p_list.set_defaults(func=list_prompts)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
