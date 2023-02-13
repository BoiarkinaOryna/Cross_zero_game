'''
    
'''

import turtle

t2 = turtle.Turtle()
t2.width(3)
t2.color("red")
t2.speed(0)
t2.hideturtle()

def draw_cross(x, y):
    t2.penup()
    t2.goto(x, y)
    t2.pendown()
    t2.goto(x + 100, y - 100)
    t2.penup()
    t2.goto(x + 100, y)
    t2.pendown()
    t2.goto(x, y - 100)
    