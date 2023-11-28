from typing import List, Dict
from decorator import log


class Pizza:
    def __init__(self, size: str = 'L', name: str = 'Pizza',
                 ingredients: List[str] = None):
        """
        Инициализация объекта Pizza.

        :param size: Размер пиццы (по умолчанию L)
        :param name: Название пиццы (по умолчанию 'Pizza')
        :param ingredients: Список ингредиентов (по умолчанию None)
        """
        self.size = size
        self.ingredients: List[str] = []
        self.name = name
        self.ingredients: List[str] = ingredients or []

    def dict(self) -> Dict[str, List[str]]:
        """
        Возвращает словарь с информацией о пицце

        :return: Словарь с размером и ингредиентами пиццы
        """
        return {'size': self.size, 'ingredients': self.ingredients}

    def __eq__(self, other: 'Pizza') -> bool:
        """
        Сравнивает текущую пиццу с другой по размеру и ингредиентам

        :param other: Другой объект Pizza для сравнения
        :return: True, если пиццы одинаковы, False в противном случае
        """
        if isinstance(other, Pizza):
            return (self.size == other.size and
                    set(self.ingredients) == set(other.ingredients))
        return False

    @log('👨‍🍳 Приготовили за {}с!')
    def bake(self):
        """Готовит пиццу"""
        pass

    @log('🛵 Доставили за {}с!')
    def deliver(self):
        """Доставка пиццы"""
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
        return self.name + ' 🍕: ' + ', '.join(self.ingredients)


class MargheritaPizza(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Инициализация объекта MargheritaPizza

        :param size: Размер пиццы (по умолчанию L)
        """
        super().__init__(
            size,
            'Margherita',
            ingredients=['tomato sauce', 'mozzarella', 'tomatoes']
        )


class PepperoniPizza(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Инициализация объекта PepperoniPizza

        :param size: Размер пиццы (по умолчанию L)
        """
        super().__init__(
            size,
            'Pepperoni',
            ingredients=['tomato sauce', 'mozzarella', 'pepperoni']
        )


class HawaiianPizza(Pizza):
    def __init__(self, size: str = 'L'):
        """
        Инициализация объекта HawaiianPizza

        :param size: Размер пиццы (по умолчанию L)
        """
        super().__init__(
            size,
            'Hawaiian',
            ingredients=['tomato sauce', 'mozzarella', 'chicken', 'pineapples']
        )
