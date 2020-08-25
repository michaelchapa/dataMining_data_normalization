import pandas as pd
import numpy as np

# A)
# 1. Calculate Mean & Midrange
def getMean(data):
    rows, _ = data.shape
    data = data[data.columns[3:]].sum(axis = 0)
    data = data / rows
    return data

# def getMidRange(data):
    
    
    
data = pd.read_csv('https://raw.githubusercontent.com/michaelchapa/dataMining_data_normalization/master/hwk01.csv')
series = getMean(data)
print(series)
