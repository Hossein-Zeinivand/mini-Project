from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.right_score = 0
        self.left_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(100, 350)
        self.write(self.right_score, align="center", font=("Courier", 30, "normal"))
        self.goto(-100, 350)
        self.write(self.left_score, align="center", font=("Courier", 30, "normal"))
        self.goto(0, 350)
        self.write("-", align="center", font=("Courier", 30, "normal"))

    def add_point_to_right(self):
        self.right_score += 1
        self.update_scoreboard()

    def add_point_to_left(self):
        self.left_score += 1
        self.update_scoreboard()
