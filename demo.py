# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 23:33:20 2020

@author: Admin
"""

import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
!pip install xlrd
df_can = pd.read_excel('https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/Canada.xlsx',
                       sheet_name='Canada by Citizenship',
                       skiprows=range(20),
                       skipfooter=2
                      )

print('Data downloaded and read into a dataframe!')
df_can.shape
df_can.head()
df_can.set_index('OdName', inplace=True)


#### Create a new line code