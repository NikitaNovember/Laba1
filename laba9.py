import tkinter as tk
from tkinter import messagebox


class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики (игра против компьютера)")

        self.current_player = "X"  # Игрок
        self.computer_player = "O"  # Компьютер
        self.board = [""] * 9
        self.buttons = []

        self.start_screen()

    def start_screen(self):
        self.clear_window()
        label = tk.Label(self.root, text="Кто ходит первым?", font=("Arial", 18))
        label.pack(pady=20)

        first_player_frame = tk.Frame(self.root)
        first_player_frame.pack()

        player_btn = tk.Button(first_player_frame, text="Я", command=self.player_starts)
        player_btn.grid(row=0, column=0, padx=10)

        computer_btn = tk.Button(first_player_frame, text="Компьютер", command=self.computer_starts)
        computer_btn.grid(row=0, column=1, padx=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def player_starts(self):
        self.current_player = "X"
        self.computer_player = "O"
        self.start_game()

    def computer_starts(self):
        self.current_player = "O"
        self.computer_player = "X"
        self.start_game()
        self.computer_move()

    def start_game(self):
        self.board = [""] * 9
        self.clear_window()
        self.create_buttons()
        self.reset_button()

    def create_buttons(self):
        # Очистка старых кнопок
        self.buttons = []

        for i in range(9):
            button = tk.Button(self.root, text="", font=("Arial", 24), width=5, height=2,
                               command=lambda i=i: self.on_player_click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def on_player_click(self, index):
        if self.board[index] == "" and self.check_winner() is None:
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            winner = self.check_winner()
            if winner:
                messagebox.showinfo("Игра окончена!", f"Победитель: {winner}")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Игра окончена!", "Ничья!")
                self.reset_game()
            else:
                self.computer_move()

    def computer_move(self):
        best_score = -float('inf')
        best_index = None

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.computer_player
                score = self.minimax(self.board, False)
                self.board[i] = ""

                if score > best_score:
                    best_score = score
                    best_index = i

        self.board[best_index] = self.computer_player
        self.buttons[best_index].config(text=self.computer_player)

        winner = self.check_winner()
        if winner:
            messagebox.showinfo("Игра окончена!", f"Победитель: {winner}")
            self.reset_game()
        elif "" not in self.board:
            messagebox.showinfo("Игра окончена!", "Ничья!")
            self.reset_game()

    def minimax(self, board, is_maximizing):
        winner = self.check_winner()
        if winner == self.computer_player:
            return 1
        elif winner == self.current_player:
            return -1
        elif "" not in board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = self.computer_player
                    score = self.minimax(board, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = self.current_player
                    score = self.minimax(board, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score

    def check_winner(self):
        for i in range(3):
            # вертикали
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":
                return self.board[i * 3]
            # горизонты
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return self.board[i]

        # диагонали
        if self.board[0] == self.board[4] == self.board[8] != "":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != "":
            return self.board[2]

        return None

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.config(text="")
        self.start_screen()

    def reset_button(self):
        reset_btn = tk.Button(self.root, text="Сбросить игру", command=self.reset_game)
        reset_btn.grid(row=3, column=0, columnspan=3)

root = tk.Tk()
game = TicTacToe(root)
root.mainloop()