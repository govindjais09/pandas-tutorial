#Pandas items() to iterate over columns

import pandas as pd
data = {
    'Id': ['s01' , 's02', "s03" , 's04' , 's05'],
    'Student' : ['Amit' , 'John' , 'Jacob' , 'David' , 'Steve'] ,
    'Rank' : [1,4,3,5,2],
}
df = pd.DataFrame(data)
print("Students Records\n" , df)

#Iterate over columns
print('\nIterate over each column')
for a,b in df.items():
    print(a) # column name
    print(b) # column data
