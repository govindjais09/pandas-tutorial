#access a value from a Panda Series

import pandas as pd
data = [10 ,20,40,80,100]

#create a series using the Series() method

s=pd.Series(data)
print("\nSeries\n\n" , s)

# accessing an index

index=3
print('Index =' , index ,'Element = ',s[index])