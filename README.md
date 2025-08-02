Welcome to the Nairobi Ride-Hailing Demand Predictor! 

This project helps figure out where and when ride-hailing drivers are needed most in Nairobi, Kenya, using data and smart predictions. It was built as a school project to make transportation planning easier and more efficient.

What This Project Does

This tool predicts how many rides will be requested in different areas of Nairobi (like Karen or Embakasi) based on factors like:Time of day (e.g., rush hours)
Day of the week (e.g., weekends)
Weather conditions (e.g., rainy days)
Other details like ride duration and wait times

We used real data to create charts and a model that guesses demand, helping drivers know where to go!

How to Use It
You can try the predictor live online:
Visit the Streamlit App (https://nairobi-ride-demand-3xg3xzzcpngq65jbpanmtv.streamlit.app/).

Pick a location (e.g., Karen), time (e.g., 5 PM), day, and weather (e.g., Heavy Rain).

Click “Predict Demand” to see how many rides are expected.
Explore charts showing demand patterns (e.g., high demand in Karen during rain).

Key Findings

Rush Hours Matter: Demand peaks between 7–9 AM and 5–7 PM, especially in busy areas like Karen.

Weather Impact: Rainy days (especially heavy rain) increase ride requests.

Weekend Boost: Saturdays and Sundays see more rides than weekdays.

Top Zone: Karen has the highest demand, needing more drivers during peak times.

Check the charts (e.g., demand_heatmap.png) in this repository for visuals!

Files in This Repositoryapp.py: 

The online tool (Streamlit app) to predict demand.
preprocessed_rides.csv: The main data about past rides.
demand.csv: Processed data used for predictions.
model.pkl: The smart model that makes predictions.
requirements.txt: List of tools needed to run the project.
PNG files (e.g., demand_by_hour.png): Charts showing demand trends.

