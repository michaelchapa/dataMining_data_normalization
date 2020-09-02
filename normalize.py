import pandas as pd
import numpy as np
from scipy.spatial import distance
from sklearn import preprocessing
import matplotlib.pyplot as plt

def getMean(data):
    rows, _ = data.shape
    data = data[data.columns[3:]].sum(axis = 0)
    data = data / rows
    
    print(data)


def getMidRange(data):
    rows, _ = data.shape
    midranges = []
    attributes = list(data.columns[3:])
    
    for attribute in attributes:
        data.sort_values(by = attribute, inplace = True)
        midranges.append(data.loc[(rows // 2), attribute])
    
    print(midranges)

    
def getMode(data):
    for attribute in ['C', 'D', 'E', 'F']:
        print(data[attribute].value_counts(), '\n')
        
    print("Attribute C is Bimodal")
    print("Attributes D and E have no Mode")
    print("Attribute F is Unimodal")
        

# For each column get Minimum, Maximum, Standard Deviation, Mean and Median
def getFiveSummary(data):
    data = data[data.columns[3:]]
    
    print('Minimum:')
    print(data.apply(np.min, axis = 0, raw = True), end='\n\n')
    print('Maximum:')
    print(data.apply(np.max, axis = 0, raw = True), end='\n\n')
    print('Standard Deviation:')
    print(data.apply(np.std, axis = 0, raw = True), end='\n\n')
    print('Mean:')
    print(data.apply(np.mean, axis = 0, raw = True), end='\n\n')
    print('Median:')
    print(data.apply(np.median, axis = 0, raw = True), end='\n\n')
    
def getCentralTendencySummary(data):
    numericAttributes = data[data.columns[3:]]
    
    print(numericAttributes.mode())
    print(numericAttributes.min())
    print(numericAttributes.max())
    print(numericAttributes.std())
    print(numericAttributes.mean())
    print(numericAttributes.median())
    
    print(numericAttributes.describe())
    
    # Normalized boxplot of the data. Mean zero.
    x = numericAttributes.values # returns numpy array
    scaler = preprocessing.MinMaxScaler(feature_range=(-1, 1))
    xScaled = scaler.fit_transform(x) # returns DataFrame
    numericAttributes = pd.DataFrame(xScaled)
    numericAttributes.boxplot()
    

# Determine the Distance of each row compared to the user input 'p'
# Prints out the least distant row
def getDistances(data):
    pValues = input("input 4 values seperated by commas (,):").split(',')
    pValues = [float(i) for i in pValues] # convert String to Float d-type
    print() # for nice formatting :P
    
    data = data[data.columns[3:]].T # get columns and transpose
    
    instances = [(euclideanDistance, "Euclidean"), 
                 (manhattanDistance, "Manhattan"), 
                 (supremumDistance, "Supremum"), 
                 (cosineDistance, "Cosine")]
    
    # Raw Distances
    for instance in instances:
        distances = data.apply(\
            instance[0], result_type = 'reduce', args = (pValues))
        leastDistantIndex = np.argmin(distances) # returns index of row
        print("Least", instance[1], "Distant columns at row " \
              , str(leastDistantIndex))
        print(data[leastDistantIndex], '\n')
    
    # Normalize data and p-values
    data = data.T
    x = data.values # creates numpy array
    
    xScaled = preprocessing.normalize(x, norm= 'l1')
    pScaled = preprocessing.normalize([pValues], norm= 'l1')
    
    data = pd.DataFrame(xScaled, columns = ['C', 'D', 'E', 'F'])
    data = data.T
    
    pScaled = pScaled.flatten()
    pScaled = pScaled.tolist()
    
    # Normalized Distances
    print('\n\n' + ('*' * 16) + ' Normalized ' + ('*' * 8))
    print('input scaled: \n' + str(pScaled) + '\n')
    for instance in instances:
        distances = data.apply(\
            instance[0], result_type = 'reduce', args = (pScaled))
        leastDistantIndex = np.argmin(distances)
        print("Normalized Least", instance[1], "Distant columns at row " \
              , str(leastDistantIndex))
        print(data[leastDistantIndex], '\n')

    
def euclideanDistance(dataValues, c, d, e, f):
    return distance.euclidean(dataValues, [c, d, e, f])

# Also known as Cityblock distance
def manhattanDistance(dataValues, c, d, e, f):
    return distance.cityblock(dataValues, [c, d, e, f])

# Also known as Chebyshev distance
def supremumDistance(dataValues, c, d, e, f):
    return distance.chebyshev(dataValues, [c, d, e, f])
    
def cosineDistance(dataValues, c, d, e, f):
    return distance.cosine(dataValues, [c, d, e, f])


# Scales the DataFrame into Real Numbers between 0 and 1.
# Input: DataFrame rows consisting of Numeric Attributes. 
# Output: Numeric feature, all instances normalized within [-1, 1] range.
def normalizeMinMax(data):
    data = data[data.columns[3:]]
    x = data.values # returns numpy array
    scaler = preprocessing.MinMaxScaler(feature_range=(-1, 1))
    xScaled = scaler.fit_transform(x) # returns DataFrame
    data = pd.DataFrame(xScaled)
    print(data[0])


# Alternative is sklearn.preprocessing.scale()
def normalizeZScore(data):
    data = data[data.columns[3:]]
    powerTransformer = preprocessing.PowerTransformer(method = 'yeo-johnson')
    data = powerTransformer.fit_transform(data.values)
    data = pd.DataFrame(data)
    print(data[0])
    
    
def normalizeDecimalScale(data):
    data = data[data.columns[3:]]
    scaler = preprocessing.StandardScaler()
    data = scaler.fit_transform(data.values)
    data = pd.DataFrame(data)
    print(data[0])
    
    
################################### MAIN ####################################    
data = pd.read_csv('https://raw.githubusercontent.com/michaelchapa/' \
                   'dataMining_data_normalization/master/hwk01.csv')
#getMean(data)
#getMidRange(data)
#getMode(data)
#getFiveSummary(data)
getCentralTendencySummary(data)
#getDistances(data)
#normalizeMinMax(data)
#normalizeZScore(data)
#normalizeDecimalScale(data)