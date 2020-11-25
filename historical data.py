from iexfinance.stocks import Stock
from iexfinance.stocks import get_historical_data
import datetime
import pandas

start = datetime.date(2020, 1, 1)
end = datetime.date(2020, 3, 1)
api_key = "pk_1d130ebd9d1943458f3443d55bc44c27"

df = pandas.DataFrame(get_historical_data('AAPL', start, end, token = api_key, close_only=True, output_format='pandas'))

# print(df)

df.to_csv(r'/Users/.../aapl_his_dta.csv', index=True)

