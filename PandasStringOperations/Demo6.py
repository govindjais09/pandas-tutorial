#contains() method in Python Pandas
import pandas as pd

#Data to be stored in the Pandas Series
data = ['jacOb' , 'amiT' , 'tRent' , 'nathan' , 'maRTIn' ]

#Create a Series using Series() method
series = pd.Series(data)

print('Series\n' , series)

#Convert to let the data to uppercase
print('Does the specific value exist on series=\n' ,series.str.contains('amiT'))