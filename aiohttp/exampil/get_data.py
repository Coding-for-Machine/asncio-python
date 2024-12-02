# import asyncio
# import aiohttp
# from pprint import pprint

# async def get_data(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             return await response.json()
        


# if __name__ in '__main__':
#     url = "https://jsonplaceholder.typicode.com/posts"
#     pprint(asyncio.run(get_data(url)), width=70)


import asyncio
import aiohttp
from pprint import pprint

async def get_data(url):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as respone:
                return await respone.text()
    except:
        print("error")      
if __name__ in "__main__":
    url = "https://jsonplaceholder.typicode.com/posts"
    pprint(asyncio.run(get_data(url)))