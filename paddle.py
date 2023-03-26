from turtle import Turtle
PADDLE_SPEED = 100

class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.goto(pos)

    def go_up(self):
        if self.ycor() < 250:
            self.goto(self.xcor(), self.ycor()+PADDLE_SPEED)

    def go_down(self):
        if self.ycor() > -250:
            self.goto(self.xcor(), self.ycor()-PADDLE_SPEED)
