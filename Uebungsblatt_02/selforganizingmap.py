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

class SOM:
    """Self-organizing map implementation"""

    def __init__(self, df, label, somRows, somColumns):

        self.df = pd.DataFrame(data = df)
        self.label = pd.Series(label)
        self.somRows = somRows
        self.somColumns = somColumns

        #self.map = self.generateRandomMap()

        print(df.info())
        print(label[0])
        print(somRows)
        print(somColumns)


        pass
