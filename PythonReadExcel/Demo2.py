#Display top n rows of the DataFrame in Pandas

import pandas as pd

#Input the excel file
#Load the excel in the DataFrame
df = pd.read_excel(r"C:\Users\govin\PycharmProjects\pandas-tutorial\PythonReadExcel\Crickets.xlsx")

#Display the excel file records
print("Our DataFrame=\n" , df)

#Display top n rows from excel
print('Top 5 Records=\n', df.head())

#Display top 2 rows from excel
print('Top 2 Records=\n', df.head(2))