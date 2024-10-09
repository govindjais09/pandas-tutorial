#Create Categorical Series in Pandas

import pandas as pd

#create a categorical series

s = pd.Series( ['p','q','r','s','q'], dtype='category')

#Display the Series
print('Series=\n' , s)