# -*- coding: utf-8 -*-

# quadratic equation
import math


class ANullException(ValueError):
    def __init__(self, msg):
        self.msg = msg


def solve(a: float, b: float, c: float, e: float) -> list:
    if math.fabs(a) < e:
        raise ANullException('Значение a не должно быть равным 0.')

    dtr: float = b*b - 4*a*c
    if dtr < -e:
        # реализация п.3 ДЗ
        return []




if __name__ == '__main__':
    print(solve(0, 23, 44, 1e-7))