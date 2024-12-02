import asyncio
import unittest
import aiohttp
# 1 test uchun 
async def run_data():
    await asyncio.sleep(2)
    return "hi"

class run_data_test(unittest.TestCase):
    def run_test_1(self):
        result = asyncio.run(run_data())
        self.assertEqual(result, "Hello Word" )

async def async_task():
    await asyncio.sleep(2)
    return "Done"

class TestAsyncTimeout(unittest.TestCase):
    def test_async_timeout(self):
        async def run_test():
            try:
                await asyncio.wait_for(async_task(), timeout=1)
            except asyncio.TimeoutError:
                return "Timeout"

        result = asyncio.run(run_test())
        self.assertEqual(result, "Timeout")

if __name__ == "__main__":
    unittest.main()
class TestWithSetup(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.data = [1, 2, 3]
        self.result = []

    async def asyncTearDown(self):
        self.data.clear()

    async def test_add_to_result(self):
        for item in self.data:
            await asyncio.sleep(0.1)
            self.result.append(item * 2)
        self.assertEqual(self.result, [2, 4, 6])

if __name__ == "__main__":
    unittest.main()
from unittest.mock import AsyncMock

class TestAsyncMock(unittest.TestCase):
    def test_async_mock(self):
        mock_func = AsyncMock(return_value="Mocked Result")
        result = asyncio.run(mock_func())
        self.assertEqual(result, "Mocked Result")
        mock_func.assert_awaited_once()

if __name__ == "__main__":
    unittest.main()
from unittest.mock import AsyncMock

class TestAsyncMock(unittest.TestCase):
    def test_async_mock(self):
        mock_func = AsyncMock(return_value="Mocked Result")
        result = asyncio.run(mock_func())
        self.assertEqual(result, "Mocked Result")
        mock_func.assert_awaited_once()

if __name__ == "__main__":
    unittest.main()
async def producer(queue):
    for i in range(5):
        await queue.put(i)
        await asyncio.sleep(0.1)

async def consumer(queue):
    result = []
    while not queue.empty() or queue.qsize() > 0:
        item = await queue.get()
        result.append(item)
    return result

class TestAsyncQueue(unittest.TestCase):
    def test_producer_consumer(self):
        async def run_test():
            queue = asyncio.Queue()
            await producer(queue)
            return await consumer(queue)

        result = asyncio.run(run_test())
        self.assertEqual(result, [0, 1, 2, 3, 4])

if __name__ == "__main__":
    unittest.main()

if __name__ in "__main__":
    asyncio.run(run_data())
