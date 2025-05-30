document.getElementById('signup-form').addEventListener('submit', async function(e) {
  e.preventDefault();
  const email = this.email.value;
  const password = this.password.value;

  const res = await fetch('/auth/signup', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password })
  });

  const data = await res.json();
  document.getElementById('response').textContent = data.message || data.error;
});
