import sys
from datetime import datetime
from weasyprint import HTML

def generate_invoice(name, email, product, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    html = open("templates/template.html").read()
    html_filled = html.replace("{{ name }}", name)                      .replace("{{ email }}", email)                      .replace("{{ date }}", date)                      .replace("{{ product }}", product)                      .replace("{{ amount }}", amount)

    with open("temp.html", "w", encoding="utf-8") as f:
        f.write(html_filled)

    HTML("temp.html").write_pdf(f"invoices/{name}_{date}.pdf")
    print("✅ PDF genererad")

# Exempelanrop:
# generate_invoice("Kalle Karlsson", "kalle@exempel.se", "Growth", "249")
