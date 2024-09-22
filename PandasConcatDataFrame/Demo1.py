#concatenate two pandas dataframe

import pandas as pd

#datasets

data1 = {
    'id' : ['S01' , 'S02' , 'S03' , 'S04' , 'S05'] ,
    'students' : ['Amit' ,'Jacob' , 'Steve' , 'Daniel' , 'Robert'],
    'roll' : [101 ,102 ,103 ,104, 105]
}

data2 = {
    'id' : ['S06' , 'S07' , 'S08'] ,
    'students': ['Ben' ,"Kane" ,"Rohit"] ,
    'roll' : [106 , 107 , 108]
}

resultDataFrame = pd.concat([pd.DataFrame(data1) ,pd.DataFrame(data2)]) #dataframe1 and dataframe2

print("\n\n Concatinated DataFrame\n" ,resultDataFrame)
