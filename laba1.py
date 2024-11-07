#9.	Формируется матрица F следующим образом: Скопировать в нее матрицу А и если минимальных чисел в нечетных столбцах в области 2 больше,
# чем количество максимальных чисел в четных строках в области 1,
# то поменять симметрично области 1 и 2 местами, иначе 2 и 3 поменять местами несимметрично.
# При этом матрица А не меняется. После чего вычисляется выражение: A*А+(K*AT).
# Выводятся по мере формирования А, F и все матричные операции последовательно.

import random
N= int(input('N='))
K= int(input('K='))
A=[]
    # инициализация матрицы а


# Выбор типа создания матрицы A
choice = int(input("Выберите способ создания матрицы A (1 - из файла, 2 - случайные числа): "))


if choice == 1:
    with open('laba1.txt', 'r') as file:
        for i in range(N):
            st = file.readline()
            A.append([int(x) for x in st.split()])

    print("Матрица A:")
    for row in A:
        print(row)

elif choice == 2:
    A = [[random.randint(-10, 10) for _ in range(N)] for _ in range(N)]
    print("Матрица A:")
    for row in A:
        print(row)
else:
    print("Некорректный ввод")
    exit()

# Формируем матрицу F
print("\nМатрица F:")
F = [[0] * N for _ in range(N)]
for i in range(N):      # Копируем A в F
    for j in range(N):
        F[i][j] = A[i][j]

print("Матрица F после копирования:")
for row in F:
    print(row)

size = len(F)
max1 = 0
min1 = 11
min_count_area2 = 0
max_count_area1 = 0
d = []
k = []

# Подсчет максимальных значений в первой области
for i in range (N//2):
    for j in range(i):
        if i % 2==0:
            max1 = A[i][j]
            if A[i][j]> max1:
                max1 = A[i][j]
                max_count_area1=1
            elif max1==A[i][j]:
                max_count_area1+=1
for i in range(N//2,N):
    for j in range(N-(i+1)):
        if i % 2==0:
            max1 = A[i][j]
            if A[i][j]> max1:
                max1 = A[i][j]
                max_count_area1=1
            elif max1==A[i][j]:
                max_count_area1+=1
#подсчет минимальных значений второй области
for i in range(N//2):
    for j in range(i+1,N//2):
        if j % 2!=0:
            min1 = A[i][j]
            if A[i][j]< min1:
                min1 = A[i][j]
                min_count_area2=1
            elif min1==A[i][j]:
                min_count_area2+=1
for i in range(N//2):
    for j in range(N//2,N-(i+1)):
        if j % 2!=0:
            min1 = A[i][j]
            if A[i][j]< min1:
                min1 = A[i][j]
                min_count_area2=1
            elif min1==A[i][j]:
                min_count_area2+=1

if min_count_area2 > max_count_area1:
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            F[i][j],F[j][i]=F[j][i],F[i][j]
    for i in range(N // 2):
        for j in range(N // 2, N - (i + 1)):
            F[i][j], F[j][i] = F[j][i], F[i][j]
    print("\nМатрица F после обмена (min_count_area2 > max_count_area1):")
    for row in F:
        print(row)

else:
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            F[i][j], F[j][N-i-1] = F[j][N-i-1], F[i][j]
    for i in range(N // 2):
        for j in range(N // 2, N - (i + 1)):
            F[i][j], F[j][N - i - 1] = F[j][N - i - 1], F[i][j]
    print("\nМатрица F после обмена (min_count_area2 <= max_count_area1):")
    for row in F:
        print(row)

# Умножение A на F
AF = [[0] * N for i in range(N)]
for i in range(N):  # A * F
    for j in range(N):
        for p in range(N):
            AF[i][j] += A[i][p] * F[p][j]


print("\nРезультат A * F:")
for row in AF:
    print(row)

# Транспонирование A
AT = [[0] * N for i in range(N)]
for i in range(N):
    for j in range(N):
        AT[i][j] = A[j][i]

print("\nТранспонированная матрица A (AT):")
for row in AT:
    print(row)

# Умножение AT на K
ATK = [[0] * N for i in range(N)]
for i in range(N):  # AT * K
    for j in range(N):
        ATK[i][j] = AT[i][j] * K

print("\nРезультат AT * K:")
for row in ATK:
    print(row)

# Сложение AF + AT*K
M = [[0] * N for i in range(N)]
for i in range(N):  # AF + ATK
    for j in range(N):
        M[i][j] = AF[i][j] + ATK[i][j]

print("\nРезультат AF + AT*K:")
for row in M:
    print(row)