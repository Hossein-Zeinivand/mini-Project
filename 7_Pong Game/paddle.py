from turtle import Turtle 

class Paddle(Turtle):

    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(14, 2)
        self.penup()
        self.goto(y_position, x_position)

    def move_up(self):
        new_y = self.ycor() + 25
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 25
        self.goto(self.xcor(), new_y)
