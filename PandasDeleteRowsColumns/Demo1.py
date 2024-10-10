#Drop columns using drop() method

import  pandas as pd
#DataSet
data = {
    'Id': ['s01' , 's02', "s03" , 's04' , 's05'],
    'Roll' : [100,101,102,103,104],
    'Student' : ['Amit' , 'John' , 'Jacob' , 'David' , 'Steve'] ,
    'Rank' : [1,4,3,5,2],
    'Marks' : [95,70,80,60,90],
    'Address' : ['East' , 'North-East' , 'West' , 'North-West' , 'South']
}

df= pd.DataFrame(data)

print('Student Records\n',df)

print("Droping Marks Column\n")
df=df.drop('Marks',axis=1)
print("Updated Dataset\n" , df)
