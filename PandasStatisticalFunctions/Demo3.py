#max() method in Python Pandas

import pandas as pd

#DataSet
marks = {
    'Maths':[90 , 85 , 98 , 80 , 55 , 78],
    'Science':[92 , 87 , None ,None , 87 , 96],
    'English':[95 , 94 , 84 , 75, 67 , None]
}

#DataSet
df = pd.DataFrame(marks)

#Display the DataFrame
print('DataFrame =\n' , df)

#Display the maximum value in each column
print('\nMaximum Value\n' ,df.max())