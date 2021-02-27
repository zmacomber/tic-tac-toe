import random

class Computer:
 
    MESSAGES = [
        'Hmm, interesting',
        'Ok',
        'Are you sure you want to do that?',
        'Fine',
        'Really',
        'Ooohhhh, boy',
        'O, common',
        'O common, you can do better than that',
        'What?!'
    ]

    def __init__(self, squares):
        self.squares = squares

    def message(self):
        return self.MESSAGES[random.randint(0,8)]

    def square(self):
        if self.square_should_be_0():
            return 0
        elif self.square_should_be_1():
            return 1
        elif self.square_should_be_2():
            return 2
        elif self.square_should_be_3():
            return 3
        elif self.square_should_be_4():
            return 4
        elif self.square_should_be_5():
            return 5
        elif self.square_should_be_6():
            return 6
        elif self.square_should_be_7():
            return 7
        else:
            return 8

    def square_should_be_0(self):
        if self.squares[0] == None:
            if self.squares[4] == 'X' \
            or self.squares[3] == 'X' and self.squares[6] == 'X' \
            or self.squares[1] == 'X' and self.squares[2] == 'X':
                return True
            if self.squares[4] == 'O' and self.squares[8] == 'O' \
            or self.squares[1] == 'O' and self.squares[2] == 'O' \
            or self.squares[3] == 'O' and self.squares[6] == 'O':
                return True
            if self.squares == [None, 'X', None, None, 'O', 'X', None, None, None] \
            or self.squares == [None, None, None, 'X', 'O', None, None, 'X', None]:
                return True
        return False

    def square_should_be_1(self):
        if self.squares[1] == None:
            if self.squares[4] == 'X' and self.squares[7] == 'X' \
            or self.squares[0] == 'X' and self.squares[2] == 'X':
                return True
            if self.squares[0] == 'O' and self.squares[2] == 'O' \
            or self.squares[4] == 'O' and self.squares[7] == 'O':
                return True
            if self.squares == [None, None, None, 'X', 'O', None, None, None, 'X'] \
            or self.squares == [None, None, None, 'X', 'O', 'X', None, None, None] \
            or self.squares == [None, None, None, None, 'O', 'X', 'X', None, None]:
                return True
        return False

    def square_should_be_2(self):
        if self.squares[2] == None:
            if self.squares[5] == 'X' and self.squares[8] == 'X' \
            or self.squares[4] == 'X' and self.squares[6] == 'X' \
            or self.squares[0] == 'X' and self.squares[1] == 'X' \
            or self.squares[4] == 'X' and self.squares[8] == 'X':
                return True
            if self.squares[0] == 'O' and self.squares[1] == 'O' \
            or self.squares[4] == 'O' and self.squares[6] == 'O' \
            or self.squares[5] == 'O' and self.squares[8] == 'O':
                return True
            if self.squares == ['X', None, None, 'O', 'O', 'X', 'X', 'X', 'O'] \
            or self.squares == [None, None, None, None, 'O', 'X', None, 'X', None]:
                return True
        return False

    def square_should_be_3(self):
        if self.squares[3] == None:
            if self.squares[0] == 'X' and self.squares[6] == 'X' \
            or self.squares[4] == 'X' and self.squares[5] == 'X':
                return True
            if self.squares[0] == 'O' and self.squares[6] == 'O' \
            or self.squares[4] == 'O' and self.squares[5] == 'O':
                return True
            if self.squares == [None, 'X', None, None, 'O', None, None, None, 'X'] \
            or self.squares == [None, 'X', None, None, 'O', None, None, 'X', None] \
            or self.squares == ['X', None, None, None, 'O', None, None, None, 'X'] \
            or self.squares == [None, None, 'X', None, 'O', None, 'X', None, None] \
            or self.squares == ['X', 'O', 'X', None, 'O', 'X', None, 'X', 'O']:
                return True
        return False

    def square_should_be_4(self):
        if self.squares[4] == None:
            if self.squares[0] == 'X' \
            or self.squares[1] == 'X' \
            or self.squares[2] == 'X' \
            or self.squares[3] == 'X' \
            or self.squares[5] == 'X' \
            or self.squares[6] == 'X' \
            or self.squares[7] == 'X' \
            or self.squares[8] == 'X':
                return True
            if self.squares[0] == 'O' and self.squares[8] == 'O' \
            or self.squares[1] == 'O' and self.squares[7] == 'O' \
            or self.squares[2] == 'O' and self.squares[6] == 'O' \
            or self.squares[3] == 'O' and self.squares[5] == 'O':
                return True
        return False

    def square_should_be_5(self):
        if self.squares[5] == None:
            if self.squares[2] == 'X' and self.squares[8] == 'X' \
            or self.squares[4] == 'X' and self.squares[3] == 'X':
                return True
            if self.squares[4] == 'O' and self.squares[3] == 'O' \
            or self.squares[2] == 'O' and self.squares[8] == 'O':
                return True
            if self.squares == ['O','X','O',None,'X',None,'X','O','X'] \
            or self.squares == [None, 'X', None, None, 'O', None, 'X', None, None]:
                return True
        return False
    
    def square_should_be_6(self):
        if self.squares[6] == None:
            if self.squares[4] == 'X' and self.squares[2] == 'X' \
            or self.squares[3] == 'X' and self.squares[0] == 'X' \
            or self.squares[7] == 'X' and self.squares[8] == 'X':
                return True
            if self.squares[3] == 'O' and self.squares[0] == 'O' \
            or self.squares[4] == 'O' and self.squares[2] == 'O' \
            or self.squares[7] == 'O' and self.squares[8] == 'O':
                return True
            if self.squares == ['X', None, None, None, 'O', 'X', None, 'X', 'O'] \
            or self.squares == [None, 'X', None, 'X', 'O', None, None, None, None]:
                return True
        return False

    def square_should_be_7(self):
        if self.squares[7] == None:
            if self.squares[8] == 'X' and self.squares[6] == 'X' \
            or self.squares[4] == 'X' and self.squares[1] == 'X':
                return True
            if self.squares[6] == 'O' and self.squares[8] == 'O' \
            or self.squares[4] == 'O' and self.squares[1] == 'O':
                return True
            if self.squares == ['O', 'X', 'X', 'X', 'O', 'O', None, None, 'X']:
                return True
        return False
