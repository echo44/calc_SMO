#  здесь представлена реализация математических функций

import math


def fakta(x):
    """Вычисляет факториал"""
    x = int(x)
    f = open("factorialy", "r")
    c = f.readlines()
    if x == 0:
        return 1
    return float(c[x - 1])


def sochetanie(n, k):
    """Вычисляет C из n по k"""
    g = n - k
    return fakta(n) / (fakta(k) * fakta(g))


def funk_mm1(x, ro):
    """Функция для MM1"""
    return (1 - ro) * math.pow(ro, x)


def funk_mminf(x, k_shtrih):
    """Функция для MMINF"""
    return ((math.pow(k_shtrih, x)) / fakta(x)) * (math.pow(math.e,
    (-k_shtrih)))


def funk_mmv1(x, ro, vv):  # j = k-v
    """Функция для MMV до достижения V"""

    def znam():
        """Вычисляет знаменатель для P от K"""
        summ = 0
        r = int(vv)
        for i in range(0, r):
            summ += math.pow(ro, i) / fakta(i)
        return summ + (math.pow(ro, vv) / fakta(vv)) * (vv / (vv - ro))

    return (math.pow(ro, x) / fakta(x)) / (znam())


def funk_mmv2(x, ro, vv):
    """Вычисляет вторую часть форумулы для MMV, после достижения V"""

    def znam():
        """Вычисляет занменатель"""
        znamenatel = 0
        r = int(vv)
        for i in range(0, r):
            znamenatel += math.pow(ro, i) / fakta(i)
        return znamenatel + (math.pow(ro, vv) / fakta(vv)) * (vv / (vv - ro))

    return ((math.pow(ro, vv) / fakta(vv)) * (math.pow((ro / vv),
    (x - vv)))) / znam()


def funk_mmv3(ro, vv):
    """Вычисляет P от t"""

    def znam():
        """Вычисляет занменатель"""
        znamenatel = 0
        r = int(vv)
        for i in range(0, r):
            znamenatel += (math.pow(ro, i) / fakta(i))
        return znamenatel + (math.pow(ro, vv) / fakta(vv)) * (vv / (vv - ro))

    return ((math.pow(ro, vv) / fakta(vv)) * (vv / (vv - ro))) / znam()


def funk_mmvk(x, ro, vv):
    """Функция для MMVK"""

    def znam():
        """Вычисляет знаменатель"""
        znamenatel = 0
        r = int(vv + 1)
        for i in range(0, r):
            znamenatel += (math.pow(ro, i) / fakta(i))
        return znamenatel

    return (math.pow(ro, x) / fakta(x)) / (znam())


def funk_mmvk1(ro, vv):
    """Вычисляет P от t"""

    def znam(vv):
        """Вычисляет занменатель"""
        znamenatel = 0
        r = int(vv)
        for i in range(0, r):
            znamenatel += (math.pow(ro, r) / fakta(i))
        return znamenatel

    return (math.pow(ro, vv) / fakta(vv)) / znam(vv)


def funk_mmvkn1(x, vv, aa, nn):
    """Вычисляет P от k"""

    def znam():
        """Вычисляет знаменатель"""
        znamenatel = 0
        r = int(vv + 1)
        for i in range(0, r):
            znamenatel += sochetanie(nn, i) * (math.pow((aa / (1 - aa)), i))
        return znamenatel

    return (sochetanie(nn, x) * math.pow((aa / (1 - aa)), x)) / znam()


def funk_mmvkn2(vv, aa, nn):
    """Вычисляет P от t"""

    def znam():
        """Вычисляет знаменатель"""
        znamenatel = 0
        r = int(vv + 1)
        for i in range(0, r):
            znamenatel += sochetanie(nn, i) * (math.pow((aa / (1 - aa)), i))
        return znamenatel

    return (sochetanie(nn, vv) * math.pow((aa / (1 - aa)), vv)) / znam()


def funk_mmvkn3(vv, aa, nn):
    """Вычисляет P от b"""

    def znam():
        """Вычисляет знаменатель"""
        znamenatel = 0
        r = int(vv + 1)
        for i in range(0, r):
            znamenatel += sochetanie(nn - 1, i) * (math.pow((aa / (1 - aa)), i))
        return znamenatel

    return (sochetanie(nn - 1, vv) * math.pow((aa / (1 - aa)), vv)) / znam()
