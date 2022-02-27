import asyncio

from impl.build_app import build_app


async def main():
    await build_app()


if __name__ == '__main__':
    asyncio.run(main())
