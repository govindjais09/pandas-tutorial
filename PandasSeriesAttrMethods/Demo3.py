# pandas size attribute

import pandas as pd

#data

data = [10,20,40,80,100]

# create a series using the Series() method
s=pd.Series(data)

#Display the series
print("Series : \n" , s)

#Size
print("\nSeries Datatype : " , s.size)
