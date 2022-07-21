"""
This module demonstrates a use of the machine learning model on a new dataset

The saved trained model is used to predict the price per unit for new real estate transactions
"""

import joblib
import os
import numpy as np

import utilities.settings as s

# Load the model from file
filename = os.path.join(s.MODEL_GB, 'GradientBoostingRegressor-model.pkl')
loaded_model = joblib.load(filename)

# Create a numpy array containing a new observation for 2 new real estate transactions
X_new = np.array(
    [
        [16.2, 289.3248, 5, 24.98203, 121.54348],
        [13.6, 4082.015, 0, 24.94155, 121.50381]
    ])

# Use the model to predict the price-per-3.3m-square-unit for the new real estate transactions
results = loaded_model.predict(X_new)
print('Price Per Unit 3.3 Square-Metre')
for unit_price in results:
    print(np.round(unit_price))
