#Join DataFrame in Pandas

import pandas as pd


data1 = {
    'id' :['501','502','503','504','505'] ,
    'student' : ['Amit' , 'John' ,'Jacob' , 'David' , 'Steve'] ,
    'roll' : [101,102,103,104,105]
}

data2 = {
    'rank':[1,4,3,5,2],
    'marks' : [95,70,80,60,90]
}
#dataframe
df1=pd.DataFrame(data1)
print('\n\nDataframe 1=',df1)
df2=pd.DataFrame(data2)
print('\n\nDataframe 2=',df2)

#join two dataframe
joinedDF =df1.join(df2)
print('\n\nJoined Dataframe =',joinedDF)
