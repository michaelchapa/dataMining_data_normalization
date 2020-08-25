import pandas as pd
import numpy as np

def getMean(data):
    rows, _ = data.shape
    data = data[data.columns[3:]].sum(axis = 0)
    data = data / rows
    print(data)

def getMidRange(data):
    rows, _ = data.shape
    midranges = []
    
    data.sort_values(by='C', inplace = True)
    midranges.append(data.loc[(rows // 2), 'C'])
    
    data.sort_values(by='D', inplace = True)
    midranges.append(data.loc[(rows // 2), 'D'])
    
    data.sort_values(by='E', inplace = True)
    midranges.append(data.loc[(rows // 2), 'E'])
    
    data.sort_values(by='F', inplace = True)
    midranges.append(data.loc[(rows // 2), 'F'])
    
    print(midranges)
    
# def getMode(data):
    
    
    
data = pd.read_csv('https://raw.githubusercontent.com/michaelchapa/dataMining_data_normalization/master/hwk01.csv')
getMean(data)
getMidRange(data)
