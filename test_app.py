# -*- coding: utf-8 -*-

import pytest
from app import solve, ANullException


@pytest.fixture
def double_zero() -> float:
    """
    фикстура эпсилон, минимального значения, значения меньше которого интерпретируются как 0
    :return:
    """
    yield 1e-7


def test_a_null(double_zero):
    """
    Реализация 9-го пункта ДЗ:
    Написать тест, который проверяет, что коэффициент a не может быть равен 0. В этом случае solve выбрасывает исключение.
    Примечание. Учесть, что a имеет тип double и сравнивать с 0 через == нельзя.
    :param double_zero: фикстура эпсилон
    :return:
    """
    # arrange
    a: float = 0.5e-7
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
    a: float = 5.432
    b: float = 11.22
    c: float = 6.789

    # act
    result = solve(a, b, c, double_zero)

    # assert
    # Проверим, что результат массив ввиду динамической типизации Python
    assert isinstance(result, (list, tuple))
    # Проверка существования двух корней
    assert len(result) == 2
