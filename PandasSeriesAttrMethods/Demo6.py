#Pandas index attribute

import pandas as pd

#Data
data = [10,20,40,80,100]

# create a series using the Series() method
s=pd.Series(data ,index=[1,2,3,4,5] ,name='MyNumberSeries')

#Display the series
print("Series : \n" , s)

