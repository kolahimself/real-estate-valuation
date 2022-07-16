[![PythonVersion](https://img.shields.io/pypi/pyversions/py?style=plastic)](https://img.shields.io/pypi/pyversions/py?style=plastic)

# `Real Estate Valuation`

> this project is an attempt to a regression challenge, view the challenge [here](https://docs.microsoft.com/en-gb/learn/modules/train-evaluate-regression-models/9-summary)

## Description
Predicting the selling price of a residential property depends on a number of factors, including the property age, availability of local amenities, and location.

The contents of this repository and project as a whole are aimed at predicting the price-per-unit of a property on its features using a dataset of real estate transactions. The price-per-unit in this data is based on a unit measurement of 3.3 square meters. Python language is used throughout.

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
