#Pandas isnull() method

import pandas as pd

#Input CSV file
#Load the CSV in DataFrame

df=pd.read_csv("C:\\Users\\govin\\PycharmProjects\\pandas-tutorial\\PandasCleanData\\Demo.csv")

print('Our DataFrame',df)

#NULL values return as TRUE
resDF=df.isnull()

#return the new DataFrame
print('\nNew DataFrame=\n',resDF.to_string())