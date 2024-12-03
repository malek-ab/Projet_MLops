# Project Overview
This project is a resale price prediction tool for apartments, developed as a Streamlit application. It allows users to input specific characteristics of an apartment, such as its location, type, floor area, and lease details, and provides a predicted resale price based on a trained machine learning model.

## Key Features
User-Friendly Interface: A simple and intuitive web interface built with Streamlit.
Accurate Predictions: Powered by a pre-trained XGBoost regression model for reliable predictions.
Interactive Inputs: Users can specify various details like apartment type, location, floor area, and lease duration for real-time predictions.
Customizable Backend: The app supports dynamic updates and improvements based on additional data or model upgrades.
## Technologies Used
Machine Learning: XGBoost regression model for predictions.
Streamlit: For creating the web application interface.
Python Libraries:
pandas for data manipulation.
joblib for loading the trained model.
numpy for numerical operations.
Application Flow
Input Features: Users enter apartment details, such as:
Location (town and street/block).
Apartment type (e.g., 2-room, 3-room).
Floor area in square meters.
Lease information (e.g., commencement year, remaining lease duration).
Data Preprocessing: The app preprocesses the inputs to match the format expected by the trained model.
Prediction: The model generates a resale price prediction in real-time.
Output: The predicted price is displayed on the app interface.
## Purpose
This project was created to:

Showcase the practical application of machine learning in real estate pricing.
Provide an accessible solution for predicting resale prices, which can be useful for property owners, buyers, and analysts.
