"""
generate_transformed.py

This module generates transformed data and saves it to disk

The essence for transforming is to remove outliers, i.e rows with house prices more than 70 per unit.
"""

import pandas as pd
import os

import utilities.settings as s
from src.data import generate_dataset


def data_transformer():
    """

    :return transform: transformed dataset with removed outliers
    :return export_loc: location to save the exported data.
    """
    # Import raw data
    data = generate_dataset.dataset

    # Remove outliers
    transformed = data[data['Y house price of unit area'] < 70]

    # Define the export location for transformed data
    filename = 'transformed-data.xlsx'
    export_loc = os.path.join(s.DATA_INTERIM, filename)

    return transformed, export_loc


data_70, exportLoc = data_transformer()

# Export the Transformed data to //interim data directory
data_70.to_excel(exportLoc, index=False)
