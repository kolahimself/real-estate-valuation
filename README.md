[![License](https://img.shields.io/github/license/kolahimself/real-estate-valuation?style=plastic))](https://opensource.org/licenses/MIT)
[![Open All Collab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1RP79ciXT9nw-sQZoyNObr9pNSP9fP9cE?usp=sharing)
[![GitHub commit](https://img.shields.io/github/last-commit/kolahimself/real-estate-valuation?style=plastic)](https://github.com/kolahimself/real-estate-valuation/commits/main)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=plastic)](http://makeapullrequest.com)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# `Real Estate Valuation`

> this project is an attempt to a regression challenge, view the challenge [here](https://docs.microsoft.com/en-gb/learn/modules/train-evaluate-regression-models/9-summary)

## Description
Predicting the selling price of a residential property depends on a number of factors, including the property age, availability of local amenities, and location.

The contents of this repository and project as a whole are aimed at predicting the price-per-unit of a property on its features using a dataset of real estate transactions. The price-per-unit in this data is based on a unit measurement of 3.3 square meters. The repository contains python scripts, notebooks and excel files.

> **Citation**: The data used in this exercise originates from the following study:
>
> *Yeh, I. C., & Hsu, T. K. (2018). Building real estate valuation models with comparative approach through case-based reasoning. Applied Soft Computing, 65, 260-271.*
>
> It was obtained from the UCI dataset repository (Dua, D. and Graff, C. (2019). [UCI Machine Learning Repository](http://archive.ics.uci.edu/ml). Irvine, CA: University of California, School of Information and Computer Science).
> The dataset can be downloaded [here](https://archive.ics.uci.edu/ml/datasets/Real+estate+valuation+data+set#)

## Objectives
Major objectives to be achieved are:
- Exploration and preparation of data
- Identification of potentially predictive features as regards the price-per-unit-label
- Training a regression model that achieves:
  - a root mean square error (RMSE) not more than 7. 
  - a coefficient of determination at least 80% in value.

## Requirements
Main language used is python, as well as jupyter notebooks. Other python packages required to run:
- Scikit-Learn: [Simple and efficient tools for predictive data analysis](https://scikit-learn.org/)
- Pandas: [An open source data analysis and manipulation tool](https://pandas.pydata.org/)
- Numpy: [Comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more.](https://numpy.org/)
- Matplotlib: [A comprehensive library for creating static, animated, and interactive visualizations](https://matplotlib.org/)
- Joblib: [Running Python functions as pipelines](https://joblib.readthedocs.io/)

## Data Review
An extract from the dataset:

| No	| X1 transaction date	| X2 house age | X3 distance to the nearest MRT station |	X4 number of convenience stores	| X5 latitude	| X6 longitude | Y house price of unit area |
--- | --- | --- | --- |--- |--- |--- |--- 
| 138	| 2013.500 | 13.6	| 319.0708 | 6 | 24.96495	| 121.54277	| 47.4 |

###   Atribute Information

  The inputs are as follows:
  - **X1** = the transaction date (for example, 2013.250=2013 March, 2013.500=2013 June, etc.)
  - **X2** = the house age (unit: year)
  - **X3** = the distance to the nearest MRT station (unit: metres)
  - **X4** = the number of convenience stores in the living circle on foot (integer)
  - **X5** = the geographic coordinate, latitude. (unit: degree)
  - **X6** = the geographic coordinate, longitude. (unit: degree)
      
  The Output:
  - **Y** = house price of unit area ( $10000 (New Taiwan Dollar)/Ping, where Ping is a local unit, 1 Ping = 3.3 meter squared)

## Exploration

![plot](https://github.com/kolahimself/real-estate-valuation/blob/main/images/label-distribution/label-distribution.png)

The plots above show that the house price per 3.3 metre-square unit ranges from 0 to 118. However, the mean (and median) number of daily rentals is closer to the low end of that range, with most of the data between 0 and around 80 units. The few values above this are shown in the box plot as small circles, indicating that they are *outliers* - in other words, unusually high or low values beyond the typical range of most of the data.

The histogram & boxplot plots below show distribution for modified data, the outliers have been removed

![plot](https://github.com/kolahimself/real-estate-valuation/blob/main/images/label-distribution/label-distribution-without-outliers.png)

### Feature Correlations
Scatter plots indicating numeric correlations between house prices and numerical features are shown [in this folder](https://github.com/kolahimself/real-estate-valuation/tree/main/images/numerical-correlations),

Boxplots indicating categorical correlations are shown [in this folder](https://github.com/kolahimself/real-estate-valuation/tree/main/images/categorical-correlations),

> **transaction_date** doesn't seem to be very predictive, so it is ommitted before preprocessing and training.

## Running the Project
Preferably, you can run python scripts directly from `src`. Similar prototypes and explorations in form of notebooks for automation can be viewed here in `notebooks`

## Project Structure Overview
The project structure tree is shown below. This structure is designed in a way to easily develop ML projects. Feedback / PRs are always welcome about the structure.

```
.
├── .github                           # Github actions CI pipeline
|
|── images
|   |── label-distributions           # .png image plots portraying label distribution with and without outliers
|   |── numeric-correlations          # .png image plots showing numeric correlations and observations
|   |── categorical-correlations      # .png image plots showing categorical features and their correlations
|
├── data                
│   ├── external                      # third party data
│   |── interim                       # transformed intermediate data, not ready for modelling
│   ├── processed                     # processed data, ready for modelling
│   ├── raw                           # immutable original data
│   ├── predictions                   # predictions data, calculated using the model
|
├── models              
|   ├── GradientBoostingRegressor     # store a serialized and well fitted GradientBoostingRegressor model
|   ├── RandomForestRegressor         # store a serialized and well fitted RandomForestRegressor model
|   ├── linear-regression             # RMSE > 7, model cannot be used❌
|
├── notebooks                         # Store prototype or exploration related .ipynb notebooks
|
├── reports                           # Store textual or visualisation content, i.e. pdf, latex, .doc, .txt 
|
├── src                               # folder containing project source code
|
└── tests                             # Unit tests
```
