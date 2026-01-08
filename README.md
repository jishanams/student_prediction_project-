# student_prediction_project-

**Project Overview

This project is a Machine Learning-based system to predict the likelihood of depression in students. It uses structured student data, including academic, lifestyle, and psychological features, to provide predictions. The goal is to identify students at risk early so that preventive measures or interventions can be taken.

The model is trained using XGBoost, and the application is deployed as a Flask API.

**Features Used

The model uses the following features:

Gender
Age
City
Profession
Academic Pressure
Work Pressure
CGPA
Study Satisfaction
Job Satisfaction
Sleep Duration
Dietary Habits
Degree
Suicidal Thoughts
Work/Study Hours
Financial Stress
Family History

##Why XGBoost?

Handles mixed numerical and categorical data efficiently.
Provides high accuracy and generalization.
Robust against overfitting.
Supports feature importance for interpretability.

##How Features Impact Prediction?

High academic/work pressure, poor sleep, and suicidal thoughts increase depression likelihood.
Higher study satisfaction, better CGPA, and absence of stress reduce the risk.
Family history and financial stress also influence predictions.

##Future Improvements

Handle unseen categorical inputs more effectively.
Add more behavioral and lifestyle features.
Improve data balance for better accuracy.
Use explainable AI methods.
Deploy on cloud for real-world use.

##setup instructions
****Clone the repository:

git clone <your-repo-url>
cd student_depression_project

****Install required packages:

pip install -r requirements.txt


****Run the Flask API:

python app.py


****Test the API using Postman at:

POST http://127.0.0.1:5000/predict


****Use JSON input with the student features.
** JSON Input
{
  "gender": "Male",
  "age": 21,
  "city": "Calicut",
  "profession": "Student",
  "academic_pressure": 3,
  "work_pressure": 2,
  "cgpa": 7.5,
  "study_satisfaction": 3,
  "job_satisfaction": 2,
  "sleep_duration": "6-7 hours",
  "dietary_habits": "Moderate",
  "degree": "Bachelors",
  "suicidal_thoughts": "No",
  "work_study_hours": 7,
  "financial_stress": "No",
  "family_history": "No"
}

Output
{
  "prediction": 1,
  "result": "Likely Depressed"
}


0 → Not Likely Depressed

1 → Likely Depressed

##Technologies Used
Python 
XGBoost
Scikit-learn
Flask
Jupyter Notebook                                                                                                                                                                               
