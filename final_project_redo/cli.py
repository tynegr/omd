import click
from pizza import Pizza, MargheritaPizza, PepperoniPizza, HawaiianPizza


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
    available_pizzas = ['margherita', 'pepperoni', 'hawaiian']

    if pizza not in available_pizzas:
        print('Нет в меню или неверное название')

    pizza_obj = None

    if pizza == 'margherita':
        pizza_obj = MargheritaPizza(size)
    elif pizza == 'pepperoni':
        pizza_obj = PepperoniPizza(size)
    elif pizza == 'hawaiian':
        pizza_obj = HawaiianPizza(size)

    if isinstance(pizza_obj, Pizza):
        pizza_obj.bake()

        if delivery:
            pizza_obj.deliver()
            if pickup:
                pizza_obj.pickup()
    else:
        print('Нельзя приготовить, так как нет в меню или неверное название')


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
