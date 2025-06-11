#!/usr/bin/env python3
# sentinelstack_gpt_api_keyarg.py – GPT-4 CLI with optional --api-key support

import argparse
import os
import openai
from dotenv import load_dotenv

# Load from .env first
load_dotenv(dotenv_path=os.path.expanduser("~/.sentinelstack.env"))

def ask_gpt(question, api_key):
    openai.api_key = api_key or os.getenv("OPENAI_API_KEY")
    if not openai.api_key:
        return "❌ Ingen API-nyckel angiven – använd --api-key eller skapa ~/.sentinelstack.env"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Du är en AI-expert som hjälper företag att följa EU:s AI-förordning."},
                {"role": "user", "content": question}
            ],
            max_tokens=800,
            temperature=0.3
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"❌ Fel vid GPT-anrop: {e}"

def run_assist(args):
    print("🧠 GPT-4 Assist för:", args.name)
    print("Fråga:", args.question)
    response = ask_gpt(args.question, args.api_key)
    print("\n📄 Svar från GPT-4:")
    print(response)

def main():
    parser = argparse.ArgumentParser(prog="sentinelstack", description="AI Compliance CLI + GPT-4 Assist")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_assist = subparsers.add_parser("assist", help="GPT-4-hjälp för compliancefrågor")
    p_assist.add_argument("--name", required=True, help="Klientnamn")
    p_assist.add_argument("--question", required=True, help="Fråga till GPT-4")
    p_assist.add_argument("--api-key", required=False, help="API-nyckel om ingen .env används")
    p_assist.set_defaults(func=run_assist)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
