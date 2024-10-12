#count() method in Python Pandas
import numpy as np
import pandas as pd

#Data to be stored in the Pandas Series
data = [np.nan,'jacOb' , 'amiT' , 'tRent' , 'nathan' , 'maRTIn' , np.nan]

#Create a Series using Series() method
series = pd.Series(data)

print('Series\n' , series)

#Convert to let the data to uppercase
print('Length of all the Data=\n' ,series.count())