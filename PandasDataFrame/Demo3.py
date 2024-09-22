#create a pandas dataframe

import pandas as pd

data = {
    'student' : ["Amit" , "John" , "Jacob" , "David" , "Steve"] ,
    'rank' : [1,2,3,4,5],
    'marks' : [95,85,75,60,55]

}

df=pd.DataFrame(data , index = ["rowA" , "rowB" , "rowC" , "rowD" , "rowE"])

# print("Student Records\n\n" ,  df)

print("\nValue = ", df.iloc[[1,2]]) # for access specific row and data you need to paas a list of indexBegin and indexEnd
print("\nValue = " , df.iloc[1:3,0:4])