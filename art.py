import turtle
from turtle import Turtle,Screen
import random

angle = [0, 90, 180, 270]

tim = Turtle()

turtle.colormode(255)
tim.pensize(5)
tim.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r,g,b)
    return random_color

def movement(qty):
    for _ in range(qty):
        tim.color(random_color())
        tim.forward(10)
        tim.setheading(random.choice(angle))



movement(200)









screen = Screen()
screen.exitonclick()