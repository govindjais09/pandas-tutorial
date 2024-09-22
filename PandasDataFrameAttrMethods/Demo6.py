#pandas dataframe t attribute
from operator import index

import pandas as pd

#dataset
data = {
    'student' : ["Amit" , "John" , "Jacob" , "David" , "Steve"] ,
    'rank' : [1,2,3,4,5],
    'marks' : [95,85,75,60,55]
}

df=pd.DataFrame(data , index=['rowA','rowB','rowC','rowD','rowE'])

print("Students records\n\n",df)

print("\nTranspose" , df.T)