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
    """Self-organizing map implementation"""

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

        print(self.__str__())


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

    def getRandomValue(self);

        return random.choice(self.df)

    #Competition
    def findBestMatchingUnit(self);

        bmu = self.map[0][0] #set an inital bmu
        bmuRowI = 0
        bmuColI = 0
        bmuDistance = float("inf")  #max float number to have highest possible distance

        for row in range(self.somRows):
            for col in range(self.somColumns):

                dist = np.linalg.norm(self.getRandomValue() - self.map[row][col])
                if (dist < bmuDistance):
                    bmu = self.map[row][col]
                    bmuRowI = row
                    bmuColI = col
                    bmuDistance = dist

        print("sample:{0}, bmu:{1}\n".format(self.getRandomValue(), bmu))
        
        return [bmuRowI,bmuColI]


    #Adaption
    def adjustmentOfWeights(self);


        weightNow =


        return weightAfter


        pass
