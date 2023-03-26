from turtle import Turtle

class Margin(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, -300)
        self.setheading(90)
        self.draw_margin()

    def draw_margin(self):
        while self.ycor() <= 300:
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)


