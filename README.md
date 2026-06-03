# Hotel Booking Cancellation Predictor

A Machine Learning web application built using Streamlit to predict whether a hotel booking will be canceled or not.

## Features

* Predict booking cancellation status
* Interactive Streamlit UI
* Machine Learning based prediction
* Real-time probability output

## Technologies Used

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Joblib
* XGBoost

## Machine Learning Models Used

* Random Forest Classifier
* Gradient Boosting Classifier
* XGBoost Classifier

## Best Performing Model

Gradient Boosting Classifier achieved the highest accuracy of approximately 83%.

## Input Features

* Lead Time
* Average Price Per Room
* Number of Special Requests
* Total Guests
* Total Nights
* Repeated Guest

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit app:

```bash
streamlit run app.py
```

## Project Structure

```text
Hotel-Booking-Cancellation-Predictor/
│
├── app.py
├── gb_booking_model.pkl
├── requirements.txt
├── README.md
```

## Author

Atreyee Bhattacharyya
