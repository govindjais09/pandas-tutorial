#Read an excel file in Pandas

import pandas as pd

#Input the excel file
#Load the excel in the DataFrame
df = pd.read_excel(r"C:\Users\govin\PycharmProjects\pandas-tutorial\PythonReadExcel\Crickets.xlsx")

#Display the excel file records
print("Our DataFrame=\n" , df)