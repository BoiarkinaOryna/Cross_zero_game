'''
   
'''

import turtle

t1 = turtle.Turtle()
t1.width(3)
t1.speed(0)
t1.hideturtle()

def draw_table():
    x = 0 
    y = 0
    # Малюємо три ряда по три квадрати
    for count in range(3):
    # Цикл що відповідає за малювання одного ряду з трьома квадратами
        for count in range(3):
            t1.penup()
            t1.goto(x, y)
            t1.pendown()
            # Малюємо один квадрат 
            for count in range(4):
                t1.left(90)
                t1.forward(100)
            x += 100
        x = 0
        y -= 100
    
            
    


   