# pandas ndim attribute

import pandas as pd

#data

data = [10,20,40,80,100]

# create a series using the Series() method
s=pd.Series(data)

#Display the series
print("Series : \n" , s)

#Datatype
print("\nSeries Datatype : " , s.dtype)

#Dimensions
print("\nSeries Datatype : " , s.ndim)
