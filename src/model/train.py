"""
This module trains the processed dataset.

Regression models used are linear regressor, random forest estimator and gradient boosting estimator.
Metrics for selecting the good models is regression models with a RMSE < 7
"""

# Standard Imports
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Module imports
from src.features import features
from src.data import generate_transformed

# Split the dataset into features and labels
X = features.processed.values
labels_source = generate_transformed.data_70
y = labels_source['Y house price of unit area'].values

# Separate the Features and labels into training and test splits, 70-30%
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

# Define preprocessing for numeric columns (scale them)
numeric_features = [0, 1, 2, 3, 4]
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())])

# Combine Preprocessing Steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features)])

# Create Preprocessing and Training Pipelines
# Linear regressor
pipeline_l = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', LinearRegression())])

# Random forrest regressor
pipeline_rf = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor())])

# Gradient boosting regressor
pipeline_gb = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', GradientBoostingRegressor())])

# Fit the Pipeline to train a Linear Regression Model on the training dataset
model_l = pipeline_l.fit(X_train, y_train)

# Fit the Pipeline to train a Random Forest Estimator on the training dataset
model_rf = pipeline_rf.fit(X_train, y_train)

# Fit the Pipeline to train a Gradient Boosting Estimator on the training dataset
model_gb = pipeline_gb.fit(X_train, y_train)
