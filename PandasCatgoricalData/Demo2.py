#Create Categorical DataFrame in Pandas

import pandas as pd
from pandas.core.interchange.dataframe_protocol import DataFrame

#Create a Categorical Dataframe

df=pd.DataFrame({
    'Cat1':list('pqrs') , 'Cat2':list('pqrp') , 'Cat3': list('qrrr')
} , dtype='category')

#Display the DataFrame
print("DataFrame = \n" ,df)

#Display the Datatypes
print('\nDataType of each column=\n' , df.dtypes)