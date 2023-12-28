async def task_1(i: int, order: list[int]) -> None:
    """
    Асинхронная функция task_1.

    Args:
    - i (int): Входной параметр.
    - order (list[int]): Список, куда добавляются значения для отслеживания порядка исполнения.

    Returns:
    - None
    """
    if i == 0:
        return

    if i > 5:
        order.append(1)
        await task_2(i // 2, order)
    else:
        order.append(2)
        await task_2(i - 1, order)


async def task_2(i: int, order: list[int]) -> None:
    """
    Асинхронная функция task_2.

    Args:
    - i (int): Входной параметр.
    - order (list[int]): Список, куда добавляются значения для отслеживания порядка исполнения.

    Returns:
    - None
    """
    if i == 0:
        return

    if i % 2 == 0:
        order.append(3)
        await task_1(i // 2, order)
    else:
        order.append(4)
        await task_2(i - 1, order)


async def coroutines_execution_order(i: int = 42) -> int:
    """
    Выполняет асинхронные задачи task_1 и task_2, отслеживает порядок исполнения и возвращает число,
    соответствующее этому порядку.

    Args:
    - i (int): Входной параметр.

    Returns:
    - int: Число, соответствующее порядку исполнения задач.
    """
    order = []
    await task_1(i, order)
    return int(''.join(map(str, order)))
