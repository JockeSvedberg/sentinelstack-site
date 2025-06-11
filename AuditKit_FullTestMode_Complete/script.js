
document.addEventListener("DOMContentLoaded", function() {
  const stripe = Stripe('pk_test_1234567890abcdef');
  const elements = stripe.elements();
  const card = elements.create('card');
  card.mount("#card-element");

  const form = document.getElementById('payment-form');
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const { error, paymentMethod } = await stripe.createPaymentMethod({
      type: 'card',
      card: card,
      billing_details: {
        name: form.name.value,
        email: form.email.value
      }
    });

    if (error) {
      document.getElementById("payment-message").textContent = error.message;
    } else {
      const res = await fetch("https://auditkit.vercel.app/api/stripe-webhook", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ paymentMethodId: paymentMethod.id, plan: "starter" })
      });
      const data = await res.json();
      if (data.success) {
        document.getElementById("payment-message").textContent = "Payment simulated successfully!";
      } else {
        document.getElementById("payment-message").textContent = "Error: " + data.error;
      }
    }
  });
});
