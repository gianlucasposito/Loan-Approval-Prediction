import streamlit as st
import pandas as pd
import pickle
import shap
import matplotlib.pyplot as plt

# Load the trained ML model
def load_model():
    with open("rf_model.pkl", "rb") as file:
        model = pickle.load(file)
    return model

# App Layout
def main():
   # Set page layout to wide
   st.set_page_config(layout="wide")
   
   # Create a centered layout
   col1, col2, col3 = st.columns([1,3,1])
   with col2:
       st.title('Loan Status Prediction App') 
       st.image("Loan_Prediction_Image.jpg", 
                caption="Make smarter loan decisions with AI",
                use_container_width=True)  # Adjusts image width automatically to the column size
       st.write("""
        Welcome to the Loan Status Prediction App! This tool allows you to predict whether your loan will be **Approved** or **Rejected** based on your provided details.
        
        👉 **How It Works:**
        - Fill in the form on the left.
        - Get a prediction on your loan status.
        - Understand why the prediction was made with an interactive **SHAP Explanation**.
        """)
        
   # Sidebar setup
   st.sidebar.header("User Input Features")    
   
   # Useer input in the sidebar
   def user_input_features():
       ApplicantIncome = st.sidebar.text_input("Applicant Income (in USD)", "0")
       CoapplicantIncome = st.sidebar.text_input("Coapplicant Income (in USD)", "0")
       LoanAmount = st.sidebar.text_input("Loan Amount (in USD thousands)","0")
       Loan_Amount_Term = st.sidebar.slider("Loan Term (in months)", 12, 360, 120)
       Credit_History = st.sidebar.selectbox("Credit History (Good: 1, Bad: 0)", [1, 0])
      
       data = {
            "ApplicantIncome": float(ApplicantIncome),
            "CoapplicantIncome": float(CoapplicantIncome),
            "LoanAmount": float(LoanAmount),
            "Loan_Amount_Term": float(Loan_Amount_Term),
            "Credit_History": Credit_History
           }
       
       return pd.DataFrame(data, index = [0]) # create a pandas DataFrame with one row of data and a specified index
           

   with col2: 
       df =  user_input_features()
       
       st.subheader("User Input Features")
       st.write(df)
   
   

if __name__ == "__main__":
    main()