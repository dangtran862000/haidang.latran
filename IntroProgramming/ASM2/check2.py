# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: La Tran Hai Dang (s3836605)
# Created date: dd/mm/yyyy
# Last modified date: dd/mm/yyyy

import turtle

window = turtle.Screen()

# creating the Turtles
uk_flag_layer1 = turtle.Turtle()
uk_flag_layer2 = turtle.Turtle()
aus_flag = turtle.Turtle()
star_7_sides = turtle.Turtle()
star_5_sides = turtle.Turtle()
'''
# setting the speed of the Turtles
uk_flag_layer1.speed(0)
uk_flag_layer2.speed(0)
aus_flag.speed(0)
star_7_sides.speed(0)
star_5_sides.speed(0)
'''
'''
# Hiding the Turtles icon
uk_flag_layer1.hideturtle()
uk_flag_layer2.hideturtle()
aus_flag.hideturtle()
star_7_sides.hideturtle()
star_5_sides.hideturtle()
'''
''' create the function to draw the UK Flag (draw_uk_flag)
 I divide the UK flag to 2 layers:
    Layer 1 (uk_flag_layer1): The darkblue background and 2 white diagonal lines 
    Layer 2 (uk_flag_layer2): The red cross shape; white cross shape; and 4 red small diagonal pieces
'''

length=600
x=300
y=-150
uk_flag_layer1.begin_fill()
uk_flag_layer1.color("darkblue", "darkblue")  # fill the color of the flag background
uk_flag_layer1.fillcolor("darkblue")
uk_flag_layer1.up()
uk_flag_layer1.goto(x, y)  # starting position
uk_flag_layer1.down()
uk_flag_layer1.left(90)
    # drawing the rectangle of the the flag with the length and the height = length/2
for i in range(2):
    uk_flag_layer1.forward(length / 2)
    uk_flag_layer1.left(90)
    uk_flag_layer1.forward(length)
    uk_flag_layer1.left(90)
    # starting drawing 2 white diagonal lines
uk_flag_layer1.end_fill()

uk_flag_layer1.goto(-300,-150)
uk_flag_layer1.right(63.5)
uk_flag_layer1.end_fill()
uk_flag_layer1.begin_fill()
uk_flag_layer1.color("black", "black")
uk_flag_layer1.fillcolor("black")
uk_flag_layer1.up()
'''Next step to check the if the length of the flag = 300 then draw the diagonal lines = length + 35
            and if the length of the flag = 600 then draw the diagonal lines = length + 70
       This step to prepare for drawing AUS flag which contain the small UK flag (the size of a quarter)
            at the left up corner
    '''

def white_line():
    if length == 300:
        uk_flag_layer1.forward(length + 35.5)
    else:
        uk_flag_layer1.forward(length + 70)
    uk_flag_layer1.down()
    uk_flag_layer1.right(180 - 63.50)
    uk_flag_layer1.forward((length / 20))
    uk_flag_layer1.right(63.50)
    uk_flag_layer1.forward(length + 2)
    uk_flag_layer1.right(26.50)
    uk_flag_layer1.forward((length / 10) + 1)
    uk_flag_layer1.right(90)
    uk_flag_layer1.forward(length / 20)
    uk_flag_layer1.right(63.50)
    uk_flag_layer1.forward(length + 5)
    uk_flag_layer1.right(26.50)
    uk_flag_layer1.forward((length / 10) + 1)
    uk_flag_layer1.end_fill()
    # This step is used to check the length of each flag and draw it proportionally.

white_line()



window.exitonclick()
