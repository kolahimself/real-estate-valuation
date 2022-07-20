"""
generate_explorations.py

This module generates various exploration results in form of .png plots with matplotlib
ALl images generated are saved to //images folder. The generated plots are:

Categorical Correlations,
Label Distribution plots,
& Numerical Correlations
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

import utilities.settings as s
from src.data import generate_dataset, generate_transformed

# Assign a Plot style
plt.style.use('seaborn-bright')


def label_distribution() -> None:
    """
    Saves exploration plots for the label distribution
    """

    # Import the dataset
    data = generate_dataset.dataset

    # Get the labels(Y) column
    label = data['Y house price of unit area']

    # Create a figure for 2 subplots, a histogram and a boxplot
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(9, 12))

    # Plot a Histogram in the first subplot
    ax[0].hist(label, bins=100);
    ax[0].set(ylabel='Frequency');
    ax[0].axvline(label.mean(), color='magenta', linestyle='--', linewidth=2);
    ax[0].axvline(label.median(), color='cyan', linestyle='--', linewidth=2);

    # Plot a boxplot in the second subplot
    ax[1].boxplot(label, vert=False);
    ax[1].set(xlabel='House Price Per 3.3 Meter-Square Unit');

    # Add a title to the figure
    fig.suptitle('House Price Per 3.3 Meter-Square Unit Distribution Plots');

    # Save the plots
    save_loc = os.path.join(s.IMAGES_LD, 'label-distribution.png')
    fig.savefig(save_loc);


def transformed_distribution() -> None:
    """
    Saves exploration plots for the label distribution without outliers
    This function uses transformed data, not yet ready for modelling.
    """

    # Import the transformed dataset
    data_70 = generate_transformed.data_70

    # Get the labels(Y) column
    label_70 = data_70['Y house price of unit area']

    # Create a figure for 2 subplots, a histogram and a boxplot
    fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(9, 12))

    # Plot a Histogram in the first subplot
    ax[0].hist(label_70, bins=100);
    ax[0].set(ylabel='Frequency');
    ax[0].axvline(label_70.mean(), color='magenta', linestyle='--', linewidth=2);
    ax[0].axvline(label_70.median(), color='cyan', linestyle='--', linewidth=2);

    # Plot a boxplot in the second subplot
    ax[1].boxplot(label_70, vert=False);
    ax[1].set(xlabel='House Price Per 3.3 Meter-Square Unit');

    # Add a title to the figure
    fig.suptitle('House Price Per 3.3 Meter-Square Unit Distribution (Eliminated Outliers)');

    # Save the plots
    save_loc = os.path.join(s.IMAGES_LD, 'label-distribution-without-outliers.png')
    fig.savefig(save_loc)


def numerical_correlations() -> None:
    """
    Saves exploration plots for the numerical correlations
    """

    # Import the transformed dataset
    data_70 = generate_transformed.data_70

    # Get the labels(Y) column
    label_70 = data_70['Y house price of unit area']

    # Define numeric features
    numeric_features = data_70[data_70.columns[1:-1]]
    
    # Generate plots for all numeric features
    for col in numeric_features:
        fig = plt.figure(figsize=(9, 6))
        ax = fig.gca()
        feature = data_70[col]
        correlation = feature.corr(label_70)
        plt.scatter(x=feature, y=label_70)
        plt.xlabel(col)
        plt.ylabel('Correlations')
        ax.set_title('Label vs ' + col + '- correlation: ' + str(correlation))
        
        # Save the plots
        plot_name = col + '.png'
        save_loc = os.path.join(s.IMAGES_NC, plot_name)
        fig.savefig(save_loc)


def categorical_correlations() -> None:
    """
    Saves all explorations for categorical correlations
    """

    # Import the transformed dataset
    data_70 = generate_transformed.data_70

    # Get the labels(Y) column
    label_70 = data_70['Y house price of unit area']

    # Define Categorical Features
    categorical_features = data_70[['X1 transaction date', 'X4 number of convenience stores']]

    # Generate plots for all categorical features
    for col in categorical_features:
        fig = plt.figure(figsize=(9, 6))
        ax = fig.gca()
        data_70.boxplot(column='Y house price of unit area', by=col, ax=ax)
        ax.set_title('Label by ' + col)
        ax.set_ylabel("Label Distribution by Categorical Variable")

        # Save the plots
        plot_name = col + '.png'
        save_loc = os.path.join(s.IMAGES_CC, plot_name)
        fig.savefig(save_loc)


def main() -> None:
    """
    main function that saves all plots
    """
    label_distribution()
    numerical_correlations()
    categorical_correlations()

main()
