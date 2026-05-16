// Base URL for the Flask Backend
const API_URL = 'http://127.0.0.1:5000/api/predict';

async function analyzeText() {
    const inputElement = document.getElementById('news-input');
    const button = document.getElementById('analyze-btn');
    const btnText = document.getElementById('btn-text');
    const loader = document.getElementById('loader');
    const resultSection = document.getElementById('result-section');
    const errorMsg = document.getElementById('error-message');
    
    const text = inputElement.value.trim();

    // Basic Validation
    if (!text) {
        alert("Please paste some article text before analyzing.");
        return;
    }
    
    if (text.split(' ').length < 15) {
        alert("This text is very short. The AI works best with at least 50 words to analyze context.");
        // We let them proceed anyway, but give a warning
    }

    // Set UI to Loading State
    button.disabled = true;
    btnText.innerText = "Analyzing...";
    loader.style.display = "block";
    errorMsg.style.display = "none";
    resultSection.classList.add("hidden");

    try {
        // Send data to Flask backend
        const response = await fetch(API_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ text: text })
        });

        if (!response.ok) {
            throw new Error(`Server error: ${response.status}`);
        }

        const data = await response.json();

        // Pass the data to our display function
        displayResults(data);

    } catch (error) {
        console.error("Error connecting to API:", error);
        errorMsg.innerText = "⚠️ Error connecting to the backend. Please ensure your Python Flask server is running.";
        errorMsg.style.display = "block";
    } finally {
        // Restore button state
        button.disabled = false;
        btnText.innerText = "Analyze Article";
        loader.style.display = "none";
    }
}

function displayResults(data) {
    const resultSection = document.getElementById('result-section');
    const badge = document.getElementById('prediction-badge');
    const realBar = document.getElementById('real-bar');
    const fakeBar = document.getElementById('fake-bar');
    
    // Calculate percentages
    const realPct = (data.confidence.real_probability * 100).toFixed(1);
    const fakePct = (data.confidence.fake_probability * 100).toFixed(1);

    // Update the visual badge
    badge.innerText = `Prediction: ${data.prediction}`;
    if (data.prediction === "FAKE") {
        badge.style.backgroundColor = "var(--fake-color)";
    } else {
        badge.style.backgroundColor = "var(--real-color)";
    }

    // Reset bars to 0 first (for the animation effect)
    realBar.style.width = '0%';
    fakeBar.style.width = '0%';

    // Remove the hidden class so the section fades in
    resultSection.classList.remove("hidden");

    // Small delay before setting the width triggers the CSS transition animation
    setTimeout(() => {
        document.getElementById('real-percent').innerText = `${realPct}%`;
        realBar.style.width = `${realPct}%`;

        document.getElementById('fake-percent').innerText = `${fakePct}%`;
        fakeBar.style.width = `${fakePct}%`;
    }, 100);
}