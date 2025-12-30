function predict() {
  const values = document.getElementById("inputData").value
                  .split(",")
                  .map(Number);

  fetch("http://127.0.0.1:5000/predict", {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ features: values })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById("result").innerText =
      "Prediction: " + data.prediction;
  });
}
