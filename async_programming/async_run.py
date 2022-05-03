import asyncio
# import ssl
import aiohttp
import os
import time

api_key = os.getenv('KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA']
results = []

start = time.time()

async def get_symbols():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
            print('Working on symbol {}'.format(symbol))
            response = await session.get(url.format(symbol, api_key), ssl=False)
            results.append(await response.json())

"""Event loop to check for async processes that are performed in the background"""
asyncio.run(get_symbols())


end = time.time() 
total_time = end - start
print('It took {} seconds to make {} API calls'.format(total_time, len(symbols)))
print('Well done, you did it!')