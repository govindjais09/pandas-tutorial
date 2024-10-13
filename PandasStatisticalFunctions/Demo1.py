#sum() method in Python Pandas
from cgi import print_environ_usage

import pandas as pd


#DataSet
marks = {
    'Maths':[90 , 85 , 98 , 80 , 55 , 78],
    'Science' :[92 , 87 , 69 , 64 , 87 , 96] ,
    'English':[95 , 94 , 84 , 75, 67 , 65]
}

#DataSet
df = pd.DataFrame(marks)

#Display the DataFrame
print('DataFrame =\n' , df)

#Display the sum of marks in each column
print('\nSum=\n' ,df.sum())