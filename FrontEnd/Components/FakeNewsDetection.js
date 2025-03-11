import React,{useState} from "react";
import "../styles/FakeNewsDetection.css";

export default function FakeNewsDetection() {
    const [news,setNews] = useState("");
    const [result,setResult] = useState(null);

    const analyzeNews = () => {
    const isFake = Math.random() > 0.5;
    setResult(isFake ? "Fake News Detected!" : "News Seems Legit!");
    };

    return (
    <div className="news-container">
        <h1>Fake News Detection</h1>
        <textarea
        placeholder="Enter news article..."
        value={news}
        onChange={(e) => setNews(e.target.value)}
        ></textarea>
        <button onClick={analyzeNews}>Analyze</button>
        {result && <p className={result.includes("Fake") ? "fake" : "real"}>{result}</p>}
    </div>
    );
}