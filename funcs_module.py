from math import *


def calculate_expression(expression: str, start: int, end: int, step: int) -> list:
    """
    Обчислює переданий вираз з невідомою змінною x за допомогою табулювання функції на певному проміжку.

    Parameters:
    -----------
        expression (str): вираз

        start (int): початок проміжку табулювання

        end (int): кінець проміжку табулювання

        step (int): крок табулювання

    Returns:
    --------
        list: список обчислених виразів табулюванням функції

    Examples:
    ---------
    >>> 2
    >>> 13
    >>> 2
    >>> fm.calculate_expression(2 * x - 1)
    [3, 7, 11, 15, 19, 23]
    """
    values = []  # Список значень змінної x
    for x in range(start, end + 1, step):
        result = eval(expression)  # Обчислюємо вираз
        values.append(round(result, 3))  # Додаємо результат до списку та округлюємо результат до 3 знаків після коми

    return values


if __name__ == "__main__":
    print("This is my module")
