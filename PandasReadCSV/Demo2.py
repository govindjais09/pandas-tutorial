#Displaying the top n rows of the DataFrame in Pandas

import pandas as pd

#Input csv file
#loading CSV in a DataFrame

df = pd.read_csv("C:\\Users\\govin\\PycharmProjects\\pandas-tutorial\\PandasReadCSV\\Students.csv")

#Display the CSV file records
print('Our DataFrame = \n' ,df)

#Display the top n records
print('Top 5 rows \n ', df.head())
print('Top 2 rows \n ', df.head(2))