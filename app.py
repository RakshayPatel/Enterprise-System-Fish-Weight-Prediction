from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('fish_weight_model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    features = np.array([data])
    prediction = model.predict(features)
    return render_template('index.html', prediction_text=f'Predicted Fish Weight: {prediction[0]:.2f} grams')

if __name__ == "__main__":
    app.run(debug=True)
