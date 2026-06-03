import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("gb_booking_model.pkl")

# Title
st.title("Hotel Booking Cancellation Predictor")

st.divider()

st.write("Enter booking details to predict cancellation.")

# Inputs
lead_time = st.slider("Lead Time", 0, 500, 50)

avg_price = st.number_input(
    "Average Price Per Room",
    min_value=0.0,
    max_value=500.0,
    value=100.0
)

special_requests = st.slider(
    "Number of Special Requests",
    0,
    5,
    1
)

total_guests = st.slider(
    "Total Guests",
    1,
    10,
    2
)

total_nights = st.slider(
    "Total Nights",
    1,
    20,
    3
)

repeated_guest = st.selectbox(
    "Repeated Guest",
    [0, 1]
)

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame([{
        "lead_time": lead_time,
        "avg_price_per_room": avg_price,
        "no_of_special_requests": special_requests,
        "total_guests": total_guests,
        "total_nights": total_nights,
        "repeated_guest": repeated_guest
    }])

    prediction = model.predict(input_data)[0]

    prob = model.predict_proba(input_data)[0][1]

    if prediction == 1:
        st.success(
            f"Prediction: Not Canceled ✅ "
            f"(Probability: {prob:.2f})"
        )

    else:
        st.error(
            f"Prediction: Canceled ❌ "
            f"(Probability: {1 - prob:.2f})"
        )