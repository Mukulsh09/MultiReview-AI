import mockResponse from '../mock/mockResponse.json';

const USE_MOCK = true;

export function useReview() {
  async function submitReview(code) {
    if (USE_MOCK) {
      await new Promise(r => setTimeout(r, 1500));
      return mockResponse;
    }
    const res = await fetch('http://localhost:8000/api/review', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ code, language: 'python' })
    });
    return res.json();
  }
  return { submitReview };
}