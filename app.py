import streamlit as st
import pandas as pd
import joblib

# Load Best Model
model = joblib.load("placement_model.pkl")

# Website Title
st.title("Student Placement Prediction System")
st.write("Predict whether a student will get placed or not.")
st.divider()

# Student Details
st.subheader("Enter Student Details")

cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, value=7.0)
internships = st.number_input("Number of Internships", min_value=0, max_value=10, value=1)
projects = st.number_input("Number of Projects", min_value=0, max_value=20, value=2)
workshops = st.number_input("Number of Workshops", min_value=0, max_value=20, value=2)
aptitude = st.number_input("Aptitude Score", min_value=0.0, max_value=100.0, value=70.0)
communication = st.number_input("Communication Score", min_value=0.0, max_value=100.0, value=70.0)
branch = st.selectbox("Department", ["CSE", "ECE", "EEE", "IT", "MECH", "CIVIL"])

# Prediction Button
if st.button("Predict Placement"):

    input_data = pd.DataFrame([{
        "CGPA": cgpa,
        "Internships": internships,
        "Projects": projects,
        "Workshops": workshops,
        "AptitudeScore": aptitude,
        "CommunicationScore": communication,
        "Branch": branch
    }])

    # Prediction - I
    prediction = model.predict(input_data)[0]

    st.divider()
    st.subheader("Prediction Result")

    if prediction == "Placed":
        st.success("Congratulations! Student is Likely to be Placed.")
        st.balloons()
    else:
        st.error("Student is Likely to be Not Placed.")
