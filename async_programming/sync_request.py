import requests
import os
import time

api_key = os.getenv('KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA']
results = []

start = time.time()
for symbol in symbols:
    print('Working on symbol {}'.format(symbol))
    response = requests.get(url.format(symbol, api_key))
    results.append(response.json())
end = time.time() 
total_time = end - start
print('It took {} seconds to make {} API calls'.format(total_time, len(symbols)))
print('Well done, you did it!')