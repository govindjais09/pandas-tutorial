#lstrip() method in Python Pandas

import pandas as pd

#Data  be stored in the Pandas Series
data = ['! !Jacob !' , '\n\nAmit' ,'Trent' ,'Nathan\t' , 'Martin']
series=pd.Series(data)

#Display the series
print("Displaying the Following Series\n=" ,series )

#Strip the values
print('Striping the whitespace and specific character from the left sides\n' , series.str.lstrip(' !\n\t'))
