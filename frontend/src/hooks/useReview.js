const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

export function useReview() {
  async function submitReview(code) {
    const res = await fetch(`${API_URL}/api/review`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, language: 'python' })
    });
    return res.json();
  }
  return { submitReview };
}
