#Check if the date is the first date of the month

import pandas as pd

#Timestamp
timeStamp = pd.Timestamp(year=1997 , month=12 , day =1 , hour=5 , minute=55)
print('Timestamp:\n' , timeStamp)

#Display day of the week
print('Is this date is the start of the month?\n' , timeStamp.is_month_start)