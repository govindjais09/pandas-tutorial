#Naming your own index also accessing it from labeled

import pandas as pd
data = [10, 20, 40, 80, 100]

#create a series using the Series() method

s=pd.Series(data , index = ['rowA' , 'rowB', 'rowC' , 'rowD' , 'rowE'])
print("\nSeries\n\n" , s)

# accessing an index

index='rowD'
print('Index =' , index ,'Element = ',s['rowD'])