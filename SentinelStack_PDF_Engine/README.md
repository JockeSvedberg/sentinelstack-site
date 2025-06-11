# SentinelStack PDF Engine (CLI)

Detta paket genererar PDF-kvitton lokalt med hjälp av Python + WeasyPrint.

## Struktur

- `generate_invoice.py` – Huvudskript
- `templates/receipt_template.html` – HTML-template
- `invoices/` – Här sparas färdiga PDF:er

## Användning

Installera WeasyPrint:

pip install weasyprint

Kör:

python generate_invoice.py "Namn" "E-post" "Paket" "Pris"

Exempel:

python generate_invoice.py "Jack Johansson" "jack@example.com" "Growth" "249"
