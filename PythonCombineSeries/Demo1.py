#Combine two Pandas Series

import pandas as pd

#data
data1 = [10, 20, 40, 80, 100]
data2 = [25, 5, 75, 95, 45]

#create a series using the Series() method
series1 = pd.Series(data1)
series2 = pd.Series(data2)

#Display the series
print('Series 1 \n', series1)
print('Series 2 \n', series2)


def fun(a, b):
    if a > b:
        return a
    else:
        return b


#Combine two series
res = series1.combine(series2, fun)  #we have to pass a function also

#Display the result
print('\n\nAfter Combine\n\n', res)
