#upper() method in Python Pandas
import pandas as pd

#Data to be stored in the Pandas Series
data = ['JacOb' , 'AmiT' , 'TRent' , 'Nathan' , 'MaRTIn']

#Create a Series using Series() method
series = pd.Series(data)

print('Series\n' , series)

#Convert to let the data to uppercase
print('UpperCase Data=\n' ,series.str.upper())