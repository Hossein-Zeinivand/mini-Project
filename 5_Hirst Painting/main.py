import turtle
import random


hirst = turtle.Turtle()
hirst.hideturtle()
turtle.colormode(255)


hirst.speed("fastest")
rows = 5
columns = 4 
x = -100
y = 100

for row in range(rows):
    for column in range(columns):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        hirst.penup()
        hirst.goto(x + column * 90, y - row * 90) 
        hirst.fillcolor((r, g, b))
        hirst.begin_fill()
        hirst.circle(35)
        hirst.end_fill()


screen = turtle.Screen()
screen.mainloop()
