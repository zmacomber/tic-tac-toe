from computer import Computer
from tkinter  import messagebox

class TicTacToe:
   
    SQUARE_COORDINATES = [
        { "bottom_right_corner_x" : 150, "bottom_right_corner_y" : 150, "letter_x" : 70,  "letter_y" : 70  },
        { "bottom_right_corner_x" : 300, "bottom_right_corner_y" : 150, "letter_x" : 225, "letter_y" : 70  },
        { "bottom_right_corner_x" : 450, "bottom_right_corner_y" : 150, "letter_x" : 370, "letter_y" : 70  },
        { "bottom_right_corner_x" : 150, "bottom_right_corner_y" : 300, "letter_x" : 70,  "letter_y" : 225 },
        { "bottom_right_corner_x" : 300, "bottom_right_corner_y" : 300, "letter_x" : 225, "letter_y" : 225 },
        { "bottom_right_corner_x" : 450, "bottom_right_corner_y" : 300, "letter_x" : 370, "letter_y" : 225 },
        { "bottom_right_corner_x" : 150, "bottom_right_corner_y" : 450, "letter_x" : 70,  "letter_y" : 370 },
        { "bottom_right_corner_x" : 300, "bottom_right_corner_y" : 450, "letter_x" : 225, "letter_y" : 370 },
        { "bottom_right_corner_x" : 450, "bottom_right_corner_y" : 450, "letter_x" : 370, "letter_y" : 370 }
    ]

    WINNING_COMBOS = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]

    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind_all('<Button-1>', self.mouse_clicked)
        self.reset()

    def all_squares_have_letters(self):
        for square in self.squares:
            if square == None:
                return False

        return True

    def determine_letter_to_draw(self):
        num_xs = 0
        num_os = 0
        for square in self.squares:
            if (square == 'X'):
                num_xs += 1
            elif (square == 'O'):
                num_os += 1
        if (num_xs == 0 or num_xs == num_os):
            return 'X'
        else:
            return 'O'

    def draw_text(self, square_index, x, y):
        if self.squares[square_index] != None:
            return

        letter = self.determine_letter_to_draw()
        self.canvas.create_text(x, y, text=letter, font=('Times', 50))
        self.squares[square_index] = letter 

    def game_has_a_winner(self):
        for winning_combo in self.WINNING_COMBOS:
            if self.squares[winning_combo[0]] == 'X' and self.squares[winning_combo[1]] == 'X' and self.squares[winning_combo[2]] == 'X':
                return True 
            elif self.squares[winning_combo[0]] == 'O' and self.squares[winning_combo[1]] == 'O' and self.squares[winning_combo[2]] == 'O':
                return True 

        return False 

    def game_is_a_draw(self):
        return ((not self.game_has_a_winner()) and self.all_squares_have_letters())

    def mouse_clicked(self, evt):
        if evt.y <= 0:
            return

        for i in range(len(self.SQUARE_COORDINATES)):
            if ((evt.x <= self.SQUARE_COORDINATES[i]['bottom_right_corner_x']) and (evt.y <= self.SQUARE_COORDINATES[i]['bottom_right_corner_y'])):
                self.draw_text(i, self.SQUARE_COORDINATES[i]['letter_x'], self.SQUARE_COORDINATES[i]['letter_y']) 
                break

        if self.game_has_a_winner():
            messagebox.showinfo('The Xs win!', 'The Xs win!')
            self.reset()
            return
        elif self.game_is_a_draw():
            messagebox.showinfo('Draw', 'This game is a draw')
            self.reset()
            return

        computer = Computer(self.squares)
        messagebox.showinfo('Computer Message', computer.message())
        i = computer.square()
        self.draw_text(i, self.SQUARE_COORDINATES[i]['letter_x'], self.SQUARE_COORDINATES[i]['letter_y']) 

        if self.game_has_a_winner():
            messagebox.showinfo('The Os win!', 'The Os win!')
            self.reset()
        elif self.game_is_a_draw():
            messagebox.showinfo('Draw', 'This game is a draw')
            self.reset()

    def reset(self):
        self.canvas.delete('all')

        self.canvas.create_line(150, 0, 150, 450)
        self.canvas.create_line(300, 0, 300, 450)
        self.canvas.create_line(0, 150, 450, 150)
        self.canvas.create_line(0, 300, 450, 300)

        self.squares = [None] * 9

