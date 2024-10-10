#Pandas itertuples() to iterate over rows

import pandas as pd
data = {
    'Id': ['s01' , 's02', "s03" , 's04' , 's05'],
    'Student' : ['Amit' , 'John' , 'Jacob' , 'David' , 'Steve'] ,
    'Rank' : [1,4,3,5,2],
}

df = pd.DataFrame(data)
print("Students Records\n" , df)

print("\nPrinting usings itertuples() method")
#Iterate over rows
for x in df.itertuples():
    print("\n",x)