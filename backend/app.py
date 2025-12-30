from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import numpy as np

app = Flask(__name__)
CORS(app)   # 🔥 THIS FIXES CORS

model = pickle.load(open("fraud_model.pkl", "rb"))

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)

    result = "Fraud" if prediction[0] == 1 else "Not Fraud"
    return jsonify({"prediction": result})

if __name__ == "__main__":
    app.run(debug=True)
