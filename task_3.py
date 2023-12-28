import asyncio
from dataclasses import dataclass
from typing import Awaitable, List

@dataclass
class Ticket:
    number: int
    key: str

async def coroutines_execution_order(coros: List[Awaitable[Ticket]]) -> str:
    """
    Выполняет все переданные асинхронные корутины, упорядочивает результаты по полю number
    и возвращает строку, состоящую из склеенных полей key.

    Args:
    - coros (List[Awaitable[Ticket]]): Список асинхронных корутин, возвращающих объекты Ticket.

    Returns:
    - str: Строка, состоящая из склеенных полей key отсортированных по полю number.
    """
    results = await asyncio.gather(*coros)
    sorted_results = sorted(results, key=lambda t: t.number)
    return ''.join(t.key for t in sorted_results)
