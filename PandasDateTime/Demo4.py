#Get the days in a month
from calendar import month

import pandas as pd

#Timestamp
timeStamp = pd.Timestamp(year=1997 , month=12 , day =9 , hour=5 , minute=55)
print('Timestamp:\n' , timeStamp)

#Display day of the week
print('Display days in the month:\n' , timeStamp.days_in_month)