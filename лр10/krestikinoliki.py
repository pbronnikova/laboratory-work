import random
import tkinter as tk
from tkinter import messagebox


class TicTacToe:

    def __init__(self, root):
        self.root = root
        self.root.title("Крестики-Нолики (Лабораторная №10)")
        self.root.geometry("330x380")
        self.root.resizable(False, False)

        self.human = "X"
        self.ai = "O"
        self.board = [""] * 9
        self.buttons = []
        self.game_over = False

        self.create_widgets()

    def create_widgets(self):
        # Панель статуса
        self.status_label = tk.Label(
            self.root, text="Ваш ход (X)", font=("Arial", 12, "bold")
        )
        self.status_label.pack(pady=10)

        # Игровое поле (сетка 3х3)
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            row = i // 3
            col = i % 3
            btn = tk.Button(
                frame,
                text="",
                font=("Arial", 20, "bold"),
                width=5,
                height=2,
                command=lambda idx=i: self.human_move(idx),
            )
            btn.grid(row=row, column=col, padx=2, pady=2)
            self.buttons.append(btn)

        # Кнопка «Новая игра»
        reset_btn = tk.Button(
            self.root,
            text="Новая игра",
            font=("Arial", 10),
            command=self.reset_game,
        )
        reset_btn.pack(pady=10)

    def human_move(self, index):
        if self.board[index] == "" and not self.game_over:
            # Ход игрока
            self.make_move(index, self.human)

            if self.check_winner(self.human):
                self.end_game("Вы победили!")
                return
            elif "" not in self.board:
                self.end_game("Ничья!")
                return

            # Ход компьютера
            self.status_label.config(text="Ход компьютера (O)...")
            self.root.update()
            self.ai_move()

    def ai_move(self):
        if self.game_over:
            return

        best_move = None

        # 1. Атака: ищем ход для победы ПК
        best_move = self.find_winning_move(self.ai)

        # 2. Защита: если победить нельзя, блокируем победу игрока
        if best_move is None:
            best_move = self.find_winning_move(self.human)

        # 3. Защита от вилки по противоположным углам
        if best_move is None and self.board[4] == self.ai:
            if (
                self.board[0] == self.human and self.board[8] == self.human
            ) or (self.board[2] == self.human and self.board[6] == self.human):
                sides = [1, 3, 5, 7]
                free_sides = [i for i in sides if self.board[i] == ""]
                if free_sides:
                    best_move = random.choice(free_sides)

        # 4. Занимаем центр (самая выгодная позиция)
        if best_move is None and self.board[4] == "":
            best_move = 4

        # 5. Занимаем углы
        if best_move is None:
            corners = [0, 2, 6, 8]
            free_corners = [i for i in corners if self.board[i] == ""]
            if free_corners:
                best_move = random.choice(free_corners)

        # 6. Занимаем оставшиеся ребра
        if best_move is None:
            free_cells = [i for i in range(9) if self.board[i] == ""]
            if free_cells:
                best_move = random.choice(free_cells)

        # Выполняем выбранный ход
        if best_move is not None:
            self.make_move(best_move, self.ai)

        # Проверка состояния игры
        if self.check_winner(self.ai):
            self.end_game("Вы проиграли! Компьютер победил.")
        elif "" not in self.board:
            self.end_game("Ничья!")
        else:
            self.status_label.config(text="Ваш ход (X)")

    def make_move(self, index, char):
        self.board[index] = char
        color = "blue" if char == "X" else "red"
        self.buttons[index].config(text=char, fg=color)
    def find_winning_move(self, char):
        win_combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],  # Горизонтали
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],  # Вертикали
            [0, 4, 8],
            [2, 4, 6],  # Диагонали
        ]
        for combo in win_combos:
            values = [self.board[i] for i in combo]
            # Если 2 клетки заняты нужным символом и 1 клетка пустая
            if values.count(char) == 2 and values.count("") == 1:
                return combo[values.index("")]
        return None

    def check_winner(self, char):
        win_combos = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for combo in win_combos:
            if (
                self.board[combo[0]] == char
                and self.board[combo[1]] == char
                and self.board[combo[2]] == char
            ):
                return True
        return False

    def end_game(self, message):
        self.game_over = True
        self.status_label.config(text="Игра окончена")
        messagebox.showinfo("Результат", message)

    def reset_game(self):
        self.board = [""] * 9
        self.game_over = False
        self.status_label.config(text="Ваш ход (X)")
        for btn in self.buttons:
            btn.config(text="", fg="black")

if __name__ == "__main__":
    root = tk.Tk()
    app = TicTacToe(root)
    root.mainloop()

