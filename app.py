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
   st.title('Loan Status Prediction App') 
   
   # Create a centered layout
   col1, col2, col3 = st.columns([1,2,1])
   with col2:
       st.image("Loan_Prediction_Image.jpg", 
                caption="Make smarter loan decisions with AI",
                use_column_width=True)  # Adjusts image width automatically to the column size


if __name__ == "__main__":
    main()