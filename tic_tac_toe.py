import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Крестики-нолики")

        self.board = [" "] * 9
        self.current_player = "X"
        self.buttons = []

        for i in range(9):
            button = tk.Button(
                master,
                text=" ",
                font=("Arial", 60),
                width=3,
                height=1,
                command=lambda i=i: self.button_click(i),
            )
            button.grid(row=i // 3, column=i % 3)
            self.buttons.append(button)

    def check_win(self, player):
        """Проверяет, выиграл ли игрок."""
        for i in range(3):
            if self.board[i*3] == self.board[i*3 + 1] == self.board[i*3 + 2] == player:
                return True
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] == player:
                return True
        if self.board[0] == self.board[4] == self.board[8] == player:
            return True
        if self.board[2] == self.board[4] == self.board[6] == player:
            return True
        return False

    def check_draw(self):
        """Проверяет, есть ли ничья."""
        return " " not in self.board

    def button_click(self, index):
        """Обрабатывает нажатие кнопки."""
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)

            if self.check_win(self.current_player):
                messagebox.showinfo("Игра окончена", f"Игрок {self.current_player} победил!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Игра окончена", "Ничья!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        """Сбрасывает игру."""
        self.board = [" "] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text=" ")


if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
