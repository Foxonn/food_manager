from typing import Any
from typing import Dict

__all__ = ['DishDbModelJSONEncoder']


class DishDbModelJSONEncoder:
    __slots__ = ()

    def __call__(self, object: Any) -> Dict:
        print('\n' + '*'*30)
        print(*[object], sep='\n\r')
        print('*'*30 + '\n')
