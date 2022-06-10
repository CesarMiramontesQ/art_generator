import turtle
from turtle import Turtle, Screen
import random

tim = Turtle()
colors = ['blue', 'red', 'green', 'purple', 'pink', 'yellow', 'black', '#2f45ff', '#54ffa4', '#11ff22', '#285078', '#a0c8f0', '#33cc8c' ]
angle = [90, 180, 270, 360]
tim.pensize(5)
tim.speed('fastest')
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

def draw_shape(num_sides):
    for _ in range(num_sides):
        tim.forward(10)
        tim.setheading(random.choice(angle))
        tim.color(random_color())


for shape_side_n in range(30):

    draw_shape(shape_side_n)










screen = Screen()
screen.exitonclick()