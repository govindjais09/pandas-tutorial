#create a pandas dataframe

import pandas as pd

data = {
    'student' : ["Amit" , "John" , "Jacob" , "David" , "Steve"] ,
    'rank' : [1,2,3,4,5],
    'marks' : [95,85,75,60,55]

}

df=pd.DataFrame(data , index = ["s1" , "s2" , "s3" , "s4" , "s5"])

print("Student Records\n\n" ,  df)
