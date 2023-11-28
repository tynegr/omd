from random import randint


def log(template: str):
    """
    Декоратор для логирования времени выполнения функции

    :param template: Шаблон строки для форматирования вывода времени выполнения
    :return: Декорированная функция
    """

    def time_of_function(func):
        def wrapper(*args, **kwargs):
            """
            Обертка вокруг функции для вывода лога с временем выполнения.

            :param args: Позиционные аргументы
            :param kwargs: Именованные аргументы
            :return: Результат выполнения функции
            """
            print(func.__name__, template.format(randint(1, 100)))
            return func(*args, **kwargs)

        return wrapper

    return time_of_function
