import random


class CA:
    def __init__(self, x, y):
        self.size_x = x
        self.size_y = y
        self.field = [[0 for i in range(self.size_x)] for j in range(self.size_y)]
        self.buffer_field = [[0 for i in range(self.size_x)] for j in range(self.size_y)]

    def Initialaze(self, life_percent):
        life_percent = int(self.size_x * self.size_y * life_percent / 100)
        for n in range(life_percent):
            x = random.randint(0, self.size_x - 1)
            y = random.randint(0, self.size_y - 1)
            self.field[y][x] = 1

    def Print_field(self):
        for i in self.field:
            print(i)
        input()

    def Field_to_buffer(self):
        for i in range(self.size_y):
            for j in range(self.size_x):
                self.buffer_field[i][j] = self.field[i][j]

    def Update(self):
        self.Field_to_buffer()
        for y1 in range(self.size_y):
            for x1 in range(self.size_x):
                counter = 0
                for y2 in range(-1, 2):
                    for x2 in range(-1, 2):
                        if (y2 != 0) & (x2 != 0):
                            if (y1 + y2) >= self.size_y:
                                y_n = 0
                            elif (y1 + y2) < 0:
                                y_n = self.size_y - 1
                            else:
                                y_n = y1 + y2
                            if (x1 + x2) >= self.size_x:
                                x_n = 0
                            elif (x1 + x2) < 0:
                                x_n = self.size_x - 1
                            else:
                                x_n = x1 + x2
                            if self.buffer_field[y_n][x_n] == 1:
                                counter += 1
                if (self.buffer_field[y1][x1] == 0) & counter == 3:
                    self.field[y1][x1] = 1
                elif (self.buffer_field[y1][x1] == 1) & ((counter == 3) | (counter == 2)):
                    self.field[y1][x1] = 1
                elif (self.buffer_field[y1][x1] == 1) & ((counter > 3) | (counter < 2)):
                    self.field[y1][x1] = 0
                else:
                    self.field[y1][x1] = 0

    def Check(self):
        mode_on = False
        for i in range(self.size_y):
            for j in range(self.size_x):
                if self.field[i][j] == 1:
                    mode_on = True
        return mode_on


def main():
    x = int(input('Введите длину по оси Х: '))
    y = int(input('Введите длину по оси Y: '))
    ca = CA(x, y)
    life_percent = int(input('Введите процент живых клеток: '))
    ca.Initialaze(life_percent)
    ca.Print_field()
    while ca.Check():
        ca.Update()
        ca.Print_field()
    print('Произошло вымирание')

main()
