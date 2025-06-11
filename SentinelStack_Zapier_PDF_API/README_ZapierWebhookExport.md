# SentinelStack – Google Docs PDF Export via Webhook (Pro API)

Detta flöde låter dig exportera ett Google Docs-dokument till PDF via ett avancerat Webhook-steg i Zapier.

## 🔗 Steg i Zapier:

1. Trigger: Stripe → Checkout Session Completed
2. Formatter: Format "Created" till YYYY-MM-DD
3. Google Docs: Create Document from Template (med kvittodata)
4. Webhook by Zapier:
   - Action Event: Custom Request
   - Method: GET
   - URL:
     https://docs.google.com/document/d/{{DOC_ID}}/export?format=pdf
   - Headers:
     Authorization: Bearer {{OAuth Access Token}}

## 📌 Viktigt:
- Du måste hämta access_token via OAuth2 om du kör den själv
- Alternativ: skapa Google Apps Script som proxy för export

## 💼 Tips:
- Spara PDF:n i Drive via Zapier Drive Upload
- Eller mejla PDF som bilaga med Gmail

