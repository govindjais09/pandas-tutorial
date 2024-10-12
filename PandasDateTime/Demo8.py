#Check if the date is the last date of the year

import pandas as pd

#Timestamp
timeStamp = pd.Timestamp(year=1997 , month=12 , day =31 , hour=5 , minute=55)
print('Timestamp:\n' , timeStamp)

#Display day of the week
print('Is this date is the last day of the year?\n' , timeStamp.is_year_end)