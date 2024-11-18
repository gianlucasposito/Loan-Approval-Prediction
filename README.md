# Loan Approval Prediction

## Overview

This project develops a machine learning model to predict loan approval based on applicant details. 
The loan prediction problem involves determining the likelihood that a loan application will be approved or rejected, given various features such as income, loan amount, and credit history. 
The goal is to enhance decision-making for loan applications by utilizing historical data. Additionally, the project emphasizes explainable AI to ensure transparency and build trust in predictions. 
Furthermore, a user-friendly app is deployed using the Streamlit library, which can be accessed here: [Streamlit App](#).

## Dataset and Variables

The project uses data from the Loan Prediction Kaggle competition.

### Key Variables
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


## Key Data Analysis Features

- **Data Preprocessing:** Handling missing values, outliers, and skewed distributions with transformations.
- **Feature Engineering:** Creation of new features like log-transformed income and balance variables to improve model performance.
- **Model Training and Comparison:**
  - Evaluated models: KNN, SVM, Random Forest, and XGBoost.
  - Random Forest was selected for its performance (highest F1-score) and interpretability.
- **Bias Reduction:** Removed demographic features (e.g., gender, marital status) to ensure fairness and focus on financial predictors.
- **Model Explanation:** Used SHAP values to provide interpretable insights into individual predictions.


## Workflow

1. **Data Cleaning:** Missing values filled; outliers addressed.
2. **Feature Engineering:** Log transformations applied to reduce skewness.
3. **Model Selection:** Hyperparameter tuning with GridSearchCV.
4. **Model Explanation:** SHAP library used for feature importance and prediction explainability.
5. **Bias Mitigation:** Removal of features prone to introducing bias.



---



## Key Findings

### Data Insights
- **Key Predictors:** Credit history, total income, balance income, and EMI were identified as the most impactful features for loan approval.
- **Ethical Considerations:** Steps were taken to reduce bias by excluding demographic features with low predictive power and potential for discrimination.



---


---

## Ethical and Practical Steps

- **Demographic Bias Mitigation:** Excluded features like gender and marital status to ensure fairness.
- **Explainability:** SHAP values used to clearly outline model decisions for transparency.

---



## Model Deployment and Usage

1. **Saving the Model:** The trained SVM classifier is saved using the pickle library. The model is serialized and saved to a file (e.g., `loan_status_model.pkl`) to be used for future predictions without the need for retraining.
2. **Streamlit App:** A web application is developed using Streamlit to create an interactive interface for users to input loan application details. 
   - Input fields include features such as gender, marital status, income, loan amount, etc.
   - After entering the details and clicking the "Predict Loan Status" button, the trained SVM model is loaded, and the loan status is predicted based on the provided information.

---


## Contributions

Contributions are welcome! Please open an issue or submit a pull request for enhancements or bug fixes.







