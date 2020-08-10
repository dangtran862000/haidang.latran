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


def draw_uk_flag_layer2(x, y, length):  # this is the function to draw the Layer 2 of the UK flag
    uk_flag_layer2.up()
    uk_flag_layer2.goto(x - (length/2), y + (length/4))  # setting the start position to draw the Layer 2
    uk_flag_layer2.right(90)
    uk_flag_layer2.forward((length/4))
    uk_flag_layer2.down()
    uk_flag_layer2.right(90)
    # drawing the white cross line
    uk_flag_layer2.begin_fill()
    uk_flag_layer2.color("white", "white")
    uk_flag_layer2.fillcolor("white")
    for i in range(2):  # This loop used for shortening by being symmetrical across the axis of the white cross shape
        uk_flag_layer2.forward(length/12)
        uk_flag_layer2.right(90)
        uk_flag_layer2.forward(length/6)
        uk_flag_layer2.left(90)
        uk_flag_layer2.forward(length/2.4)
        uk_flag_layer2.right(90)
        uk_flag_layer2.forward(length/6)
        uk_flag_layer2.right(90)
        uk_flag_layer2.forward(length/2.4)
        uk_flag_layer2.left(90)
        uk_flag_layer2.forward(length/6)
        uk_flag_layer2.right(90)
        uk_flag_layer2.forward(length/12)
    uk_flag_layer2.end_fill()
    # drawing the red cross line
    uk_flag_layer2.begin_fill()
    uk_flag_layer2.fillcolor("red")
    for i in range(2):  # This loop used for shortening by being symmetrical across the axis of the red cross shape
        uk_flag_layer2.forward(length/20)
        uk_flag_layer2.right(90)
        uk_flag_layer2.forward(length/5)
        uk_flag_layer2.left(90)
        uk_flag_layer2.forward(length/(20/9))
        uk_flag_layer2.right(90)
        uk_flag_layer2.forward(length/10)
        uk_flag_layer2.right(90)
        uk_flag_layer2.forward(length/(20/9))
        uk_flag_layer2.left(90)
        uk_flag_layer2.forward(length/5)
        uk_flag_layer2.right(90)
        uk_flag_layer2.forward(length/20)
    uk_flag_layer2.end_fill()
    # drawing 4 red cross diagonal pieces
    uk_flag_layer2.up()
    uk_flag_layer2.forward(length/2)
    uk_flag_layer2.down()
    uk_flag_layer2.right(90)
    # This loop used for shortening to draw 4 red cross diagonal pieces
    # by being symmetrical across the axis of the flag
    for i in range(2):
        uk_flag_layer2.begin_fill()
        uk_flag_layer2.fillcolor("red")
        uk_flag_layer2.right(63.50)
        uk_flag_layer2.forward(length/(8/3))
        uk_flag_layer2.right(26.50)
        uk_flag_layer2.forward(length/15)
        uk_flag_layer2.right(180 - 26.50)
        uk_flag_layer2.forward(length/(8/3))
        uk_flag_layer2.right(26.50)
        uk_flag_layer2.forward(length/15)
        uk_flag_layer2.end_fill()
        uk_flag_layer2.up()
        uk_flag_layer2.backward(length)
        uk_flag_layer2.down()

        uk_flag_layer2.begin_fill()
        uk_flag_layer2.fillcolor("red")
        uk_flag_layer2.right(26.5)
        uk_flag_layer2.forward(length/(8/3))
        uk_flag_layer2.right(180 - 26.50)
        uk_flag_layer2.forward(length/15)
        uk_flag_layer2.right(26.5)
        uk_flag_layer2.forward(length/(10/3))
        uk_flag_layer2.right(63.5)
        uk_flag_layer2.penup()
        uk_flag_layer2.forward(length/30)
        uk_flag_layer2.pendown()
        uk_flag_layer2.end_fill()
        uk_flag_layer2.up()
        uk_flag_layer2.backward(length/2)
        uk_flag_layer2.down()


