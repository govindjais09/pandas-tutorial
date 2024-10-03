#Pandas hasnans attribute

import numpy as np
import pandas as pd

#data

data = [10,20,40,80,100 , np.nan]

# create a series using the Series() method
s=pd.Series(data , name='MyNumberSeries')

#Display the series
print("Series : \n" , s)


print('\nDoes the Series has NaN?' , s.hasnans)