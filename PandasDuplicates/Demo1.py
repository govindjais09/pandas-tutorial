#Find duplicates using the duplicates()

import pandas as pd

#DataSet
data= {
    'Student': ['Amit' , 'John' , 'Amit' ,'David' ,'Steve'] ,
    'Rank' : [1,4,1,5,2],
    'Marks' : [95 ,70,95,60,90]
}

#Create the DataFrame
df=pd.DataFrame(data)

print('Describing Duplicate\n')

res=df.duplicated()

print(res)