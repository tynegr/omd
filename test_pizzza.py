from click.testing import CliRunner
from pizzza import order, menu, Pizza
import pytest


# Обычные тесты для команды order

def test_order_margherita():
    runner = CliRunner()
    result = runner.invoke(order, ['margherita', '--delivery'])
    assert result.exit_code == 0
    assert 'Приготовили за' in result.output
    assert 'Доставили за' in result.output


def test_order_pepperoni():
    runner = CliRunner()
    result = runner.invoke(order, ['pepperoni'])
    assert result.exit_code == 0
    assert 'Приготовили за' in result.output
    assert 'Доставили за' not in result.output


# Обычный тест для команды menu

def test_menu():
    runner = CliRunner()
    result = runner.invoke(menu)
    assert result.exit_code == 0
    assert 'MargheritaPizza' in result.output
    assert 'PepperoniPizza' in result.output
    assert 'HawaiianPizza' in result.output


# Тесты для команды order с неверными типами данных


def test_order_invalid_size_type():
    runner = CliRunner()
    result = runner.invoke(order, ['margherita', '--size', 'M'])
    assert result.exit_code != 0
    assert 'Error: Invalid value for \'--size\'' in result.output


# Тест для команды menu с неверными типами данных

def test_menu_with_invalid_argument():
    runner = CliRunner()
    result = runner.invoke(menu, ['invalid_argument'])
    assert result.exit_code != 0
    assert 'Error: Got unexpected extra argument' in result.output


def test_order_margherita_no_delivery():
    runner = CliRunner()
    result = runner.invoke(order, ['margherita'])
    assert result.exit_code == 0
    assert 'Приготовили за' in result.output
    assert 'Доставили за' not in result.output

# Тесты с флажками


def test_order_margherita_with_delivery():
    runner = CliRunner()
    result = runner.invoke(order, ['margherita', '--delivery'])
    assert result.exit_code == 0
    assert 'Приготовили за' in result.output
    assert 'Доставили за' in result.output


def test_order_margherita_with_delivery_and_pickup():
    runner = CliRunner()
    result = runner.invoke(order, ['margherita', '--delivery', '--pickup'])
    assert result.exit_code == 0
    assert 'Приготовили за' in result.output
    assert 'Доставили за' in result.output
    assert 'Забрали за' in result.output

# Тесты функций класса Pizza


@pytest.fixture
def pizza_instance():
    """Создает экземпляр класса Pizza для тестирования"""
    return Pizza(size='L')


def test_add_ingredient(pizza_instance):
    pizza_instance.add_ingredient('tomato')
    pizza_instance.add_ingredient('cheese')
    assert pizza_instance.ingredients == ['tomato', 'cheese']


def test_dict(pizza_instance):
    pizza_instance.add_ingredient('tomato')
    pizza_instance.add_ingredient('cheese')
    expected_dict = {'size': 'L', 'ingredients': ['tomato', 'cheese']}
    assert pizza_instance.dict() == expected_dict


def test_eq_same_pizza():
    pizza1 = Pizza(size='L')
    pizza1.add_ingredient('tomato')
    pizza1.add_ingredient('cheese')
    pizza2 = Pizza(size='L')
    pizza2.add_ingredient('cheese')
    pizza2.add_ingredient('tomato')
    assert pizza1 == pizza2


def test_eq_different_pizza():
    pizza1 = Pizza(size='L')
    pizza1.add_ingredient('tomato')
    pizza1.add_ingredient('cheese')
    pizza2 = Pizza(size='M')
    pizza2.add_ingredient('tomato')
    pizza2.add_ingredient('cheese')
    assert pizza1 != pizza2
