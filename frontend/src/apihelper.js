const BASE_URL = '/api';

export async function getIncidents() {
  const r = await fetch(`${BASE_URL}/incidents`);
  if (!r.ok) throw new Error(`GET /incidents failed: ${r.status}`);
  return r.json();
}

export async function createIncident(payload) {
  const r = await fetch(`${BASE_URL}/incidents`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  });
  if (!r.ok) throw new Error(`POST /incidents failed: ${r.status}`);
  return r.json();
}
