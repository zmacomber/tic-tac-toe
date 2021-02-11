from tictactoe import TicTacToe
from tkinter import Canvas, Tk

tk = Tk()
tk.title("Tic Tac Toe")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=450, height=450, bd=0, highlightthickness=0)
canvas.pack()

TicTacToe(canvas)

