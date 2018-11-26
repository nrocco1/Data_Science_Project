#!/usr/bin/env python2.7

# Computing the rolling average of the equity premium

import pandas as pd
import numpy as np


if __name__ == '__main__':
    df = pd.read_csv("raw_predictors_until2013.csv")
    
    df['premium'] = df['CRSP_SPvw'] - df['Rfree']

    premium = 0
    count = 0
    
    temp = df['premium']
    
    cumsum = []
    
    for i in temp:
        premium += i
        count += 1
        cumsum.append(premium/count)
    
    df['cumsum'] = cumsum
