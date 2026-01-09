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
 
Step 1: Open Project Folder
Open Command Prompt / Terminal and go to the project directory.
cd student_depression_project

Step 2: Install Required Packages
Install Flask and other required libraries.
pip install flask numpy scikit-learn xgboost

Step 3: Run the Flask Application
Start the API server by running:
python app.py


If successful, you will see:
Running on http://127.0.0.1:5000
This means the Flask server is running.

Step 4: Open Postman
Open Postman application.

Step 5: Create a New Request in Postman
Select POST method
Enter URL:
http://127.0.0.1:5000/predict

Step 6: Add Request Body
Go to Body → raw → JSON
Paste input data:

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

Step 7: Send Request
Click Send.

Step 8: View Prediction
Postman will return the prediction result in JSON format:

{
  "prediction": 1,
  "result": "Likely Depressed"
}

Step 9: Stop the Server
Press CTRL + C in the terminal to stop Flask.

0 → Not Likely Depressed

1 → Likely Depressed

##Technologies Used
Python 
XGBoost
Scikit-learn
Flask
Jupyter Notebook                                                                                                                                                                               
