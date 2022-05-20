from math import sqrt

with open('liczby.txt', 'r', encoding='utf-8') as f:
    data = [int(i) for i in f.read().splitlines()]


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def n_factors(n):
    s = 0
    while n > 1:
        for i in range(2, int(sqrt(n)) + 1):
            if n % i == 0:
                s += 1
                n //= i
                break
        else:
            s += 1
            n = 1
    return s


def n_unique(n):
    s = 0
    for i in range(2, int(sqrt(n) + 1)):
        if is_prime(i) and n % i == 0:
            s += 1
    return s


def zad4_1():
    n = 0
    first = 0
    for i in data:
        l = i % 10
        f = i
        while f >= 10:
            f //= 10
        if f == l:
            n += 1
            if first == 0:
                first = i
    print('Ile liczb:', n)
    print('Pierwsza liczba:', first)


def zad4_2():
    most_factors = 0
    most_factors_n = 0
    most_unique = 0
    most_unique_n = 0
    for i in data:
        factors_n = n_factors(i)
        unique_n = n_unique(i)
        if factors_n > most_factors_n:
            most_factors_n = factors_n
            most_factors = i
        if unique_n > most_unique_n:
            most_unique_n = unique_n
            most_unique = i
    print('Najwięcej czynników:', most_factors, 'liczba:', most_factors_n)
    print('Najwięcej różnych czynników:', most_unique, 'liczba:', most_unique_n)


def zad4_3():
    t = 0
    p = 0
    for x in data:
        for y in data:
            if y % x == 0 and x != y:
                for z in data:
                    if z % y == 0 and len({x, y, z}) == 3:
                        t += 1
                        print(x, y, z)
                        for u in data:
                            if u % z == 0 and len({x, y, z, u}) == 4:
                                for w in data:
                                    if w % u == 0 and len({x, y, z, u, w}) == 5:
                                        p += 1
    print('Liczba trójek:', t)
    print('Liczba piątek:', p)


print('Zad. 4.1.')
zad4_1()

print('\nZad. 4.2.')
zad4_2()

print('\nZad. 4.3.')
zad4_3()
