#Check if the date is the first day of the year

import pandas as pd

#Timestamp
timeStamp = pd.Timestamp(year=1997 , month=1 , day =1 , hour=5 , minute=55)
print('Timestamp:\n' , timeStamp)

#Display day of the week
print('Is this date is the first day of the year?\n' , timeStamp.is_year_start)