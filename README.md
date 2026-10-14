#  Student Performance Prediction System Using Machine Learning

##  Project Overview

The Student Performance Prediction System is a Machine Learning-based application developed to predict students' final examination marks using academic indicators such as attendance percentage, internal assessment scores, assignment performance, and daily study hours.

The project follows the complete Machine Learning lifecycle including data preprocessing, exploratory data analysis, feature engineering, model training, evaluation, and deployment through a Streamlit web application.

---

##  Objectives

* Predict students' final examination marks.
* Analyze factors affecting academic performance.
* Compare multiple regression algorithms.
* Deploy a user-friendly prediction system.
* Demonstrate the practical application of Machine Learning in education.

---

##  Dataset Information

**Dataset Name:** Student Academic Performance Dataset

**Total Records:** 2000 Students

### Features

| Feature           | Description                       |
| ----------------- | --------------------------------- |
| Student_ID        | Unique Student Identifier         |
| Attendance (%)    | Student Attendance Percentage     |
| Internal Test 1   | Marks Obtained in Internal Test 1 |
| Internal Test 2   | Marks Obtained in Internal Test 2 |
| Assignment Score  | Assignment Performance Score      |
| Daily Study Hours | Average Daily Study Hours         |
| Final Exam Marks  | Target Variable                   |

### Target Variable

**Final Exam Marks (out of 100)**

---

##  Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Joblib
* Streamlit

---

##  Machine Learning Workflow

1. Data Collection
2. Data Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Feature Selection
6. Model Training
7. Model Evaluation
8. Model Deployment

---

##  Data Preprocessing

The following preprocessing steps were performed:

* Missing value analysis
* Duplicate record removal
* Data validation
* Feature creation
* Dataset preparation

### Added Features

#### Average Internal Marks

Average_Internal_Marks = (Internal Test 1 + Internal Test 2) / 2

#### Overall Academic Score

Overall_Academic_Score = Attendance + Assignment Component + Study Hour Component

---

##  Exploratory Data Analysis

EDA was performed using:

* Histograms
* Boxplots
* Scatter Plots
* Correlation Heatmaps

### Key Findings

* Student marks follow an approximately normal distribution.
* Attendance has a strong positive relationship with final marks.
* Internal assessments are highly predictive of final performance.
* Daily study hours positively impact examination results.
* Average Internal Marks showed the highest correlation with final exam marks.

---

##  Machine Learning Models

### 1. Linear Regression

A baseline regression model used for predicting continuous values.

### 2. Random Forest Regressor

An ensemble learning algorithm that combines multiple decision trees to improve prediction accuracy and reduce overfitting.

---

##  Evaluation Metrics

The following regression metrics were used:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---



##  Deployment

The trained model was deployed using Streamlit.

### Application Features

* Interactive user interface
* Real-time prediction
* Easy user input
* Fast and accurate results


##  Future Scope

* Deep Learning-based prediction models
* Mobile application development
* Real-time student monitoring system
* Cloud deployment
* Early warning systems for academically at-risk students

---

##  Internship Information

**Project:** Student Performance Prediction System

**Program:** AIML Summer Internship 2026

**Domain:** Machine Learning / Educational Data Mining

---

##  Conclusion

This project successfully demonstrates the application of Machine Learning techniques for predicting student academic performance. By utilizing attendance records, internal assessment scores, assignment performance, and study habits, the system provides accurate predictions that can assist educators in making data-driven decisions and improving student outcomes.
