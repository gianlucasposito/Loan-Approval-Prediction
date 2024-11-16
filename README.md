# Loan Approval Prediction

# Overview
This project develops a machine learning model to predict loan approval based on applicant details. The goal is to enhance decision-making for loan applications by using historical data.

# Key Features
- **Data Preprocessing:** Handling missing values, outliers, and skewed distributions with transformations.
- **Feature Engineering:** Creation of new features like log-transformed income and balance variables to improve model performance.
- **Model Training and Comparison:**
  - Evaluated models: KNN, SVM, Random Forest, and XGBoost.
  - Random Forest was selected for its performance (highest F1-score) and interpretability.
- **Bias Reduction:** Removed demographic features (e.g., gender, marital status) to ensure fairness and focus on financial predictors.
- **Model Explanation:** Used SHAP values to provide interpretable insights into individual predictions.

# Data Insights
- **Key Predictors:** Credit history, total income, balance income, and EMI were identified as the most impactful features for loan approval.
- **Ethical Considerations:** Steps were taken to reduce bias by excluding demographic features with low predictive power and potential for discrimination.

# Workflow
1. **Data Cleaning:** Missing values filled; outliers addressed.
2. **Feature Engineering:** Log transformations applied to reduce skewness.
3. **Model Selection:** Hyperparameter tuning with GridSearchCV.
4. **Model Explanation:** SHAP library used for feature importance and prediction explainability.
5. **Bias Mitigation:** Removal of features prone to introducing bias.

# Model Performance
- **Evaluation Metric:** F1-score (to handle class imbalance).
- **Top Model:** Random Forest with an F1-score higher than KNN, SVM, and XGBoost.
- **Feature Importance:** Credit history was the most influential feature, followed by income-related attributes.

# Ethical and Practical Steps
- **Demographic Bias Mitigation:** Excluded features like gender and marital status to ensure fairness.
- **Explainability:** SHAP values used to clearly outline model decisions for transparency.

# Future Work
- Deploy the model for real-world application.
- Periodically audit for bias and fairness.
- Integrate real-time explainability tools to aid users.



Saving the Model: The trained SVM classifier is saved using the pickle library. The model is serialized and saved to a file (e.g., loan_status_model.pkl) to be used for future predictions without the need for retraining.

Streamlit App: A web application is developed using Streamlit to create an interactive interface for users to input loan application details. The input fields include features such as gender, marital status, income, loan amount, etc. After entering the details and clicking the "Predict Loan Status" button, the trained SVM model is loaded, and the loan status is predicted based on the provided information.










