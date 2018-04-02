# -*- coding: utf-8 -*-
"""
Created on Thu May 04 00:33:12 2017

@author: muthu
"""

import pandas as py
import matplotlib.pyplot as plt
pd = py.read_csv('C:/Users/muthu/Desktop/DataScience/FinalProject/Correlation2015Data.csv')
#print pd.describe# -*- coding: utf-8 -*-
"""
Created on Thu May 04 00:33:12 2017

@author: muthu
"""

import pandas as py
import matplotlib.pyplot as plt
pd = py.read_csv('C:/Users/muthu/Desktop/DataScience/FinalProject/Correlation2015Data.csv')
#print pd.describe()
from pandas.tools.plotting import scatter_matrix
scatter_matrix(pd, figsize=(50,50), diagonal='kde')
plt.savefig('scatter.png')
plt.show()