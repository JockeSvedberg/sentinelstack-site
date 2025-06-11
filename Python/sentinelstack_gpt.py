#!/usr/bin/env python3
# sentinelstack_gpt.py – CLI with GPT simulation (offline mock)

import argparse
import os
from datetime import datetime

def simulate_gpt_response(prompt):
    # Placeholder logic to simulate GPT
    if "risk" in prompt.lower():
        return "Din AI-lösning kan klassas som high-risk enligt Annex III. Dokumentera enligt Artikel 9–15."
    elif "vilka dokument" in prompt.lower():
        return "Du behöver: Riskanalys, Datapolicy, Loggpolicy, Transparensmanual, AI-modellbeskrivning."
    else:
        return "Jag är din GPT-assistent. Skriv en fråga om AI-lagstiftning eller dokumentation."

def run_assist(args):
    print("🧠 GPT-Assistent för:", args.name)
    print("Fråga:", args.question)
    response = simulate_gpt_response(args.question)
    print("\n📄 Svar:")
    print(response)

def main():
    parser = argparse.ArgumentParser(prog="sentinelstack", description="AI Compliance CLI + GPT Assist")
    subparsers = parser.add_subparsers(dest="command", required=True)

    p_assist = subparsers.add_parser("assist", help="GPT-hjälp för compliancefrågor")
    p_assist.add_argument("--name", required=True, help="Klientnamn")
    p_assist.add_argument("--question", required=True, help="Fråga till GPT")
    p_assist.set_defaults(func=run_assist)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
