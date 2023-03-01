from turtle import *

t = Turtle()
t.speed('fastest')
s = Screen()

s.bgcolor('black')
t.pencolor('pink')

t.width(3)

colors = ['green', 'yellow', 'blue', 'red']

for x in range(600):
    t.pencolor(colors[x % 4])
    # t.penup()
    t.forward(2 * x)
    # t.pendown()
    # t.write('anyád!')
    t.left(45)