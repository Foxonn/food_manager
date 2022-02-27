import asyncio
from typing import (
    Dict,
    Any,
)

from impl.build_app import build_app


async def main():
    ioc: Dict[Any, Any] = {}
    await build_app(ioc)

    print('\n' + '*' * 30)
    print(*[*ioc], sep='\n\r')
    print('*' * 30 + '\n')


if __name__ == '__main__':
    asyncio.run(main())
