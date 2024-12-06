'''Задание состоит из двух частей.
1 часть – написать программу в соответствии со своим вариантом задания. Написать 2 варианта
формирования (алгоритмический и с помощью функций Питона), сравнив по времени их выполнение.
2 часть – усложнить написанную программу, введя по своему усмотрению в условие минимум одно
ограничение на характеристики объектов (которое будет сокращать количество переборов) и целевую
функцию для нахождения оптимального  решения.
Вариант 9. Вывести все натуральные числа до n, в записи которых встречается не более 2 четных
цифр.'''
import timeit
import re

d = {
    '0': 0,
    '2': 0,
    '4': 0,
    '6': 0,
    '8': 0
}


def alg(n):
    a = []
    for number in range(1, n):
        count_ch = 0
        for el in str(number):
            if count_ch > 2: break
            if int(el) % 2 == 0: count_ch += 1
        if count_ch < 3: a.append(number)

    return a


def func(n):
    a = [str(ch) for ch in range(1, n)]
    matches = []
    for number in a:
        for el in number:
            if el in d.keys(): d[el] += 1
        if sum(d.values()) < 3: matches.append(int(number))
        for keys in d.keys(): d[keys] = 0
    return matches


def target(n):
    msumm = 0
    chislo = 0
    a = [str(ch) for ch in range(1, n)]
    matches = []
    for number in a:
        tsumm = 0
        for el in number:
            tsumm += int(el)
            if el in d.keys(): d[el] += 1
        if sum(d.values()) < 3:
            if msumm < tsumm:
                msumm = tsumm
                chislo = number
            matches.append(int(number))
        for keys in d.keys(): d[keys] = 0

    print(f"Наибольшая сумма цифр в выведенных числах находится в наибольшем числе {chislo}: {msumm}")
    return matches


n = input('Введите целое число n: ')
while True:
    if n.isnumeric():
        n = int(n)
        if n > 0:
            break
        else:
            n = input('Вы ввели некорректное число n. Введите целое число n: ')
    else:
        n = input('Вы ввели некорректное число n. Введите целое число n: ')
while True:
    choice = input(
        '\nВыберите, какую часть программы вы хотите выполнить: \n"1" - 1 часть\n"2" - 2 часть\nИли же вы можете завершить программу, введя с клавиатуры "3":\n')
    try:
        choice = int(choice)
    except:
        choice = input(
            'Вы ввели некорректные данные. Выберите, какую часть программы вы хотите выполнить: \n1 - 1 часть\n2 - 2 часть\nИли же вы можете завершить программу, введя с клавиатуры "3":\n')
    else:
        if choice == 1:
            print(f'n: {n}\n')
            print(alg(n))
            alg_time = timeit.timeit('alg(n)', globals=globals(), number=1)
            print(f'Время выполнение алгоритмическим способом формирования: {alg_time}')
            print()
            print(func(n))
            func_time = timeit.timeit('func(n)', globals=globals(), number=1)
            print(f'Время выполнение функциональным способом формирования: {func_time}')
        elif choice == 2:
            print(f'n: {n}\n')
            print(target(n))
            target_time = timeit.timeit('target(n)', globals=globals(), number=1)
            print(f'Время выполнение программы: {target_time}')
        elif choice == 3:
            break
        else:
            print('Вы ввели некорректные данные.', end=' ')