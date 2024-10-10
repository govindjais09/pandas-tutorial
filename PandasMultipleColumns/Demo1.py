#Select two columns with Pandas

import pandas as pd

#DataSet
data = {
    'Student' : ['Amit' , 'John' , 'Jacob' , 'David' , 'Steve'] ,
    'Rank' : [1,4,3,5,2],
    'Marks' : [95,70,80,60,90]
}

df = pd.DataFrame(data)

print('Students Records\n' , df)

print('Ranks and Marks\n' , df[['Rank' , 'Marks']])