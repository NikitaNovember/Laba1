# Импортируем модуль re для работы с регулярными выражениями
import re

with open('laba4.txt', 'r') as file:
    for line in file:
        words = line.split()

        # Проходимся по каждому "слову" из строки
        for word in words:
            # Проверяем, является ли объект натуральным числом, содержащим хотя бы один ноль
            if word == "0" or not re.search('0', word):
                print(f"Ошибка: '{word}' не является натуральным числом с нулем.")
            elif re.fullmatch(r'[1-9]\d*0\d*', word):
                # Если найдено подходящее число, выводим его
                print(f"Найдено число: {word}")

                # Считаем количество нулей в числе
                zero_count = word.count('0')
                print(f"Количество нулей: {zero_count}")
