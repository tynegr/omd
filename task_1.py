from asyncio import Task
from typing import Callable, Coroutine, Any

async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    """
    Асинхронная функция для ожидания выполнения переданной корутины, функции или объекта Task.

    Parameters:
    - f: Union[Callable[..., Coroutine], Task, Coroutine]
        Объект, представляющий собой корутину, функцию или задачу Task.

    Returns:
    - Any
        Результат выполнения переданной корутины или функции.

    Raises:
    - ValueError: Если передан некорректный аргумент.
    """
    if isinstance(f, Callable):
        # Если передана обычная функция (Callable), вызываем её.
        return await f()

    elif isinstance(f, Task):
        # Если передан объект Task, ожидаем его выполнение.
        return await f

    elif isinstance(f, Coroutine):
        # Если передана уже запущенная корутина, ожидаем её завершение.
        return await f

    else:
        raise ValueError('invalid argument')
