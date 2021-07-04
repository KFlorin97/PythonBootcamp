import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
t.Screen().bgcolor("black")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


turtle.speed("fastest")

def draw_spirogragh(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.setheading(turtle.heading() + size_of_gap)

draw_spirogragh(2)


"""directions = [0, 90, 180, 270]
turtle.pensize(10)
turtle.speed("fastest")

for i in range(200):
    turtle.color(random_color())
    turtle.forward(50)
    turtle.setheading(random.choice(directions))"""

"""def draw_shape(num_sides):
    angle = 360 / num_sides
    for i in range(num_sides):
        turtle.forward(100)
        turtle.right(angle)

for shape_side in range(3,11):
    draw_shape(shape_side)"""


screen = t.Screen()
screen.exitonclick()