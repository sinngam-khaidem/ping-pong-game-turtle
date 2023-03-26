import time
from turtle import Turtle
import random
CHANGE = [-5, 5, -6, 6, -7, 7, -8, 8, -9, -9, -10, 10]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.x_change = 0
        self.y_change = 0
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.reset_ball()

    def reset_ball(self):
        self.x_change = random.choice(CHANGE)
        self.y_change = random.choice(CHANGE)
        self.goto(0, 0)

    def move(self):
        new_x = self.xcor() + self.x_change
        new_y = self.ycor() + self.y_change
        self.goto(new_x, new_y)

    def change_dir_wall(self):
        if self.x_change >= 0 and self.y_change >= 0:
            self.x_change = self.x_change
            self.y_change = 0 - self.y_change
            self.move()

        elif self.x_change <= 0 and self.y_change >= 0:
            self.x_change = self.x_change
            self.y_change = 0 - self.y_change
            self.move()

        elif self.x_change >= 0 and self.y_change <= 0:
            self.x_change = self.x_change
            self.y_change = 0 - self.y_change
            self.move()

        elif self.x_change <= 0 and self.y_change <= 0:
            self.x_change = self.x_change
            self.y_change = 0 - self.y_change
            self.move()

    def change_dir_pad(self):
        if self.x_change >= 0 and self.y_change >= 0:
            self.x_change = 0 - self.x_change
            self.y_change = self.y_change
            self.move()

        elif self.x_change <= 0 and self.y_change >= 0:
            self.x_change = 0 - self.x_change
            self.y_change = self.y_change
            self.move()

        elif self.x_change >= 0 and self.y_change <= 0:
            self.x_change = 0 - self.x_change
            self.y_change = self.y_change
            self.move()

        elif self.x_change <= 0 and self.y_change <= 0:
            self.x_change = 0 - self.x_change
            self.y_change = self.y_change
            self.move()
