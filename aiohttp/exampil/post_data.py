import asyncio
import aiohttp
from pprint import pprint

async def post_data(url, data):
    async with aiohttp.ClientSession() as session:
        async with session.post(url, json=data) as respone:
            return await respone.json()


if __name__ in "__main__":
    data = {
    "userId": 1,
    "id": 10,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
  },

    url = 'https://jsonplaceholder.typicode.com/posts'
    pprint(asyncio.run(post_data(url, data)))