function handleAuth(formId, url) {
  const form = document.getElementById(formId);
  if (!form) return;

  form.addEventListener('submit', async function (e) {
    e.preventDefault();
    const email = this.email.value;
    const password = this.password.value;

    const res = await fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();
    document.getElementById('response').textContent = data.message || data.error;

    if (data.idToken && url.includes('login')) {
      // Simple redirect to dashboard after login
      window.location.href = 'dashboard.html';
    }
  });
}

handleAuth('signup-form', '/auth/signup');
handleAuth('login-form', '/auth/login');
