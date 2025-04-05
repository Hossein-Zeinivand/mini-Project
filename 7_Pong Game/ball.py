from turtle import Turtle 

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(2, 2)

        self.x_velocity = 10
        self.y_velocity = 10

    def move_ball(self):
        new_x = self.xcor() + self.x_velocity
        new_y = self.ycor() + self.y_velocity
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_velocity *= -1

    def bounce_x(self):
        self.x_velocity *= -1

    def reset_position(self):
        self.goto(0, 0)
