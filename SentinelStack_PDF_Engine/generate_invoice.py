from datetime import datetime
from weasyprint import HTML
import os

def generate_invoice(name, email, product, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    with open("templates/receipt_template.html", "r", encoding="utf-8") as f:
        html = f.read()
    html_filled = html.replace("{{ name }}", name)                      .replace("{{ email }}", email)                      .replace("{{ date }}", date)                      .replace("{{ product }}", product)                      .replace("{{ amount }}", amount)
    output_path = f"invoices/{name.replace(' ', '_')}_{date}.pdf"
    with open("temp.html", "w", encoding="utf-8") as f:
        f.write(html_filled)
    HTML("temp.html").write_pdf(output_path)
    os.remove("temp.html")
    print(f"✅ PDF genererad: {output_path}")

# Exempelanrop:
# generate_invoice("Jack Johansson", "jack@example.com", "Growth", "249")
