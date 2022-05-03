import asyncio
from contextlib import suppress
import aiohttp
import os
import time

api_key = os.getenv('KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA', 'MSFT', 'GOOG', 'TSLA']
results = []

start = time.time()


def get_tasks(session):
    tasks = []
    for symbol in symbols:
        # tasks.append(session.get(url.format(symbol, api_key), ssl=False))
        tasks.append(asyncio.create_task(session.get(url.format(symbol, api_key), ssl=False)))
    return tasks


async def get_symbols():
    async with aiohttp.ClientSession() as session:
        tasks = get_tasks(session)
        responses = await asyncio.gather(*tasks)
        for response in responses:
            results.append(await response.json())
        # pass

"""Event loop to check for async processes that are performed in the background"""
asyncio.run(get_symbols())


end = time.time() 
total_time = end - start
print("====================================================================")
print('It took {} seconds to make {} API calls'.format(total_time, len(symbols)))
print(results)
print('Well done, you did it!')
print("====================================================================")