from math import *


def calculate_expression(expression: str, start: float, end: float, step: int) -> list:
    """
    Обчислює переданий вираз з невідомою змінною x за допомогою табулювання функції на певному проміжку.

    Parameters:
    -----------
        expression (str): вираз

        start (float): початок проміжку табулювання

        end (float): кінець проміжку табулювання

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
    x = start  # Присвоєння змінній x початкового значення
    while x <= end:
        result = eval(expression)  # Обчислюємо вираз
        values.append(round(result, 3))  # Додаємо результат до списку та округлюємо результат до 3 знаків після коми
        x += step

    return values


if __name__ == "__main__":
    print("This is my module")
