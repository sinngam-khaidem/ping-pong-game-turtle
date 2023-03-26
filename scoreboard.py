from turtle import Turtle
SCOREBOARD_POSITION = (0, 250)
ALIGNMENT = "center"
FONT = ('Times New Roman',40,'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.color("green")
        self.penup()
        self.goto(SCOREBOARD_POSITION)
        self.update_scores()

    def update_scores(self):
        self.write(arg=f"{self.l_score}   {self.r_score}", move=False, align=ALIGNMENT, font=FONT)
