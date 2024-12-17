#Объекты – банковские вклады
#Функции:	сегментация полного списка вкладов по видам
#визуализация предыдущей функции в форме круговой диаграммы
#сегментация полного списка вкладов по типам (мелкие, средние, крупные)
#визуализация предыдущей функции в форме круговой диаграммы


from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

# Настройка шрифта для поддержки кириллицы и корректного отображения знаков
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['font.size'] = 10  # Размер шрифта для улучшения читаемости

class Deposit:
    def __init__(self, amount, deposit_type, deposit_name):
        self.amount = float(amount)
        self.deposit_type = deposit_type
        self.deposit_name = deposit_name

    @staticmethod
    def segment_by_type(deposits):
        types_count = {}
        for dep in deposits:
            print(f"Обрабатывается вклад: {dep.deposit_type} (Сумма: {dep.amount})")  # Отладочная печать
            if dep.deposit_type not in types_count:
                types_count[dep.deposit_type] = 0
            types_count[dep.deposit_type] += 1
        print("Результат сегментации по видам:", types_count)  # Отладочная печать
        return types_count

    @staticmethod
    def segment_by_amount(deposits):
        small = [dep for dep in deposits if dep.amount < 10000]
        medium = [dep for dep in deposits if 10000 <= dep.amount < 50000]
        large = [dep for dep in deposits if dep.amount >= 50000]

        # Отладочная печать для проверки
        print(f"Мелкие вклады (< 10,000): {[dep.amount for dep in small]}")
        print(f"Средние вклады (10,000–50,000): {[dep.amount for dep in medium]}")
        print(f"Крупные вклады (>= 50,000): {[dep.amount for dep in large]}")

        return len(small), len(medium), len(large)

    @staticmethod
    def read_from_file(file_path):
        deposits = []
        try:
            with open(file_path, 'r', encoding='utf-8') as file:  # Открытие файла в кодировке UTF-8
                for line in file:
                    print(f"Читаем строку: {line.strip()}")  # Отладочная печать
                    parts = line.strip().split(',')
                    if len(parts) != 3:
                        raise ValueError(f"Invalid line format: {line}. Must be: amount,deposit_type,deposit_name")
                    amount, deposit_type, deposit_name = parts
                    deposits.append(Deposit(amount, deposit_type, deposit_name))
        except Exception as e:
            messagebox.showerror("Error", f"Failed to read file: {str(e)}")
        return deposits

    @staticmethod
    def plot_pie_chart(data, title):
        labels = data.keys()
        sizes = data.values()
        plt.figure(figsize=(6, 6))
        plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(title, fontname='DejaVu Sans', fontsize=12)
        plt.show()

class DepositApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Банковские вклады")

        self.deposits = []

        self.load_button = Button(root, text="Загрузить данные", command=self.load_data)
        self.load_button.pack(pady=10)

        self.segment_type_button = Button(root, text="Сегментация по видам", command=self.segment_by_type)
        self.segment_type_button.pack(pady=10)

        self.segment_amount_button = Button(root, text="Сегментация по суммам", command=self.segment_by_amount)
        self.segment_amount_button.pack(pady=10)

    def load_data(self):
        self.deposits = Deposit.read_from_file('laba8.txt')
        if self.deposits:
            print("Загруженные данные:")
            for dep in self.deposits:
                print(f"Сумма: {dep.amount}, Тип: {dep.deposit_type}, Название: {dep.deposit_name}")
            messagebox.showinfo("Информация", f"Загружено {len(self.deposits)} вкладов.")

    def segment_by_type(self):
        if not self.deposits:
            messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
            return
        type_data = Deposit.segment_by_type(self.deposits)
        print("Данные для графика (виды вкладов):", type_data)  # Отладка
        Deposit.plot_pie_chart(type_data, "Сегментация по видам вкладов")

    def segment_by_amount(self):
        if not self.deposits:
            messagebox.showwarning("Предупреждение", "Сначала загрузите данные.")
            return
        small_count, medium_count, large_count = Deposit.segment_by_amount(self.deposits)
        amount_data = {'Мелкие': small_count, 'Средние': medium_count, 'Крупные': large_count}
        print("Данные для графика (суммы вкладов):", amount_data)  # Отладка
        Deposit.plot_pie_chart(amount_data, "Сегментация по суммам вкладов")


if __name__ == "__main__":
    root = Tk()
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2 - 250
    h = h // 2 - 150
    root.geometry(f'500x300+{w}+{h}')
    root.resizable(width=False, height=False)
    app = DepositApp(root)
    root.mainloop()
