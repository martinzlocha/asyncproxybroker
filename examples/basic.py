import asyncio

from asyncproxybroker import AsyncProxyBroker


async def get_proxy(proxy_provider):
    print(await proxy_provider.random_proxy())


async def main():
    proxy_provider = AsyncProxyBroker('http://wikipedia.com')
    tasks = [asyncio.create_task(get_proxy(proxy_provider)) for _ in range(100)]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(main())