import streamlit as st
import joblib
import pandas as pd

model = joblib.load("student_performance_model.pkl")

st.title("Student Performance Prediction System")

attendance = st.slider(
    "Attendance (%)",
    0,
    100,
    75
)

test1 = st.slider(
    "Internal Test 1",
    0,
    40,
    20
)

test2 = st.slider(
    "Internal Test 2",
    0,
    40,
    20
)

assignment = st.slider(
    "Assignment Score",
    0,
    10,
    5
)

study_hours = st.slider(
    "Daily Study Hours",
    0,
    12,
    3
)

if st.button("Predict Final Marks"):

    avg_internal = (
        test1 + test2
    ) / 2

    overall_score = (
        attendance +
        assignment*10 +
        study_hours*5
    )

    data = pd.DataFrame({
        "Attendance (%)":[attendance],
        "Internal Test 1 (out of 40)":[test1],
        "Internal Test 2 (out of 40)":[test2],
        "Assignment Score (out of 10)":[assignment],
        "Daily Study Hours":[study_hours],
        "Average_Internal_Marks":[avg_internal],
        "Overall_Academic_Score":[overall_score]
    })

    prediction = model.predict(data)

    st.success(
        f"Predicted Final Marks : {prediction[0]:.2f}"
    )