# for more info refer to "https://github.com/addisonlynch/iexfinance"

import pandas as pd
import datetime
from iexfinance.stocks import get_historical_data
from iexfinance.stocks import Stock

start = datetime.date(2020, 7, 1)
api_key = "pk_1d130ebd9d1943458f3443d55bc44c27"

df = get_historical_data("AAPL", output_format = "pandas", token = api_key, start = start)

print(df.head())

stock = Stock("AAPL", token=api_key)
a = stock.get_company()
# print(a)
print(a['description'])