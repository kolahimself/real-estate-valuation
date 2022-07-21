"""
This module makes predictions on the testing set using the trained model.

The predictions are plotted against the actual labels as .png files and saved to /images.
"""
import os
import matplotlib.pyplot as plt
import numpy as np

import utilities.settings as s
from src.model.train import *

# Evaluate the linear regression model on the test subset of the processed data
l_predictions = model_l.predict(X_test)

# Evaluate the Random Forest Regression model on the test subset of the processed data
rf_predictions = model_rf.predict(X_test)

# Evaluate the Gradient Boosting regression model on the test subset of the processed data
gb_predictions = model_gb.predict(X_test)


def plot_predictions():
    """
    Plots the predicted results vs actual labels from the trained model
    """

    # Define the calculated predictions
    predictions = [gb_predictions, l_predictions, rf_predictions]

    # Define file titles
    titles = ['Gradient-Boosting-Regressor-predictions.png',
              'Linear-Regression-predictions.png',
              'Random-Forest-Regressor-predictions.png']

    for pred, t in zip(predictions, titles):

        # Plot predicted vs actual
        plt.scatter(y_test, pred)
        plt.xlabel('Actual Labels')
        plt.ylabel('Predicted Labels')
        plt.title('Price Per Unit Predictions')

        # overlay the regression line
        z = np.polyfit(y_test, pred, 1)
        p = np.poly1d(z)
        plt.plot(y_test, p(y_test), color='magenta')

        # Save the plot
        plt.savefig(os.path.join(s.IMAGES_PRED, t))


plot_predictions()
