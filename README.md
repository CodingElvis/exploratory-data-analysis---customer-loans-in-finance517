# Exploratory Data Analysis - Customer Loans in Finance


## Overview
This repository describes an Exploratory Data Analysis (EDA) project which has been undertaken as part of AiCore's Bootcamp in Data Analytics, and follows AiCore guidance.

A dataset is accessed from an RDS database (saved here as a CSV file).  The dataset contains information about a portfoilo of 54000 customer loans.  We undertake the core tasks of an EDA including:
- assigning data to appropriate datatypes
- handling null/missing values
- testing for skewness and transforming skewed variables
- considering the role of outliers
- considering the issue of collinearity.

We then progress to querying the data.  We consider questions such as the losses and revenue shortfalls that payment problems generate and what indicators might help to predict the likelihoods of a loan experiencing such problems. 

## Installation
Install by cloning `https://github.com/CodingElvis/exploratory-data-analysis---customer-loans-in-finance517.git`

## Usage
Open the file `overview.ipynb` which runs and documents all stages of the analysis.

## File Structure

### Core file

`overview.ipynb`

### Supporting classes and functions

`data_frame_transform.py`
`data_transform.py`
`DataFrameInfo.py`
`plotter.py`
`load.py`

### Annex to core file

`datatypes.ipynb`

### Getting hold of the data

`db_utils.py`

### Dataset in csv form

`intial_data.csv`


## Licence
MIT Licence