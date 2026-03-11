# 💊 Medical Insurance Cost Prediction

## 📌 Project Overview

Healthcare costs vary significantly among individuals due to various personal and lifestyle factors. Insurance companies must determine appropriate premium charges for each customer based on their health risk profile.

The goal of this project is to develop a **machine learning-based system that predicts medical insurance costs** using patient information such as age, BMI, smoking status, and other demographic factors.

This project follows a **complete data science workflow**, including **data analysis, model building, model evaluation, and deployment using interactive dashboards**.

---

## 🎯 Objectives

- Analyze healthcare insurance data to understand factors influencing medical charges.
- Perform **Exploratory Data Analysis (EDA)** to uncover patterns and relationships.
- Build and compare multiple **machine learning regression models**.
- Select the best-performing model based on evaluation metrics.
- Develop **interactive dashboards** for both data analysis and real-time prediction.
- Provide **data-driven insights** that can support insurance pricing strategies.

---

## 📊 Dataset Description

The dataset contains the following features:

| Feature | Description |
|--------|-------------|
| Age | Age of the insured person |
| Sex | Gender of the customer |
| BMI | Body Mass Index |
| Children | Number of dependents |
| Smoker | Smoking status |
| Region | Residential region |
| Charges | Medical insurance cost (Target Variable) |

This is a **supervised regression problem**, where the objective is to predict the **continuous target variable (insurance charges)**.

---

## 🔍 Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the structure and relationships within the dataset.

The analysis included:

- **Univariate Analysis** to study individual feature distributions
- **Bivariate Analysis** to understand the relationship between features and insurance charges
- **Multivariate Analysis** to examine combined effects of multiple variables
- **Correlation Analysis** to identify relationships among numerical variables

### Key Insights

- **Smoking status significantly increases insurance charges**
- **Age shows a positive relationship with medical cost**
- **Higher BMI moderately increases insurance charges**
- **Region has minimal impact on pricing**

These insights help understand how lifestyle and demographic factors influence healthcare expenses.

---

## 🤖 Machine Learning Model Development

To predict insurance charges, several regression models were trained and evaluated.

### Models Used

- Linear Regression
- K-Nearest Neighbors (KNN)
- Decision Tree Regressor
- Random Forest Regressor

### Data Preprocessing

The following preprocessing steps were applied:

- **StandardScaler** for scaling numerical features
- **OneHotEncoder** for encoding categorical variables
- **ColumnTransformer** to handle mixed data types
- **Pipeline** to integrate preprocessing and modeling steps and prevent data leakage

### Model Evaluation

Models were evaluated using **Mean Absolute Error (MAE)**, which measures the average difference between predicted and actual values.

The **best-performing model** was selected and saved using **Joblib** for deployment.

---

## 📈 Analysis Dashboard

An **interactive Streamlit dashboard** was developed to visualize the dataset and explore insights.

### Dashboard Features

- KPI cards showing key metrics such as average charges and smoker percentage
- Dataset overview
- Univariate analysis visualizations
- Bivariate analysis (feature vs charges)
- Multivariate analysis
- Correlation heatmap
- Business insights and recommendations

This dashboard allows users to explore patterns in the healthcare dataset interactively.

---

## 💻 Prediction Dashboard

A second **Streamlit dashboard** was created to provide **real-time insurance cost predictions**.

Users can enter patient details such as:

- Age
- BMI
- Number of children
- Gender
- Smoking status
- Region

The trained machine learning model processes the input and predicts the **estimated insurance cost instantly**.

This makes the project practical and easy to use for real-world scenarios.

---

## 💼 Business Insights

From the analysis and model results, several important insights were discovered:

- Smoking is the **most significant factor** affecting insurance cost.
- Older individuals tend to have higher medical expenses.
- Higher BMI is associated with increased healthcare costs.
- Region has little influence on insurance pricing.

### Recommendations

- Implement **smoker-based premium pricing models**
- Introduce **BMI-based health incentive programs**
- Apply **age-based insurance tiers**
- Promote preventive healthcare awareness

---

## 🛠 Technologies Used

### Programming Language
- Python

### Data Analysis & Visualization
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Machine Learning
- Scikit-learn

### Deployment & Dashboard
- Streamlit

### Model Saving
- Joblib

---

## 🚀 Project Workflow

1. Data Collection  
2. Data Cleaning & Preprocessing  
3. Exploratory Data Analysis  
4. Feature Engineering  
5. Model Training & Evaluation  
6. Best Model Selection  
7. Model Deployment  
8. Dashboard Development  

---

## 📌 Conclusion

This project demonstrates how **data analysis and machine learning can be applied to solve real-world problems in the healthcare insurance domain**.

By combining **data exploration, predictive modeling, and interactive dashboards**, this system provides both **business insights and practical prediction capabilities** for estimating medical insurance costs.
