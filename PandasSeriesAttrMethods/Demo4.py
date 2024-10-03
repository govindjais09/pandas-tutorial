# pandas name attribute

import pandas as pd

#data

data = [10,20,40,80,100]

# create a series using the Series() method
s=pd.Series(data , name='MyNumberSeries')

#Display the series
print("Series : \n" , s)

#Display Series Name
print('\nSeries Name :' , s.name)
