#Sort the Pandas DataFrame (default descending order)

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

#Sort the DataFrame in descending order by Rank
df=df.sort_values(by= 'Rank' , ascending=False)

print('After Sorting DataFrame=\n' , df)