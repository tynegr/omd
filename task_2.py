async def magic_func() -> int:
    """
    Пример асинхронной функции, возвращающей целое число.

    Returns:
    - int
        Целое число 42.
    """
    return 42


async def fix_this_code() -> int:
    """
    Асинхронная функция, которую необходимо исправить.

    Returns:
    - int
        Результат выполнения функции `magic_func`.
    """
    return await magic_func()
