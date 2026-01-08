from flask import Flask, request, jsonify
import pickle
import numpy as np
import xgboost

app = Flask(__name__)

# Load files 
model = pickle.load(open('gscv_xgb.pkl', 'rb'))
scaler = pickle.load(open('scaler.pkl', 'rb'))

l1 = pickle.load(open('l1.pkl', 'rb'))
l2 = pickle.load(open('l2.pkl', 'rb'))
l3 = pickle.load(open('l3.pkl', 'rb'))
l4 = pickle.load(open('l4.pkl', 'rb'))
l5 = pickle.load(open('l5.pkl', 'rb'))
l6 = pickle.load(open('l6.pkl', 'rb'))
l7 = pickle.load(open('l7.pkl', 'rb'))
l8 = pickle.load(open('l8.pkl', 'rb'))
l9 = pickle.load(open('l9.pkl', 'rb'))

#  Safe encoder
def safe_transform(encoder, value):
    if value in encoder.classes_:
        return encoder.transform([value])[0]
    else:
        return -1

#  Home route 
@app.route('/')
def home():
    return "Student Depression Prediction API is running"

#  Predict route 
@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        encoded_input = [
            safe_transform(l1, data['gender']),
            float(data['age']),
            safe_transform(l2, data['city']),
            safe_transform(l3, data['profession']),
            float(data['academic_pressure']),
            float(data['work_pressure']),
            float(data['cgpa']),
            float(data['study_satisfaction']),
            float(data['job_satisfaction']),
            safe_transform(l4, data['sleep_duration']),
            safe_transform(l5, data['dietary_habits']),
            safe_transform(l6, data['degree']),
            safe_transform(l7, data['suicidal_thoughts']),
            float(data['work_study_hours']),
            safe_transform(l8, data['financial_stress']),
            safe_transform(l9, data['family_history'])
        ]

        scaled_input = scaler.transform([encoded_input])

        prediction = int(model.predict(scaled_input)[0])

        if prediction == 1:
            result = "Likely Depressed"
        else:
            result = "Not Likely Depressed"

        return jsonify({
            "prediction": prediction,
            "result": result
        })

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500

#  Run app 
if __name__ == '__main__':
    app.run(debug=True)
