import click
from random import randint
from typing import List, Dict


def log(template: str):
    """
    Декоратор для логирования времени выполнения функции.

    :param template: Шаблон строки для форматирования вывода времени выполнения
    :return: Декорированная функция.
    """

    def time_of_function(func):
        def wrapper(*args, **kwargs):
            """
            Обертка вокруг функции для вывода лога с временем выполнения.

            :param args: Позиционные аргументы.
            :param kwargs: Именованные аргументы.
            :return: Результат выполнения функции.
            """
            print(func.__name__, template.format(randint(1, 100)))
            return func(*args, **kwargs)

        return wrapper

    return time_of_function


class Pizza:
    def __init__(self, size: str = 'L'):
        """
        Инициализация объекта Pizza.

        :param size: Размер пиццы (по умолчанию L).
        """
        self.size = size
        self.ingredients: List[str] = []

    def add_ingredient(self, ingredient: str) -> None:
        """
        Добавление ингредиента к пицце.

        :param ingredient: Ингредиент для добавления.
        """
        self.ingredients.append(ingredient)

    def dict(self) -> Dict[str, List[str]]:
        """
        Возвращает словарь с информацией о пицце.

        :return: Словарь с размером и ингредиентами пиццы.
        """
        return {'size': self.size, 'ingredients': self.ingredients}

    def __eq__(self, other: 'Pizza') -> bool:
        """
        Сравнивает текущую пиццу с другой по размеру и ингредиентам.

        :param other: Другой объект Pizza для сравнения.
        :return: True, если пиццы одинаковы, False в противном случае.
        """
        return (self.size == other.size and
                set(self.ingredients) == set(other.ingredients))

    @log('👨‍🍳 Приготовили за {}с!')
    def bake(self):
        """Готовит пиццу"""
        pass

    @log('🛵 Доставили за {}с!')
    def deliver(self):
        """Доставка пиццы."""
        pass

    @log('🏠 Забрали за {}с!')
    def pickup(self):
        """
        Забрать пиццу у доставщика

        """
        pass

    def display_menu(self) -> str:
        """
        Вывод меню пиццы в виде строки

        :return: Меню пиццы в виде строки
        """
        return self.__class__.__name__ + ' 🍕: ' + ', '.join(self.ingredients)


class MargheritaPizza(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Инициализация объекта MargheritaPizza.

        :param size: Размер пиццы (по умолчанию L).
        """
        super().__init__(size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('tomatoes')


class PepperoniPizza(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Инициализация объекта PepperoniPizza.

        :param size: Размер пиццы (по умолчанию L).
        """
        super().__init__(size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('pepperoni')


class HawaiianPizza(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Инициализация объекта HawaiianPizza.

        :param size: Размер пиццы (по умолчанию L).
        """
        super().__init__(size)
        self.add_ingredient('tomato sauce')
        self.add_ingredient('mozzarella')
        self.add_ingredient('chicken')
        self.add_ingredient('pineapples')


@click.group()
def cli():
    """Группа команд для управления пиццей """
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--pickup', default=False, is_flag=True,
              help='Include pickup')
@click.option('--size', type=click.Choice(['L', 'XL']),
              default='L', help='Размер пиццы')
@click.argument('pizza', nargs=1)
def order(pizza: str, size: str, delivery: bool, pickup: bool):
    """
    Команда для заказа пиццы

    :param pizza: Вид пиццы для заказа (margherita, pepperoni, hawaiian)
    :param size: Размер пиццы (по умолчанию L)
    :param delivery: Флаг для указания наличия доставки (по умолчанию False)
    :param pickup: Флаг, был ли самовывоз (по умолчанию False)
    """
    if pizza == 'margherita':
        pizza = MargheritaPizza(size)
    elif pizza == 'pepperoni':
        pizza = PepperoniPizza(size)
    elif pizza == 'hawaiian':
        pizza = HawaiianPizza(size)

    pizza.bake()

    if delivery:
        pizza.deliver()
        if pickup:
            pizza.pickup()


@cli.command()
def menu():
    """
    Команда для вывода меню пиццы
    """
    margherita = MargheritaPizza()
    pepperoni = PepperoniPizza()
    hawaiian = HawaiianPizza()

    print('- ' + margherita.display_menu() + '  🧀')
    print('- ' + pepperoni.display_menu() + ' 🍕')
    print('- ' + hawaiian.display_menu() + ' 🍍')


if __name__ == '__main__':
    cli()
