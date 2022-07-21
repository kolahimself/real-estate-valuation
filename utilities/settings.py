""" Configuration file.
All static variables can be assigned in these settings.py file
"""

import os

# Directories
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.getcwd())))

# > data
DATA_DIR = os.path.join(ROOT_DIR, "data")
DATA_EXTERNAL = os.path.join(DATA_DIR, "external")
DATA_INTERIM = os.path.join(DATA_DIR, "interim")
DATA_PROCESSED = os.path.join(DATA_DIR, "processed")
DATA_RAW = os.path.join(DATA_DIR, "raw")

# > images
IMAGES_DIR = os.path.join(ROOT_DIR, "images")
IMAGES_CC = os.path.join(IMAGES_DIR, "categorical-correlations")
IMAGES_LD = os.path.join(IMAGES_DIR, "label-distribution")
IMAGES_NC = os.path.join(IMAGES_DIR, "numerical-correlations")
IMAGES_PRED = os.path.join(IMAGES_DIR, "predictions")

# > models
MODEL_DIR = os.path.join(ROOT_DIR, "models")
MODEL_GB = os.path.join(MODEL_DIR, 'GradientBoostingRegressor')
MODEL_L = os.path.join(MODEL_DIR, 'linear-regression')
MODEL_RF = os.path.join(MODEL_DIR, 'RandomForestRegressor')

DATASET_NAME = "Real estate valuation data set.xlsx"
