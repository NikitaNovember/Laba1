'''Задана рекуррентная функция. Область определения функции – натуральные числа. Написать
программу сравнительного вычисления данной функции рекурсивно и итерационно. Определить границы
применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования
времени вычисления представить в табличной форме. Обязательное требование – минимизация времени
выполнения и объема памяти.
9 вариант. F(1) = 1,F(n) = (-1)^n * (F(n–1) + (n+1)!/(2n)!), при n > 1'''
from math import factorial
import timeit
fact1, fact2 = 2, 2 #начальные значения для (n+1)! и (2n)!, когда n=1
n=input('Введите натуральное число n > 1 и n < 996: ')
while True:
    try: n = int(n)
    except: n = input('Вы неправильно ввели n. Введите натуральное число n > 1 и n < 996: ')
    else:
        if n>1 and n<996: break #если ввести больше 996 рекурсия не вывезет
        else: n = input('Вы неправильно ввели n. Введите натуральное число n > 1 и n < 996: ')
def st1(n):
    if n%2==0: return 1
    else: return -1
def recursive_f(n):
    if n == 1: return 1
    else: return st1(n) * (recursive_f(n-1) + factorial(n+1) / factorial(2*n))
def iterative_f(n, fact1,fact2):
    f=1
    for i in range(2,n+1):
        fact1 *=(i+1)
        fact2 *= (i*2) * ((i*2)-1)
        f = st1(i) * (f + fact1/fact2)
    return f
def compare_methods(n):
    print(f"n: {n}")
    a = timeit.timeit('recursive_f(n)', globals = globals(), number =1)
    print(f'Рекурсивный результат: {recursive_f(n)} \nВремя рекурсивного вычисления: {a}')
    a = timeit.timeit('iterative_f(n, fact1, fact2)', globals = globals(), number =1)
    print(f'Итерационный результат: {iterative_f(n, fact1,fact2)} \nВремя итерационного вычисления: {a}')
compare_methods(n)