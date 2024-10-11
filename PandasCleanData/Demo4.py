#Pandas fillna() method

import pandas as pd

#Input CSV file
#Load the CSV in DataFrame

df=pd.read_csv("C:\\Users\\govin\\PycharmProjects\\pandas-tutorial\\PandasCleanData\\Demo.csv")

print('Our DataFrame',df)

#Find and replace  null values with specific value 111
resDF=df.fillna(111)

#return the new DataFrame
print('\nNew DataFrame=\n',resDF.to_string())
