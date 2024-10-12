#strip() method in Python Pandas

import pandas as pd

#Data  be stored in the Pandas Series
data = ['!Jacob' , 'Amit\n\n' ,'Trent' ,'Nathan\t' , 'Martin']
series=pd.Series(data)

#Display the series
print("Displaying the Following Series\n=" ,series )

#Strip the values
print('Striping the whitespace and specific character from the both sides\n' , series.str.strip('!\n\t'))
