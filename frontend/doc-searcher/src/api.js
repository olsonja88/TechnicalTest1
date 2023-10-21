
export async function fetchDocument() {
    try {
        const response = await fetch("http://localhost:8000/");
        if (!response.ok) {
            throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error("API request error:", error);
        throw error;
    }
}

export default fetchDocument;
