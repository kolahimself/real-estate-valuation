"""
This module saves trained models as pickle (.pkl) files for scoring
"""

import joblib
import os

import utilities.settings as s
from src.model.train import *


def save_pkl():
    """
    Saves trained models as .pkl files in //models directory.
    """

    # Define trained models
    models = [model_gb, model_l, model_rf]

    # Define Save locations
    loc = [s.MODEL_GB, s.MODEL_L, s.MODEL_RF]

    # Define model titles
    titles = ['GradientBoostingRegressor-model.pkl',
              'linear-regression-model.pkl',
              'RandomForestRegressor-model.pkl']

    for m, t, l in zip(models, titles, loc):
        joblib.dump(m, os.path.join(l, t))


save_pkl()
