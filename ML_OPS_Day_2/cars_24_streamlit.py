import streamlit as st
import pandas as pd
import numpy as np

st.title("Cars24 Price Prediction App")

encode_dict = {
    'fuel': {'Petrol': 1, 'Diesel': 2, 'CNG': 3, 'LPG': 4},
    'transmission': {'Manual': 1, 'Automatic': 2},
    'seller_type': {'Individual': 1, 'Dealer': 2, 'Trustmark Dealer': 3},
    'owner': {'First Owner': 1, 'Second Owner': 2, 'Third Owner': 3, 'Fourth & Above Owner': 4, 'Test Drive Car': 5}    
}

model = joblib.load('ML_OPS_Day_2/car_price_model.pkl')

import joblib
# model = joblib.load('car_price_model.pkl')

# Eneter the details of the car

year = st.slider("Year of Manufacture", min_value=1990, max_value=2025, value=2015  , step=1 )

km_driven = st.number_input("Kilometers Driven", min_value=0, max_value=1000000, value=50000, step=5000)

col1, col2 = st.columns(2)

fuel = col1.selectbox("Fuel Type", options=['Petrol', 'Diesel', 'CNG', 'LPG'])

seller_type = st.selectbox("Seller Type", options=['Individual', 'Dealer', 'Trustmark Dealer'])

transmission  = st.selectbox("Transmission Type", options=['Manual', 'Automatic'])

owner = st.selectbox("Owner Type", options=['First Owner', 'Second Owner', 'Third Owner', 'Fourth & Above Owner', 'Test Drive Car'])

mileage = st.number_input("Mileage (kmpl)", min_value=0.0, max_value=25.0, value=15.0, step=0.5)

engine = col2.number_input("Engine (cc)", min_value=800, max_value=5000, value=1500, step=100)   

max_power = st.number_input("Max Power (bhp)", min_value=0.0, max_value=300.0, value=150.0, step=5.0) 

seats = st.number_input("Number of Seats", min_value=2, max_value=10, value=5, step=1)  

scaler = joblib.load('ML_OPS_Day_2/scaler.pkl')

def model_predict(year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats):
    # Encode categorical variables
    seller_type_encoded = encode_dict['seller_type'][seller_type]
    fuel_type_encoded = encode_dict['fuel'][fuel]
    transmission_type_encoded = encode_dict['transmission'][transmission]
    owner_type_encoded = encode_dict['owner'][owner]

    # Create a DataFrame for the input data
    input_data = pd.DataFrame({
        'year' : [year],
        'km_driven': [km_driven],
        'fuel': [fuel_type_encoded],
        'seller_type': [seller_type_encoded],
        'transmission': [transmission_type_encoded],
        'owner': [owner_type_encoded],
        'mileage(km/ltr/kg)': [mileage],
        'engine': [engine],
        'max_power': [max_power],
        'seats': [seats]        
    })

    # Scale the input data
    input_data_scaled = scaler.transform(input_data)

    # Make prediction
    predicted_price = model.predict(input_data_scaled)
    
    return round(predicted_price[0],2)

if st.button("Predict Price"):
    predicted_price = model_predict(year, km_driven, fuel, seller_type, transmission, owner, mileage, engine, max_power, seats)
    st.write(f"The predicted price of the car is ₹{predicted_price:,} lakh (approx.)")
else:
    st.write("Click the button to predict the price of the car.")