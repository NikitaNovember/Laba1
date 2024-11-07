import numpy as np
import matplotlib.pyplot as plt


# Функция для заполнения матрицы из файла
def fill_matrix_from_file(filename, N):
    with open(laba1.txt, 'r') as f:
        matrix = []
        for line in f:
            matrix.append(list(map(int, line.split())))
    return np.array(matrix)


# Функция для генерации матрицы
def generate_matrix(N, random_fill=True, filename=None):
    if random_fill:
        return np.random.randint(-10, 11, (N, N))
    else:
        return fill_matrix_from_file(filename, N)


# Функция для симметричной замены элементов матриц
def swap_symmetric(A, B):
    A[:], B[:] = B[::-1, ::-1], A[::-1, ::-1]


# Функция для несимметричной замены элементов матриц
def swap_non_symmetric(A, B):
    A[:], B[:] = B, A


# Функция для создания матрицы F на основе A
def create_F(A, K):
    N = A.shape[0]
    half_N = N // 2

    B = A[:half_N, :half_N]
    C = A[:half_N, half_N:]
    D = A[half_N:, :half_N]
    E = A[half_N:, half_N:]

    # Подсчет строк, состоящих из одних нулей в четных столбцах в B
    zero_rows_in_B = sum(np.all(B[:, 1::2] == 0, axis=1))
    # Сумма положительных элементов в четных строках B
    positive_sum_in_even_rows = sum(np.sum(B[1::2] > 0))

    F = np.copy(A)

    # Замена подматриц в зависимости от условий
    if zero_rows_in_B > positive_sum_in_even_rows:
        swap_symmetric(E, C)
    else:
        swap_non_symmetric(B, E)

    return F


# Функция для вычисления итоговых матриц
def calculate_matrices(A, F, K):
    det_A = np.linalg.det(A)  # Определитель матрицы A
    diag_sum_F = np.trace(F)  # Сумма диагональных элементов матрицы F

    # Выбор выражения для вычисления в зависимости от условия
    if det_A > diag_sum_F:
        A_inv = np.linalg.inv(A)  # Обратная матрица A
        AT = A.T  # Транспонированная матрица A
        F_inv = np.linalg.inv(F)  # Обратная матрица F
        result = A_inv @ AT - K * F_inv
    else:
        AT = A.T
        G = np.tril(A)  # Нижняя треугольная матрица G из A
        FT = F.T  # Транспонированная матрица F
        result = (AT + G - FT) * K

    return result


# Функция для построения графиков матриц
def plot_matrices(A, F, result):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))

    axs[0].imshow(A, cmap='viridis')
    axs[0].set_title('Матрица A')

    axs[1].imshow(F, cmap='viridis')
    axs[1].set_title('Матрица F')

    axs[2].imshow(result, cmap='viridis')
    axs[2].set_title('Итоговая матрица')

    plt.show()


# Главная функция
def main():
    K = int(input("Введите K: "))
    N = int(input("Введите N: "))

    # Измените на False и укажите имя файла для нерегулярного заполнения
    random_fill = True
    filename = "matrix.txt"

    A = generate_matrix(N, random_fill=random_fill, filename=filename)
    print("Матрица A:\n", A)

    F = create_F(A, K)
    print("Матрица F:\n", F)

    result = calculate_matrices(A, F, K)
    print("Итоговая матрица:\n", result)

    plot_matrices(A, F, result)


if __name__ == "__main__":
    main()
