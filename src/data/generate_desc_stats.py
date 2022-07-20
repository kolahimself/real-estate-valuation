"""
generate_desc_stats.py

This module generates descriptive statistics of the data set in an Excel format.
"""

import pandas as pd
import os

from utilities import settings as s
from src.data import generate_dataset


def describe(dataframe):
    """

    :param dataframe: The real estate transactions already loaded as a pandas dataframe.
    :return: description: a descriptive dataframe consisting of: count, mean, std, quartiles,
             min and max values of each column in the dataframe.
    """

    description = dataframe.describe()

    return description


def export() -> None:
    """
    exports desc_stats.xlsx as n excel file containing descriptive stats.
    """

    # Generate the descriptive statistics
    dataset = generate_dataset.dataset

    # Generate the descriptive data set
    description = describe(dataset)

    # Define the export location
    filename = 'desc_stats.xlsx'
    export_loc = os.path.join(s.DATA_INTERIM, filename)

    # Export the data
    description.to_excel(export_loc, index=True)


export()
