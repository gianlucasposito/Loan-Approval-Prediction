# Loan Approval Prediction

## Overview

This project develops a machine learning model to predict loan approval based on applicant details. 
The loan prediction problem involves determining the likelihood that a loan application will be approved or rejected, given various features such as income, loan amount, and credit history. 
The goal is to enhance decision-making for loan applications by using historical data. Additionally, the project emphasizes explainable AI to ensure transparency and build trust in predictions. 
Furthermore, a user-friendly app is deployed using the Streamlit library, which can be accessed here: [Streamlit App](#).

## Dataset and Variables

The project uses data from the Loan Prediction Kaggle competition. The dataset includes various key variables that contribute to predicting loan approval:

- **Loan_ID:** Unique identifier for each loan application.
- **Demographic Details:**
  - `Gender`, `Married`, `Dependents`
- **Socioeconomic Factors:**
  - `Education`, `Self_Employed`, `ApplicantIncome`, `CoapplicantIncome`
- **Loan Details:**
  - `LoanAmount`, `Loan_Amount_Term`, `Credit_History`
- **Geographic Information:**
  - `Property_Area`
- **Target Variable:**
  - `Loan_Status` (Binary: Approved `Y` or Rejected `N`)

## Data Analysis Workflow

- **Data Preprocessing:** Handling missing values, outliers, and skewed distributions with transformations.
- **Feature Engineering:** Creation of new features like log-transformed income and balance variables to improve model performance.
- **Data Visualization:** Visual exploration of key variables and relationships to understand data distributions and correlations.
- **Model Training and Comparison:**
  - Evaluated models: KNN, SVM, Random Forest, and XGBoost.
  - Random Forest was selected for its performance (highest F1-score) and interpretability.
  - Feature Importance Analysis
- **Bias Reduction:** Removed demographic features (e.g., gender, marital status) to ensure fairness and focus on financial predictors.
- **Model Explanation:** Used SHAP values to provide interpretable insights into individual predictions and clearly outline model decisions for transparency

## Data Insights

- **Key Predictors:** Credit history, total income, balance income, and EMI were identified as the most impactful features for loan approval.
- **Ethical Considerations:** Exclude demographic features with low predictive power and potential for discrimination.

## Model Deployment and Usage

1. **Saving the Model:** The trained Random Forest classifier is saved using the pickle library.
2. **Streamlit App:** A web application is developed using **Streamlit** to create an interactive interface for users to input loan application details.

👉 [Go to the App](#)

---

## Contributions

Contributions are welcome! Please open an issue or submit a pull request for enhancements or bug fixes.

