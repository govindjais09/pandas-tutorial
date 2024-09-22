#iterate a panda dataframe to display column name

import pandas as pd

data = {
    'student' : ["Amit" , "John" , "Jacob" , "David" , "Steve"] ,
    'rank' : [1,2,3,4,5],
    'marks' : [95,85,75,60,55]

}
wA
df=pd.DataFrame(data , index = ["s1" , "s2" , "s3" , "s4" , "s5"])

print("\nStudent Records by iterating column names\n\n")

for col in df:
    print(col)
