from typing import List, Tuple
import pytest


def fit_transform(*args: str) -> List[Tuple[str, List[int]]]:
    """
    fit_transform(iterable)
    fit_transform(arg1, arg2, *args)
    """
    if len(args) == 0:
        raise TypeError('expected at least 1 arguments, got 0')

    categories = args if isinstance(args[0], str) else list(args[0])
    uniq_categories = set(categories)
    bin_format = f'{{0:0{len(uniq_categories)}b}}'

    seen_categories = dict()
    transformed_rows = []

    for cat in categories:
        bin_view_cat = (int(b) for b in
                        bin_format.format(1 << len(seen_categories)))
        seen_categories.setdefault(cat, list(bin_view_cat))
        transformed_rows.append((cat, seen_categories[cat]))

    return transformed_rows


def test_fit_transform_one_word():
    """
        Тестируем, что функция корректно кодирует одну строку
    """
    input_data = 'nuggets'
    expected_result = [('nuggets', [1])]
    result = fit_transform(input_data)
    assert result == expected_result

def test_fit_transform_list_of_words():
    """
        Тестируем, что функция корректно кодирует список строк
    """
    input_data = ['clippers', 'nicks', 'lakers', 'bulls']
    expected_result = [
        ('clippers', [0, 0, 0, 1]),
        ('nicks', [0, 0, 1, 0]),
        ('lakers', [0, 1, 0, 0]),
        ('bulls', [1, 0, 0, 0])
    ]
    result = fit_transform(*input_data)
    assert result == expected_result

def test_fit_transform_missed_word():
    """
        Тестируем, что функция правильно обрабатывает пустые строки
    """
    input_data = ['lebron', '', 'james']
    expected_result = [('lebron', [0, 0, 1]), ('', [0, 1, 0]),
                       ('james', [1, 0, 0])]
    result = fit_transform(*input_data)
    assert result == expected_result

def test_fit_transform_no_arguments():
    """
        Тестируем, что функция вызывает исключение при отсутствии аргументов

    """
    with pytest.raises(TypeError):
        fit_transform()

def test_fit_transform_assertNotIn():
    """
        Тестируем, что функция правильно обрабатывает отсутствующие категории
    """
    input_data = ['curry', 'durant', 'irving']
    result = fit_transform(*input_data)
    for category, _ in result:
        assert category not in ['kareem', 'iverson']

if __name__ == '__main__':
    pytest.main()
