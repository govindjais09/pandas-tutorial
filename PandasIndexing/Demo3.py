#Indexing in Pandas using iloc[]

import pandas as pd

# Input CSV
# Load the CSV into DataFrame
df = pd.read_csv(r"C:\Users\govin\PycharmProjects\pandas-tutorial\PandasReadCSV\Students.csv", index_col='Student')

# Display the CSV file records
print("Our DataFrame = \n ", df)

#Retrive a Single Row
print("\n" , df.iloc[2])
