#Split the object and combine the result in Pandas

import pandas as pd

data ={
    'Player' : ['Amit' , 'John' , 'Amit' , 'David' , 'Steve','John'] ,
    'Rank' : [1,4,3,5,2,7] ,
    'Year' : [2023,2022,2021,2018,2019,2016]
}

#DataFrame
df=pd.DataFrame(data)

#Display the records
print('Cricket Player Records=\n', df)

#Group the data on Player Value
res=df.groupby("Player")

#Display the First Entry
print('\n', res.first())