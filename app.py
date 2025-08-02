import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import seaborn as sns

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load data for zone encoding
df = pd.read_csv('preprocessed_rides.csv')

# Prediction function
def predict_demand(zone, hour, day_of_week, is_weekend, weather, surge=1.0, ride_duration=20.0, wait_duration=10.0):
    zone_code = df[df['pickup_zone'] == zone]['pickup_zone'].astype('category').cat.codes.iloc[0] if zone in df['pickup_zone'].values else 0
    input_data = pd.DataFrame({
        'pickup_zone': [zone_code],
        'hour_of_day': [hour],
        'day_of_week': [day_of_week],
        'is_weekend': [is_weekend],
        'weather': [weather],
        'surge_multiplier': [surge],
        'ride_duration(min)': [ride_duration],
        'ride_wait_duration(min)': [wait_duration]
    })
    pred = model.predict(input_data)[0]
    return round(pred, 2)

st.title('Nairobi Ride Demand Predictor')

# Input fields
zone = st.selectbox('Pickup Zone', df['pickup_zone'].unique())
hour = st.slider('Hour of Day', 0, 23, 17)
day_of_week = st.selectbox('Day of Week', range(7), format_func=lambda x: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'][x])
is_weekend = 1 if day_of_week in [5, 6] else 0
weather = st.selectbox('Weather', [0, 1, 2, 3], format_func=lambda x: ['Clear', 'Cloudy', 'Light Rain', 'Heavy Rain'][x])
surge = st.number_input('Surge Multiplier', 1.0, 2.0, 1.0)
ride_duration = st.number_input('Average Ride Duration (min)', 5.0, 60.0, 20.0)
wait_duration = st.number_input('Average Wait Duration (min)', 2.0, 15.0, 10.0)

# Predict
if st.button('Predict Demand'):
    demand_pred = predict_demand(zone, hour, day_of_week, is_weekend, weather, surge, ride_duration, wait_duration)
    st.write(f'Predicted Demand: {demand_pred} rides')
else:
    st.write('Click "Predict Demand" to see the predicted number of rides.')

# Display visualizations
st.header('Understanding Ride Demand')
st.image('demand_by_hour.png', caption='Ride demand peaks during rush hours (7–9 AM, 5–7 PM).')
st.image('demand_by_zone.png', caption='Karen has the highest ride demand, needing more drivers.')
st.image('demand_by_day.png', caption='Weekends see more rides, especially on Saturday.')
st.image('demand_by_weather.png', caption='Heavy rain increases ride demand.')

st.header('Model Insights')
st.image('feature_importance.png', caption='Hour and zone are the biggest factors in predicting demand.')
st.image('actual_vs_predicted.png', caption='Our predictions are close to actual ride counts.')
st.image('demand_heatmap.png', caption='Red areas show high demand (e.g., Karen at 5 PM).')
st.image('sample_predictions.png', caption='Example: More rides in Karen on a rainy evening.')
