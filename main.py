# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:43:30 2020

@author: Gaston Tavara
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


training = pd.read_csv('train.csv')
testing = pd.read_csv('test.csv')


# Understand nature of the data .info() .describe()
"""
1) For numeric data
Made histograms to understand distributions
Corrplot
Pivot table comparing survival rate across numeric variables
2) For Categorical Data
Made bar charts to understand balance of classes
Made pivot tables to understand relationship with survival
"""

training.info()



# Histograms and boxplots 
# Value counts 
# Missing data 
# Correlation between the metrics 
# Explore interesting themes 
    # Wealthy survive? 
    # By location 
    # Age scatterplot with ticket price 
    # Young and wealthy Variable? 
    # Total spent? 
# Feature engineering 
# preprocess data together or use a transformer? 
    # use label for train and test   
# Scaling?

# Model Baseline 
# Model comparison with CV 