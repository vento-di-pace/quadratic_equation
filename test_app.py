# -*- coding: utf-8 -*-

import pytest
from app import solve, ANullException


@pytest.fixture
def double_zero() -> float:
    yield 1e-7


def test_a_null(double_zero):
    # arrange
    a: float = 0.5e-7
    b: float = 12
    c: float = 33

    # act and assert
    with pytest.raises(ANullException) as e_info:
        result = solve(a, b, c, double_zero)
    assert e_info.value.msg == 'Значение a не должно быть равным 0.'


def test_no_squares(double_zero):

    # arrange
    a: float = 2.0
    b: float = 3
    c: float = 3.0

    # act
    result = solve(a, b, c, double_zero)

    # assert
    assert result == []
