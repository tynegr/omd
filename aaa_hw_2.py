import csv
from typing import List, Dict, Any
CSV_FILE_PATH = '/Users/egortishchenko/Downloads/Corp_Summary (1).csv'


def open_file_and_prepare(path: str) -> List[Dict[str, Any]]:
    """
    Открывает CSV-файл и готовит данные для обработки.

    Args:
        path (str): Путь к CSV-файлу.

    Returns:
        List[Dict[str, Any]]: Список словарей с данными из файла.
    """
    result = []
    with open(path, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile, delimiter=';')
        for row in csvreader:
            result.append(row)
    return result


def department_report(data: List[Dict[str, Any]]) -> None:
    """
    Выводит иерархию команд.


    Args:

    data - List[Dict[str, Any]]: Список словарей с данными из файла


    Returns:
        None
    """
    dep_team = {}
    for i in data:
        dep = i['Департамент']
        team = i['Отдел']
        if dep in dep_team:
            dep_team[dep].add(team)
        else:
            dep_team[dep] = set()
            dep_team[dep].add(team)
    for key, val in dep_team.items():
        print(f'{key}: {", ".join(val)}')


def pivot_report(data) -> List[List[str]]:
    """
    Создает сводный отчет по департаментам.

    Returns:
        List[List[str]]: Сводный отчет в виде списка списков.
    """
    dep_salary = {}
    report = []
    for i in data:
        dep = i['Департамент']
        salary = int(i['Оклад'])
        if dep in dep_salary:
            dep_salary[dep].append(salary)
        else:
            dep_salary[dep] = []
            dep_salary[dep].append(salary)
    max_salary = {}
    min_salary = {}
    mean_salary = {}

    for key in dep_salary:
        max_salary[key] = max(dep_salary[key])
        min_salary[key] = min(dep_salary[key])
        mean_salary[key] = sum(dep_salary[key]) / len(dep_salary[key])
        dep_name = f'{key}'
        dep_length = f'{len(dep_salary[key])}'
        dep_vilka = f'{min_salary[key]} - {max_salary[key]}'
        dep_mean_salary = f'{int(mean_salary[key])}'
        report.append([dep_name, dep_length, dep_vilka, dep_mean_salary])
    report.insert(0, ['Имя департамента', 'Численность департамента',
                      'Вилка', 'Средняя зарплата'])
    return report


def print_pivot_report(data: List[Dict[str, Any]]) -> None:
    """
    Выводит сводный отчет на экран.

    Args:

    data - List[Dict[str, Any]]: Список словарей с данными из файла

    Returns:
        None
    """
    report = pivot_report(data)
    max_widths = []
    for column in zip(*report):
        max_column_width = 0
        for element in column:
            element_str = str(element)
            element_width = len(element_str)
            if element_width > max_column_width:
                max_column_width = element_width
        max_widths.append(max_column_width)

    for row in report:
        row_str = ''
        for ind, item in enumerate(row):
            row_str += str(item).ljust(max_widths[ind] + 2) + '| '
        print(row_str.rstrip('| '))


def save_pivot_report(name: str, data: List[Dict[str, Any]]) -> None:
    """
    Сохраняет сводный отчет в виде CSV-файла.

    Args:

    name (str): Название файла.
    data - List[Dict[str, Any]]: Список словарей с данными из файла

    Returns:
        None
    """
    with open(f'{name}.csv', 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        file = pivot_report(data)
        csv_writer.writerows(file)


def menu() -> None:
    """
    Основное меню для выбора задач.

    Returns:
        None
    """
    data = open_file_and_prepare(CSV_FILE_PATH)
    while True:
        print('Выберите задачу - 1, 2 или 3, или введите "q" для выхода:')
        print('1 - Вывести в понятном виде иерархию команд')
        print('2 - Вывести сводный отчёт по департаментам')
        print('3 - Сохранить сводный отчёт  в виде csv-файла')
        answer = input()

        if answer == 'q':
            print('Конец программы')
            break  # Выход из цикла при вводе "q"

        if answer == '1':
            department_report(data)
        elif answer == '2':
            print_pivot_report(data)
        elif answer == '3':
            print('Введите название файла:')
            filename = input()
            save_pivot_report(filename, data)
            print('Загрузка успешно завершена')


if __name__ == "__main__":
    menu()
