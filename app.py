# -*- coding: utf-8 -*-

# quadratic equation
import math


class ANullException(ValueError):
    def __init__(self, msg):
        self.msg = msg


def solve(a: float, b: float, c: float, e: float) -> list:
    x1 = x2 = 0.0 # инициализация корней
    if math.fabs(a) < e:
        raise ANullException('Значение a не должно быть равным 0.')

    dtr: float = b*b - 4*a*c
    # реализация п.4. Детерминант отрицательный - действительных корней нет
    if dtr < -e:
        #
        return []
    # реализация п.6. Детерминант положительный - два действительных корня
    if dtr > e:
        x1 = (- b - math.sqrt(dtr)) / 2*c
        x2 = (- b + math.sqrt(dtr)) / 2*c
    # реализация п.8
    if math.fabs(dtr) < e:
        x1 = x2 = - (b / 2) / a

    return [x1, x2]



if __name__ == '__main__':
    print(solve(0, 23, 44, 1e-7))