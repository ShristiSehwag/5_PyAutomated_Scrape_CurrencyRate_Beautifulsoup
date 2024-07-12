import requests
from datetime import datetime
import time

ticker = input("Enter a ticker symbol (Eg : AAPL,MSFT): ")
from_date = input('From Date (YYYY-MM-DD): ')
to_date = input('To Date (YYYY-MM-DD): ')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))

url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true"

headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
}

#bite object
content = requests.get(url, headers= headers ).content
print(content)

with open('data3.csv', 'wb') as file:
  file.write(content)
  


