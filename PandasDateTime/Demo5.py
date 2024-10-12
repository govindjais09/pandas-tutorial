#Check if the year is a leap year

import pandas as pd

#Timestamp
timeStamp = pd.Timestamp(year=1997 , month=12 , day =9 , hour=5 , minute=55)
print('Timestamp:\n' , timeStamp)

#Display day of the week
print('Is this year a leap year?\n' , timeStamp.is_leap_year)