# Write functions to estimate the functions.

import math


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def sin(x, n):
    result = 0
    for i in range(n):
        tinh_toan = ((-1)**i) * (x**(2*i + 1)) / factorial(2*i + 1)
        result += tinh_toan
    return result


def cos(x, n):
    result = 0
    for i in range(n):
        tinh_toan = ((-1)**i) * (x**(2*i)) / factorial(2*i)
        result += tinh_toan
    return result


def sinh(x, n):
    result = 0
    for i in range(n):
        tinh_toan = (x**(2*i + 1)) / factorial(2*i + 1)
        result += tinh_toan
    return result


def cosh(x, n):
    result = 0
    for i in range(n):
        tinh_toan = (x**(2*i)) / factorial(2*i)
        result += tinh_toan
    return result


# INPUT
x = 3.14
n = 10

print(f"sin({x}, {n}) = {sin(x, n)}")
print(f"cos({x}, {n}) = {cos(x, n)}")
print(f"sinh({x}, {n}) = {sinh(x, n)}")
print(f"cosh({x}, {n}) = {cosh(x, n)}")
