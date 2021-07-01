import asyncio
import aiohttp

class HTTPConnection:
  def __init__(self):
    self.session = aiohttp.ClientSession()

  async def request(self, url, params = None):
    async with self.session as session:
        if params is not None:
          async with session.get(url, params=params) as response:
            return await response.json()
        else: 
          async with session.get(url) as response:
            return await response.json()

async def instantiate():
  return HTTPConnection()
