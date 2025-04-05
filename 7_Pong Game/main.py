from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.tracer(0)
screen.setup(1700, 1100)
screen.title("PONG GAME")
screen.bgcolor("black")

right_paddle = Paddle(0, 790)
left_paddle = Paddle(0, -790)
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(fun=right_paddle.move_up, key="o")
screen.onkey(fun=right_paddle.move_down, key="l")
screen.onkey(fun=left_paddle.move_up, key="w")
screen.onkey(fun=left_paddle.move_down, key="s")

ball = Ball()

game_is_running = True

while game_is_running:
    screen.update()
    time.sleep(0.05)
    ball.move_ball()

    if ball.ycor() > 500 or ball.ycor() < -500:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 100 and ball.xcor() > 750) or \
       (ball.distance(left_paddle) < 100 and ball.xcor() < -750):
        ball.bounce_x()

    if ball.xcor() > 790:
        ball.reset_position()
        scoreboard.add_point_to_left()

    if ball.xcor() < -790:
        ball.reset_position()
        scoreboard.add_point_to_right()

screen.mainloop()
