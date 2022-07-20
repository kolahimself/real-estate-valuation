"""
This module subtly drops columns or fields that are not potentially predictive

This module contains functions that export the processed data as well.
"""

import os
import pandas as pd

import utilities.settings as s
from src.data import generate_transformed


def process(transformed_dataset):
    """
    Prepares the dataset for machine learning modelling by keeping potentially predictive fields,
    discards unnecessary fields as well.

    :param transformed_dataset: (dtype object) the transformed/interim data to be processed for modelling

    :return: x: dataset ready to be modelled
    """

    # Define columns that are not potentially predictive.
    unnecessary = ['No', 'X1 transaction date', 'Y house price of unit area']

    # Drop columns that are not potentially predictive.
    x = transformed_dataset.drop(labels=unnecessary, axis=1)

    return x


# Import the transformed dataset
transformed = generate_transformed.data_70

# Prepare the data for processing
processed = process(transformed)

# Save the processed data to disk
xlsx_name = "processed.xlsx"
save_path = os.path.join(s.DATA_PROCESSED, xlsx_name)
processed.to_excel(save_path, index=True)
