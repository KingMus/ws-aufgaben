"""Class for a own implementation of a self-organizing map (SOM).

Description
-----------
... some stuff

Names of the students
---------------------
1. Marco Mueller
2.

"""
import numpy as np
import pandas as pd
import random

class SOM:

    def __init__(self, df, label, somRows, somColumns):

        self.df = pd.DataFrame(data = df)
        self.label = pd.Series(label)
        self.somRows = somRows
        self.somColumns = somColumns

        self.map = self.generateRandomMap()

        print(df.info())
        print(label[0])
        print(somRows)
        print(somColumns)


    def generateRandomMap(self):

        #shape describes tupel of dimensions
        nFeatures = self.df.count().shape[0]

        #zeros initializes random map
        map = np.zeros([self.somRows, self.somColumns, nFeatures], dtype=float)

        for row in range(self.somRows):
            for col in range(self.somColumns):
                for feature in range(nFeatures):

                    #find random value between min and max value in dataframe
                    minValueInDf = np.nanmin(self.df.iloc[:, feature].values)
                    maxValueInDf = np.nanmax(self.df.iloc[:, feature].values)
                    neuronFeature = np.random.uniform(minValueInDf, maxValueInDf, 1)
                    map[row][col][feature] = neuronFeature

        return map

    def getRandomValue(self):

        return (self.df.sample(n=1)).as_matrix().squeeze()

    #Competition
    def findBestMatchingUnit(self, randomValue):

        bmu = self.map[0][0] #set an inital bmu
        bmuRowI = 0
        bmuColI = 0
        bmuDistance = float("inf")  #max float number to have highest possible distance

        for row in range(self.somRows):
            for col in range(self.somColumns):

                dist = np.linalg.norm(randomValue - self.map[row][col]) #euclidean norm
                if (dist < bmuDistance): #store all important values for this neighbour if it is nearer than the last nearest neighbour
                    bmu = self.map[row][col]
                    bmuRowI = row
                    bmuColI = col
                    bmuDistance = dist

        print("sample:{0}, bmu:{1}\n".format(randomValue, bmu))

        return [bmuRowI,bmuColI]


    #Cooperation
    def findNeighbours(self, bumRowI, bumColI):

        neighborhood_radius = int(sqrt(self.somRows*self.somColumns * 0.03))  # influence 5% of neurons at the beginning

        #find all neighbours in radius and adjust their weights
        for nr in range(neighborhood_radius):
            for row in range(self.somRows):
                for col in range(self.somColumns):
                    if(row - nr == bmuRowI):
                        self.adjustmentOfWeights([bmuRowI, bmuColI], [row - nr, col], (1 / (nr + 2)))
                    if(row + nr == bmuRowI):
                        self.adjustmentOfWeights([bmuRowI, bmuColI], [row + nr, col], (1 / (nr + 2)))
                    if(col - nr == bmuColI):
                        self.adjustmentOfWeights([bmuRowI, bmuColI], [row, col - nr], (1 / (nr + 2)))
                    if(col + nr == bmuColI):
                        self.adjustmentOfWeights([bmuRowI, bmuColI], [row, col + nr], (1 / (nr + 2)))



    #Adaption
    def adjustmentOfWeights(self, bmuC, infC, alpha):
        distance = np.subtract(self.map[infC[0], infC[1]], self.map[bmuC[0], bmuC[1]])
        adapionValues = distance * alpha
        self.map[infC[0], infC[1]] = np.subtract(self.map[infC[0], infC[1]], adapionValues)


    def train(self):

        randomValue =  self.getRandomValue();

        bmu = self.findBestMatchingUnit(randomValue)
        bmuRowI = bmu[0]
        bmuColI = bmu[1]

        self.findNeighbours(bumRowI,bumColI)
