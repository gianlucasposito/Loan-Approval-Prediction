# Loan Approval Prediction

## Overview

This project predicts loan approval using machine learning models trained on a dataset of applicant details. It aims to:
- Enhance decision-making in loan processing.
- Promote transparency through explainable AI techniques like SHAP.
- Provide a **Streamlit** web app for real-time, user-friendly predictions.

👉 [**Access the Application**](#)

## Dataset and Variables

The project uses the Loan Prediction Dataset from Kaggle, containing features across demographic, socioeconomic, and financial categories:

| **Feature Type** | **Features**                                         | **Description**                         |
|------------------|-----------------------------------------------------|-----------------------------------------|
| Demographic      | `Gender`, `Married`, `Dependents`                   | Applicant details.                      |
| Socioeconomic    | `Education`, `Self_Employed`, `ApplicantIncome`     | Income and education info.              |
| Loan Details     | `LoanAmount`, `Loan_Amount_Term`, `Credit_History`  | Loan and credit details.                |
| Target Variable  | `Loan_Status`                                       | Approved (`Y`) or Rejected (`N`).       |

---

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

