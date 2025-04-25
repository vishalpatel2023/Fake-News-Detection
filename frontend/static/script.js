function getPrediction() {
    const text = document.getElementById("newsInput").value;
  
    fetch("http://127.0.0.1:5000/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ text })
    })
    .then(res => res.json())
    .then(data => {
      document.getElementById("result").innerText = data.prediction;
      document.getElementById("card").style.transform = "rotateY(180deg)";
    })
    .catch(err => {
      console.error(err);
      alert("Something went wrong.");
    });
  }

  const card = document.querySelector('.flip-card');
  const safeZones = ['TEXTAREA', 'BUTTON', 'INPUT'];
  
  card.addEventListener('click', (e) => {
    if (!safeZones.includes(e.target.tagName)) {
      card.classList.toggle('flipped');
    }
  });
  

