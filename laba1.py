import random
N= int(input())
K= int(input())
a=[]
    # инициализация матрицы а
file = open('laba1.txt', 'r')
for i in range(N):
    st = file.readline()
    a.append([int(x) for x in st.split()])
print("A")
for i in a:
    print(i)
a= [[random.randint(-10,10) for i in range(N)] for j in range(N)]
for i in a:
    print(i)
f= []
import random

# Выбор типа создания матрицы A
choice = int(input("Выберите способ создания матрицы A (1 - из файла, 2 - случайные числа): "))
n = int(input("Введите размерность матрицы (n): "))
A = []

if choice == 1:
    with open('laba1.txt', 'r') as file:
        for i in range(n):
            st = file.readline()
            A.append([int(x) for x in st.split()])

    print("Матрица A:")
    for row in A:
        print(row)

elif choice == 2:
    A = [[random.randint(-10, 10) for _ in range(n)] for _ in range(n)]
    print("Матрица A:")
    for row in A:
        print(row)
else:
    print("Некорректный ввод")
    exit()

# Формируем матрицу F
print("\nМатрица F:")
F = [[0] * n for _ in range(n)]
for i in range(n):      # Копируем A в F
    for j in range(n):
        F[i][j] = A[i][j]

print("Матрица F после копирования:")
for row in F:
    print(row)

size = len(F)
min_count_area2 = 0
max_count_area1 = 0
d = []
k = []

# Подсчет минимальных и максимальных значений
for i in range(n):
    for j in range(n):
        if j % 2 != 0:  # Нечетные столбцы (область 2)
            if i > j and i + j > size - 1:
                if F[i][j] == 0:
                    min_count_area2 += 1
        elif j % 2 == 0:  # Четные столбцы (область 1)
            if i > j and i + j < size - 1:
                max_count_area1 += F[i][j]

# Логика обмена областей
t = 0
y = 0

if min_count_area2 > max_count_area1:
    # Обмен областей 1 и 2
    for i in range(n):
        for j in range(n):
            if i < j and i + j < size - 1:
                d.append(F[i][j])
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if i > j and i + j < size - 1:
                k.append(F[i][j])
    for i in range(n):
        for j in range(n):
            if i < j and i + j < size - 1:
                F[i][j] = k[t]
                t += 1
    for j in range(n):
        for i in range(n - 1, -1, -1):
            if i > j and i + j < size - 1:
                F[i][j] = d[y]
                y += 1
    print("\nМатрица F после обмена (min_count_area2 > max_count_area1):")
    for row in F:
        print(row)

else:
    # Обмен областей 2 и 3
    for i in range(n):
        for j in range(n):
            if i < j and i + j < size - 1:
                d.append(F[i][j])
    for j in range(n - 1, -1, -1):
        for i in range(n):
            if i < j and i + j > size - 1:
                k.append(F[i][j])
    for i in range(n):
        for j in range(n - 1, -1, -1):
            if i < j and i + j < size - 1:
                F[i][j] = k[t]
                t += 1
    for j in range(n - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            if i < j and i + j > size - 1:
                F[i][j] = d[y]
                y += 1

    print("\nМатрица F после обмена (min_count_area2 <= max_count_area1):")
    for row in F:
        print(row)

# Умножение A на F
C = [[0] * n for i in range(n)]
for i in range(n):  # A * F
    for j in range(n):
        s = 0
        for p in range(n):
            s += A[i][p] * F[p][j]
        C[i][j] = s

print("\nРезультат A * F:")
for row in C:
    print(row)

K = 2  # Значение K, которое можно настроить
for i in range(n):  # K * C
    for j in range(n):
        C[i][j] *= K

print("\nРезультат K * C:")
for row in C:
    print(row)

# Транспонирование A
AT = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        AT[i][j] = A[j][i]

print("\nТранспонированная матрица A (AT):")
for row in AT:
    print(row)

# Умножение AT на K
ATK = [[0] * n for i in range(n)]
for i in range(n):  # AT * K
    for j in range(n):
        ATK[i][j] = AT[i][j] * K

print("\nРезультат AT * K:")
for row in ATK:
    print(row)

# Вычитание C - AT*K
M = [[0] * n for i in range(n)]
for i in range(n):  # C - ATK
    for j in range(n):
        M[i][j] = C[i][j] - ATK[i][j]

print("\nРезультат C - AT*K:")
for row in M:
    print(row)