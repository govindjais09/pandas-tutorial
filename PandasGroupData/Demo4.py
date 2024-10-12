#Aggregation Operation - Get the mean of the Grouped Data
import numpy as np
import pandas as pd

data ={
    'Player' : ['Amit' , 'John' , 'Amit' , 'David' , 'Steve','John'] ,
    'Rank' : [1,4,3,5,2,7] ,
    'Year' : [2023,2022,2021,2023,2019,2016],
    'Points' : [95,70,65,80,90,50]
}

#DataFrame
df=pd.DataFrame(data)

#Display the records
print('Cricket Player Records=\n', df)

#Use the groupby() to group
groupRes=df.groupby('Year')

#Use the agg() to perform aggregation
print('Mean:\n' , groupRes['Points'].agg(np.mean))