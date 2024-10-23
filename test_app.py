# -*- coding: utf-8 -*-

import pytest
from app import solve, ANullException
from sys import float_info


@pytest.fixture
def double_zero() -> float:
    """
    Фикстура эпсилон, минимального значения, значения меньше которого интерпретируются как 0
    :return:
    """
    #yield 1e-7
    yield float_info.epsilon


def test_a_null(double_zero):
    """
    Реализация 9-го пункта ДЗ:
    Написать тест, который проверяет, что коэффициент a не может быть равен 0. В этом случае solve выбрасывает исключение.
    Примечание. Учесть, что a имеет тип double и сравнивать с 0 через == нельзя.
    :param double_zero: фикстура эпсилон
    :return:
    """
    # arrange
    a: float = 0.5e-16
    b: float = 12
    c: float = 33

    # act and assert
    with pytest.raises(ANullException) as e_info:
        result = solve(a, b, c, double_zero)
    assert e_info.value.msg == 'Значение a не должно быть равным 0.'


def test_no_squares(double_zero):
    """
    Реализация 3-го пункта ДЗ
    Написать тест, который проверяет, что для уравнения x^2+1 = 0 корней нет (возвращается пустой массив)
    :param double_zero: - фикстура эпсилон
    :return: Логический результат тестирования
    """
    # arrange
    a: float = 2.0
    b: float = 3
    c: float = 3.0

    # act
    result = solve(a, b, c, double_zero)

    # assert
    assert result == []


def test_two_squares(double_zero):
    """
    Реализация 5-го пункта ДЗ:
    Написать тест, который проверяет, что для уравнения x^2-1 = 0 есть два корня кратности 1 (x1=1, x2=-1)
    :param double_zero: фикстура эпсилон
    :return:
    """
    # arrange
    a: float = 4.321
    b: float = 11.22
    c: float = 5.6789112123213

    # act
    result = solve(a, b, c, double_zero)

    # assert
    # Проверим, что результат массив ввиду динамической типизации Python
    assert isinstance(result, (list, tuple))
    # Проверка существования разных двух корней
    assert len(result) == 2 and result[0] != result[1]


def test_one_square(double_zero):
    """
    Реализация 7-го пункта ДЗ:
    Написать тест, который проверяет, что для уравнения x^2+2x+1 = 0 есть один корень кратности 2 (x1= x2 = -1).
    :param double_zero: фикстура эпсилон
    :return:
    """
    # arrange
    a: float = 5670.7
    b: float = 33242.12
    c: float = 48717.0253273141005

    # act
    result = solve(a, b, c, double_zero)

    # Проверим, что результат массив ввиду динамической типизации Python
    assert isinstance(result, (list, tuple))

    # Проверка существования одного корня, записанного в массив из двух элементов
    # для сохранения типа вывода функции
    assert len(result) == 2 and result[0] == result[1]


def test_one_square_border_case(double_zero):
    """
    Реализация 11-го пункта ДЗ:
    Написать тест, который проверяет, что для уравнения x^2+2x+1 = 0 есть один корень кратности 2 (x1= x2 = -1).
    :return:
    """
    # arrange
    a: float = 56.7070000000000028
    b: float = 3.24212000000000001
    c: float = 0.046340584471052981
    # слегка увеличенное значение эпсилон
    e: float = 1e-14

    # act
    result = solve(a, b, c, e)

    # Проверим, что результат массив ввиду динамической типизации Python
    assert isinstance(result, (list, tuple))

    # Проверка существования одного корня, записанного в массив из двух элементов
    # для сохранения типа вывода функции
    assert len(result) == 2 and result[0] == result[1]