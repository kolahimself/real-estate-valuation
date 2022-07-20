""
generate_dataset.py

This module generates the raw dataset from the data// directory and loads the data into a pandas dataframe.
"""

import pandas as pd
import os

from utilities import settings as s


def load(data_loc: str):
    """
    Load the real estate valuation dataset into a pandas dataframe
    
    Parameters:
        :parameter raw_data_loc: string file name path to the dataset in an Excel format.
    
    Returns 
        :returns dataset: pandas dataframe
    """

    dataset = pd.read_excel(raw_data_loc)

    return dataset


# Get the directory for the raw dataset
raw_data_loc = os.path.join(s.DATA_RAW, s.DATASET_NAME)

# Load the dataset
dataset = load(raw_data_loc)