def draw_uk_flag(x, y, length):  # this is the function to draw full of the uk flag
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
    uk_flag_layer1.begin_fill()
    uk_flag_layer1.color("white", "white")
    uk_flag_layer1.fillcolor("white")
    uk_flag_layer1.up()
    uk_flag_layer1.left(63.50)

    '''Next step to check the if the length of the flag = 300 then draw the diagonal lines = length + 35
            and if the length of the flag = 600 then draw the diagonal lines = length + 70
       This step to prepare for drawing AUS flag which contain the small UK flag (the size of a quarter)
            at the left up corner
    '''

    uk_flag_layer1.forward(length/(60/67))
    uk_flag_layer1.down()
    uk_flag_layer1.left(180 - 63.50)
    uk_flag_layer1.forward((length / 20))
    uk_flag_layer1.left(63.50)
    uk_flag_layer1.forward(length + 2)
    uk_flag_layer1.left(26.50)
    uk_flag_layer1.forward((length / 10))
    uk_flag_layer1.left(90)
    uk_flag_layer1.forward(length / 20)
    uk_flag_layer1.left(63.50)
    uk_flag_layer1.forward(length + 5)
    uk_flag_layer1.left(26.50)
    uk_flag_layer1.forward((length / 10) + 1)
    uk_flag_layer1.end_fill()

    uk_flag_layer1.up()
    uk_flag_layer1.backward(length)
    uk_flag_layer1.left(26.6)
    uk_flag_layer1.forward(length/(60/67))
    uk_flag_layer1.down()
    uk_flag_layer1.begin_fill()
    uk_flag_layer1.fillcolor("white")
    uk_flag_layer1.left(180 - 26.50)
    uk_flag_layer1.forward((length / 10))
    uk_flag_layer1.left(26.50)
    uk_flag_layer1.forward(length + 5)
    uk_flag_layer1.left(63.50)
    uk_flag_layer1.forward((length / 10) - 1)
    uk_flag_layer1.left(90)
    uk_flag_layer1.forward(length / 10)
    uk_flag_layer1.left(26.50)
    uk_flag_layer1.forward(length + 3.31)
    uk_flag_layer1.left(63.50)
    uk_flag_layer1.forward(length / 20)
    uk_flag_layer1.end_fill()
    # This step is used to check the length of each flag and draw it proportionally.
    if length >= 600:
        draw_uk_flag_layer2(x, y, length)
    elif length <= 300:
        draw_uk_flag_layer2(x, y, length)


def draw_star_7_side(size):  # this is the function to draw the start with 7 side of the UK flag
    star_7_sides.begin_fill()
    star_7_sides.color("white", "white")
    star_7_sides.fillcolor("white")
    star_7_sides.left(90)
    star_7_sides.up()
    star_7_sides.forward(size)
    star_7_sides.down()

    star_7_sides.right(166)
    for i in range(7):
        star_7_sides.forward(size)
        star_7_sides.left(101.25)
        star_7_sides.forward(size)
        star_7_sides.right(152.70)
    star_7_sides.right(180 - 153)
    star_7_sides.end_fill()


def draw_aus_flag(x, y, length):    # this is the function to draw the start with 7 side of the UK flag
    aus_flag.goto(x - (length/2), y + (length/4))
    aus_flag.right(90)
    aus_flag.begin_fill()
    aus_flag.fillcolor("darkblue")
    for i in range(2):
        aus_flag.forward(length/2)
        aus_flag.left(90)
        aus_flag.forward(length)
        aus_flag.left(90)
    aus_flag.end_fill()
    draw_uk_flag(x, y, length/2)
    aus_flag.up()
    aus_flag.forward((length/4)+1)
    aus_flag.down()
    aus_flag.pensize(2)
    aus_flag.color("darkblue")
    aus_flag.left(90)
    aus_flag.forward((length/2)+1.25)
    aus_flag.left(90)
    aus_flag.forward(length/4)

    star_7_sides.up()
    star_7_sides.goto((x - (length/4), y - (length/10)))
    star_7_sides.down()
    draw_star_7_side(length/20)

    position_list = [(x + (length/4), y + (length/6)),
                     (x + (length/(600/145)), y - (length/6)),
                     (x + (length/8), y + (length/(80/3))),
                     (x + (length/(8/3)), y + (length/16))]

    for position in position_list:
        star_7_sides.up()
        star_7_sides.goto(position)
        star_7_sides.down()
        draw_star_7_side(length/40)

# small star 5 sides
    star_5_sides.up()
    star_5_sides.goto(x + (length/(10/3)), y-(length/60))
    star_5_sides.down()
    star_5_sides.begin_fill()
    star_5_sides.color("white", "white")
    star_5_sides.fillcolor("white")
    star_5_sides.left(90)
    star_5_sides.up()
    star_5_sides.forward(length/60)
    star_5_sides.down()
    star_5_sides.right(162)
    for i in range(5):
        star_5_sides.forward(length/60)
        star_5_sides.left(72)
        star_5_sides.forward(length/60)
        star_5_sides.right(144)
    star_5_sides.end_fill()


def input_info():
    print("***************************")
    print("1. Draw UK flag")
    print("2. Draw Australia flag")
    print("3. Exit")


input_info()
n = input("Enter an option (1/2/3): ")


while (n != "1") and (n != "2") and (n != "3"):
    print("Invalid option")
    input_info()
    n = input("Enter an option (1/2/3): ")
if n == "1":
    draw_uk_flag(300, -150, 600)
elif n == "2":
    draw_aus_flag(0, 0, 600)
elif n == "3":
    print("Program exits. Have a nice day!")
    exit()
    

window.exitonclick()
