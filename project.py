import streamlit as st
import pickle
import xgboost 

st.header(" Student Depression Prediction")
st.subheader("Predicting students' likelihood of depression")
st.image("STUDENT DEPRESSION.jpg")
st.text('''Depression in students, particularly adolescents and college students, is a serious issue with significant consequences for their academic, social, and overall well-being. It can manifest in various ways, including persistent sadness, loss of interest in activities, changes in appetite or sleep, and even suicidal thoughts. Early recognition and intervention are crucial for improving long-term outcomes.''')


# Load model and preprocessing objects
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

# Inputs
gender = st.selectbox("Gender:", options=l1.classes_)
age = st.number_input("Age:")
city = st.selectbox("City:", options=l2.classes_)
profession = st.selectbox("Profession:", options=l3.classes_)
academic_pressure = st.number_input("Academic Pressure:")
work_pressure = st.number_input("Work Pressure:")
cgpa = st.number_input("CGPA:")
study_satisfaction = st.number_input("Study Satisfaction:")
job_satisfaction = st.number_input("Job Satisfaction:")
sleep_duration = st.selectbox("Sleep Duration:", options=l4.classes_)
dietary_habits = st.selectbox("Dietary Habits:", options=l5.classes_)
degree = st.selectbox("Degree:", options=l6.classes_)
suicidal_thoughts = st.selectbox("Suicidal Thoughts:", options=l7.classes_)
work_study_hours = st.number_input("Work/Study Hours per day:")
financial_stress = st.selectbox("Financial Stress:", options=l8.classes_)
family_history = st.selectbox("Family History:", options=l9.classes_)

if st.button("Predict"):
    # Encode categorical features
    encoded_input = [
        l1.transform([gender])[0],
        age,
        l2.transform([city])[0],
        l3.transform([profession])[0],
        academic_pressure,
        work_pressure,
        cgpa,
        study_satisfaction,
        job_satisfaction,
        l4.transform([sleep_duration])[0],
        l5.transform([dietary_habits])[0],
        l6.transform([degree])[0],
        l7.transform([suicidal_thoughts])[0],
        work_study_hours,
        l8.transform([financial_stress])[0],
        l9.transform([family_history])[0]
    ]

    # Scale and predict
    scaled = scaler.transform([encoded_input])
    prediction = model.predict(scaled)[0]

    # Show result
    st.subheader("Prediction Result:")
    if prediction == 0:
        st.success("Not Likely Depressed")
    else:
        st.error("Likely Depressed")
