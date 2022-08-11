#firstly I've downloaded colorgram package into my IDE
import colorgram
import turtle
import random

number_of_iteration = 10
rgb_colors = []
colors = colorgram.extract('My_Image.jpg', number_of_iteration)
for color in colors:
    rgb_colors.append(color.rgb)
mouse = turtle.Turtle()
mouse.penup()
mouse.sety(-250)
mouse.setx(-250)
temp = mouse.xcor()
turtle.colormode(255)
print(rgb_colors)


def random_choice_from_color_list():
    generated_color = random.choice(rgb_colors)
    return generated_color


mouse.speed("fastest")
for i in range(100):
    current_color = random_choice_from_color_list()
    if i % 10 == 0 and i != 0:
        mouse.penup()
        mouse.sety(mouse.ycor() + 50)
        mouse.setx(temp)
    mouse.dot(20, current_color)
    mouse.penup()
    mouse.forward(50)


screen = turtle.Screen()
screen.setup(600,600)
screen.exitonclick()
