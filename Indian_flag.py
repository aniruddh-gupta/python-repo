import turtle
import time

screen = turtle.Screen()
screen.bgcolor("red")
screen.title("Indian Flag ")
oogway = turtle.Turtle()
oogway.speed(100)
oogway.penup()
oogway.hideturtle()
Name = "INDIAN FLAG"
oogway.write(Name, False, align="center", font=("Arial", 14, "normal"))
flag_height = 300
flag_width = 450
start_x = -225
start_y = 150
stripe_height = flag_height/3
stripe_width = flag_width

chakra_radius = 545 / 2
chakra_radius1 = 100 / 2

def draw_fill_rectangle(x, y, height, width, color):
    oogway.goto(x,y)
    oogway.pendown()
    oogway.color(color)
    oogway.begin_fill()
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.forward(width)
    oogway.right(90)
    oogway.forward(height)
    oogway.right(90)
    oogway.end_fill()
    oogway.penup()

def draw_stripes():
    x = start_x
    y = start_y

    draw_fill_rectangle(x, y, stripe_height, stripe_width, "#FF9933")
    y = y - stripe_height   
    
    draw_fill_rectangle(x, y, stripe_height, stripe_width, "white")
    y = y - stripe_height               

    draw_fill_rectangle(x, y, stripe_height, stripe_width, 'green')
    y = y - stripe_height

def draw_chakra():
    oogway.speed(6)
    oogway.goto(0,0)
    color = "#000080" # navy blue
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(0, 0 - chakra_radius)
    oogway.pendown()
    oogway.circle(chakra_radius)
    # draw 24 spikes in chakra
    for _ in range(24):
        oogway.penup()
        oogway.goto(0,0)
        oogway.left(15)
        oogway.pendown()
        oogway.forward(chakra_radius)
draw_chakra()
time.sleep(0)

def draw_chakra1():
    oogway.speed(6)
    oogway.goto(0,0)
    color = "#000080" # navy blue
    oogway.penup()
    oogway.color(color)
    oogway.fillcolor(color)
    oogway.goto(0, 1 - chakra_radius1)
    oogway.pendown()
    oogway.circle(chakra_radius1)
    for _ in range(24):
        oogway.penup()
        oogway.goto(0,0)
        oogway.left(15)
        oogway.pendown()
        oogway.forward(chakra_radius1)

time.sleep(0)
draw_stripes()
draw_chakra1()
screen.mainloop()
