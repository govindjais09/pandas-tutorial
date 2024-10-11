#Sort the Pandas DataFrame (default ascending order)

import pandas as pd

#DataSet

data= {
    'Student': ['Amit' , 'John' , 'Jacob' ,'David' ,'Steve'] ,
    'Rank' : [1,4,3,5,2],
    'Marks' : [95 ,70,80,60,90]
}

#Create a DataFrame
df =pd.DataFrame(data, index=['RowA','RowB','RowC','RowD','RowE'])

#Display
print('Student Records\n' , df)

#Sort the DataFrame in ascending order by Rank
df=df.sort_values(by= 'Rank')

print('After Sorting DataFrame=\n' , df)