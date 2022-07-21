"""
This module evaluates the trained models using the following metrics:
- Mean squared error
- Root mean squared error
- Coefficient of determination

The results of the metrics above are organized into .xlsx files for easier viewing,
the predicted
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score

from src.model.train import *
from src.model.predict import *
import utilities.settings as s


def metric_evaluator(pred, test_subset):
    """
    Evaluates the metrics of the trained model when its given prediction is plotted against actual labels

    :param pred: a numpy array of generated predictions.
    :param test_subset: the test subset/actual labels to be compared with predictions

    :return ms_error, rms_error, r_two: float, mean squared error, root mean squared error
                                        coefficient of determination of the trained model,
    """

    # Evaluate metrics
    ms_error = mean_squared_error(test_subset, pred)  # Mean squared error
    rms_error = np.sqrt(ms_error)  # Root mean squared error
    r_two = r2_score(test_subset, pred)  # Coefficient of determination

    return [ms_error, rms_error, r_two]


def display_metrics(metrics: list):
    """
    Accepts evaluated metrics (python list) in form of input and returns a pandas dataframe

    :param metrics: python list containing evaluated metrics iin the order:
                    [mean_squared_error, root_mean_square_error, coefficient_of_determination]

    :return: metrics_result pandas dataframe diplaying the evaluated metrics
    """

    metrics_result = pd.DataFrame(
        {
            'Mean Squared Error': pd.Series([metrics[0]]),
            'Root Mean Squared Error': pd.Series([metrics[1]]),
            'Coefficient of Determination': pd.Series([metrics[2]])
        })

    return metrics_result


def main():
    """
    Main function that performs evaluation and saves to disk
    """

    # Import predictions
    predictions = [gb_predictions, l_predictions, rf_predictions]

    # Define file titles
    titles = ['Gradient-Boosting-Regressor-evaluations.xlsx',
              'Linear-Regression-evaluations.xlsx',
              'Random-Forest-Regressor-evaluations.xlsx']

    # Define Save locations
    loc = [s.MODEL_GB, s.MODEL_L, s.MODEL_RF]

    for p, t, l in zip(predictions, titles, loc):
        # Evaluate metrics
        evaluated_metrics = metric_evaluator(p, y_test)

        # Convert to pandas dataframe
        result = display_metrics(evaluated_metrics)

        # Save the pandas dataframe as .xlsx
        result.to_excel(os.path.join(l, t), index=True)


main()
