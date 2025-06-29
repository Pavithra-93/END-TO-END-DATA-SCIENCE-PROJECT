from flask import Flask, request, jsonify
import joblib
import numpy as np

# Load trained model and scaler
model = joblib.load("model/iris_model.joblib")
scaler = joblib.load("model/scaler.joblib")


# Create Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Iris Model API is running."

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json(force=True)
    features = np.array(data["features"]).reshape(1, -1)
    scaled_features = scaler.transform(features)
    prediction = model.predict(scaled_features)[0]

    # Map numeric label to species name
    label_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
    species = label_map.get(prediction, "unknown")

    return jsonify({"predicted_class": species})

if __name__ == "__main__":
    app.run(debug=True)
