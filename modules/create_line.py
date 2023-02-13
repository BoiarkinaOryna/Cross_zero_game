import turtle
def draw_line_horizontal(x, y):
    t4.penup()
    t4.goto(x, y)
    t4.pendown()
    t4.goto(x + 200, y)
def draw_line_vertical(x, y):
    t4.penup()
    t4.goto(x, y)
    t4.pendown()
    t4.goto(x, y - 200)
def draw_line_digonal(x, y):
    t4.penup()
    t4.goto(x, y)
    t4.pendown()
    if x == -50:
        t4.goto(x + 200, y - 200)
    elif x == 150:
        t4.goto(x - 200, y - 200)

t4 = turtle.Turtle()
t4.hideturtle()
t4.color("red")
t4.width(5)