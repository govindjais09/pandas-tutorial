#pandas head() method

import  pandas as pd

#data

data = [10,20,40,80,100,200,300]

# create a series using the Series() method
s=pd.Series(data)

# #Display the series
# print("Series : \n" , s)

#Display first 5 datas
print("\n Last Five Datas\n",s.tail())

#Display first 2 datas
print("\n Last Two Datas\n",s.tail(2))