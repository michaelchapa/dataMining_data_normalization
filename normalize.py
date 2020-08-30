import pandas as pd
import numpy as np
from scipy.spatial import distance

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

def getFiveSummary(data):
    # fiveList = [[i for i in range(5)] for j in range(4)]
    fiveList = []
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


# Determine the Distance of each row compared to the user input 'p'
# Print out the least distant row
def getDistances(data):
    pValues = input("input 4 values seperated by commas (,):").split(',')
    pValues = [float(i) for i in pValues] # convert String to Float d-type
    print() # for nice formatting :P
    data = data[data.columns[3:]].T # get columns and transpose
    
    # Calculate and print least Euclidean distance
    distances = data.apply(\
        euclideanDistance, result_type = 'reduce', args=(pValues))
    leastDistantIndex = np.argmin(distances) # returns index of row
    print("Least Euclidean Distant columns at row " \
          + str(leastDistantIndex), end='\n')
    print(data[leastDistantIndex], '\n')
    
    # Calculate and print least Manhattan (cityblock) distance
    distances = data.apply(\
        manhattanDistance, result_type = 'reduce', args=(pValues))
    leastDistantIndex = np.argmin(distances)
    print("Least Manhattan Distant columns at row " \
          + str(leastDistantIndex), end='\n')
    print(data[leastDistantIndex], '\n')
    
    # Calculate and print least Supremum distance
    distances = data.apply(\
        supremumDistance, result_type = 'reduce', args=(pValues))
    leastDistantIndex = np.argmin(distances)
    print("Least Supremum Distant columns at row " \
          + str(leastDistantIndex), end='\n')
    print(data[leastDistantIndex], '\n')
    
    # Calculate and print least Cosine distance
    distances = data.apply(\
        cosineDistance, result_type = 'reduce', args=(pValues))
    leastDistantIndex = np.argmin(distances)
    print("Least Cosine Distant columns at row " \
          + str(leastDistantIndex), end='\n')
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

################################### MAIN ####################################    
data = pd.read_csv('https://raw.githubusercontent.com/michaelchapa/' \
                   'dataMining_data_normalization/master/hwk01.csv')
#getMean(data)
#getMidRange(data)
#getFiveSummary(data)
#getDistances(data)
