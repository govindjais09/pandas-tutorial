#Remove a Categories in Pandas

import pandas as pd

#Create a Categorical Series

s = pd.Series(['p','q','r','s','q'],dtype='category')

#Display the Series
print('Series =\n' , s)

#Append a category
s=s.cat.remove_categories('q')

#Display the updated category
print('\n\nUpdated Categories\n' ,s)
