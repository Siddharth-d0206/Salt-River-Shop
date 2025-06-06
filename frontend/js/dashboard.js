const listingForm = document.getElementById('listing-form');
const listingsDiv = document.getElementById('listings');

async function fetchListings() {
  const res = await fetch('/listings');
  const data = await res.json();
  listingsDiv.innerHTML = '';
  if (!data) return;
  Object.values(data).forEach(item => {
    const div = document.createElement('div');
    div.innerHTML = `<h3>${item.title}</h3><p>${item.description}</p>` +
      `<img src="${item.image_url}" alt="${item.title}" width="200" />`;
    listingsDiv.appendChild(div);
  });
}

if (listingForm) {
  listingForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(listingForm);
    const res = await fetch('/listings', {
      method: 'POST',
      body: formData
    });
    await res.json();
    listingForm.reset();
    fetchListings();
  });
}

fetchListings();
