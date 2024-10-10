# Indexing in Pandas using indexing operator []

import pandas as pd

# Input CSV
# Load the CSV into DataFrame
df = pd.read_csv(r"C:\Users\govin\PycharmProjects\pandas-tutorial\PandasReadCSV\Students.csv", index_col='Student')

# Display the CSV file records
print("Our DataFrame = \n ", df)

# Use the Indexing Operator
res = df['Marks']

print("Only Student's Name and their respective Marks=\n\n", res)
