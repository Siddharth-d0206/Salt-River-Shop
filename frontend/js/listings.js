export async function getListings() {
  const res = await fetch('/listings');
  return res.json();
}
