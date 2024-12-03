#Формируется матрица F следующим образом: скопировать в нее А и если в В
#количество строк, состоящих из одних нулей в четных столбцах, чем сумма
#положительных  элементов в четных строках, то поменять местами Е и С симметрично,
#иначе В и Е поменять местами несимметрично. При этом матрица А не меняется.
#После чего если определитель матрицы А больше суммы диагональных элементов
#матрицы F, то вычисляется выражение: A-1*AT – K * F-1, иначе вычисляется выражение
#(AТ +G-FТ)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по
#мере формирования А, F и все матричные операции последовательно


import numpy as np  # Для работы с матрицами
import matplotlib.pyplot as plt  # Для построения графиков

# Ввод чисел K и N
K = int(input("Введите значение K (целое число): "))
N = int(input("Введите размер матрицы N (четное число): "))

half = N // 2

# Создаем пустую матрицу A и заполняем подматрицы
A = np.zeros((N, N), dtype=int)  # Матрица A изначально заполнена нулями
B = np.full((half, half), 1)  # Подматрица B заполнена единицами
C = np.full((half, half), 2)  # Подматрица C заполнена двойками
D = np.full((half, half), 3)  # Подматрица D заполнена тройками
E = np.full((half, half), 4)  # Подматрица E заполнена четверками

# Вставляем подматрицы в A
A[:half, :half] = B  # Верхний левый угол — B
A[half:, :half] = C  # Нижний левый угол — C
A[half:, half:] = D  # Нижний правый угол — D
A[:half, half:] = E  # Верхний правый угол — E

# Показываем матрицу A
print("\nМатрица A:")
print(A)

# Создаем матрицу F как копию A
F = A.copy()

zero_rows = 0
for row in B:
    if all(row[::2] == 0):
        zero_rows += 1


positive_sum = 0
for i in range(0, half, 2):
    for elem in B[i]:
        if elem > 0:
            positive_sum += elem

# Условие для перестановки подматриц
if zero_rows > positive_sum:
    # Симметрично меняем местами E и C
    F[half:, :half], F[:half, half:] = E, C
else:
    # Несимметрично меняем местами B и E
    F[:half, :half], F[:half, half:] = E, B

# Показываем матрицу F
print("\nМатрица F после перестановок:")
print(F)


diag_sum_F = sum(F[i][i] for i in range(N))

# Считаем определитель матрицы A вручную
if N == 2:
    det_A = A[0, 0] * A[1, 1] - A[0, 1] * A[1, 0]
else:
    det_A = round(np.linalg.det(A))


print(f"\nОпределитель матрицы A: {det_A}")
print(f"Сумма диагональных элементов матрицы F: {diag_sum_F}")


if det_A > diag_sum_F:

    A_T = A.T
    F_T = F.T
    result = A_T - K * F_T
else:
    # Выражение: (AТ + G - FТ) * K
    G = np.zeros_like(A)
    for i in range(N):
        for j in range(i + 1):
            G[i, j] = A[i, j]
    A_T = A.T
    F_T = F.T
    result = (A_T + G - F_T) * K

# Показываем результат
print("\nРезультат вычислений:")
print(result)

# Построение графиков
plt.figure(figsize=(12, 4))

# График 1: Тепловая карта матрицы F
plt.subplot(1, 3, 1)
plt.imshow(F, cmap='coolwarm', interpolation='nearest')
plt.title("Тепловая карта матрицы F")
plt.colorbar()

# График 2: Первая строка матрицы F
plt.subplot(1, 3, 2)
plt.plot(F[0], marker='o', label='Первая строка F')
plt.title("Первая строка матрицы F")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()

# График 3: Гистограмма значений F
plt.subplot(1, 3, 3)
plt.hist(F.flatten(), bins=8, color='orange', edgecolor='black')
plt.title("Гистограмма значений F")
plt.xlabel("Значение")
plt.ylabel("Частота")

# Показать графики
plt.tight_layout()
plt.show()

