import API_BASE_URL from "./config";

export async function analyzeSite(latitude, longitude) {
  const response = await fetch(`${API_BASE_URL}/analysis`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      latitude,
      longitude,
    }),
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(
      `Analysis request failed: ${response.status} ${errorText}`
    );
  }

  return await response.json();
}