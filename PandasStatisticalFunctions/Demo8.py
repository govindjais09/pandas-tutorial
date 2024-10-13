#describe() method in Python Pandas

import pandas as pd

#DataSet
marks = {
    'Maths':[90 , 85 , 98 , 80 , 55 , 78],
    'Science':[92 , 87 , 85 ,96 , 87 , 96],
    'English':[95 , 94 , 84 , 75, 67 , 87]
}

#DataSet
df = pd.DataFrame(marks)

#Display the DataFrame
print('DataFrame =\n' , df)

#Display the summary using describe() method
print('\nSummary of Statistics\n' ,df.describe())