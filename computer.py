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
            if self.squares[4] == 'X':
                return True

        return False

    def square_should_be_1(self):
        return False

    def square_should_be_2(self):
        return False

    def square_should_be_3(self):
        return False

    def square_should_be_4(self):
        return False

    def square_should_be_5(self):
        return False
    
    def square_should_be_6(self):
        return False

    def square_should_be_7(self):
        return False

