#Check if the date is the last date of the month

import pandas as pd

#Timestamp
timeStamp = pd.Timestamp(year=1997 , month=12 , day =31 , hour=5 , minute=55)
print('Timestamp:\n' , timeStamp)

#Display day of the week
print('Is this date is the end of the month?\n' , timeStamp.is_month_end)