import turtle

# create the Turtles
UKflag_layer1 = turtle.Turtle()
UKflag_layer2 = turtle.Turtle()
AUSflag = turtle.Turtle()
Star = turtle.Turtle()
Star5 = turtle.Turtle()
window = turtle.Screen()

# Hiding the Turtle icon
UKflag_layer1.hideturtle()
UKflag_layer2.hideturtle()
AUSflag.hideturtle()
Star.hideturtle()
Star5.hideturtle()


''' create the function to draw the UK Flag (draw_UKflag)
 I divide the UK flag to 2 layers:
    Layer 1 (UKflag_layer1): The darkblue background and 2 white diagonal lines 
    Layer 2 (UKflag_layer2): The red cross line; white cross line; and 4 red small pieces
'''


def draw_UKflag(x, y, length):
    # the function draw_UKflag with (x,y is the starting position of Turtle) and the length of the flag
    # starting draw the background of the UK flag
    UKflag_layer1.begin_fill()
    UKflag_layer1.color("darkblue", "darkblue")    # fill the color of the flag background
    UKflag_layer1.fillcolor("darkblue")
    UKflag_layer1.up()
    UKflag_layer1.goto(x, y)   # starting position
    UKflag_layer1.down()
    UKflag_layer1.left(90)
    # drawing the rectangle of the the flag with the length and the height = length/2
    for i in range(2):
        UKflag_layer1.forward(length/2)
        UKflag_layer1.left(90)
        UKflag_layer1.forward(length)
        UKflag_layer1.left(90)
    # starting drawing 2 white diagonal lines
    UKflag_layer1.end_fill()
    UKflag_layer1.begin_fill()
    UKflag_layer1.color("white", "white")
    UKflag_layer1.fillcolor("white")
    UKflag_layer1.up()
    UKflag_layer1.left(63.50)

    '''Next step to check the if the length of the flag = 300 then draw the diagonal lines = length + 35
            and if the length of the flag = 600 then draw the diagonal lines = length + 70
       This step to prepare for drawing AUS flag which contain the small UK flag (the size of a quarter)
            at the left up corner
    '''
    if length == 300:
        UKflag_layer1.forward(length+35)
    else:
        UKflag_layer1.forward(length+70)
    UKflag_layer1.down()
    UKflag_layer1.left(180 - 63.50)
    if length < 600:
        UKflag_layer1.forward((length/20)+1)
    else:
        UKflag_layer1.forward((length/20)+1)
    UKflag_layer1.left(63.50)
    UKflag_layer1.forward(length+2)
    UKflag_layer1.left(26.50)
    UKflag_layer1.forward((length/10)+1)
    UKflag_layer1.left(90)
    UKflag_layer1.forward(length/20)
    UKflag_layer1.left(63.50)
    UKflag_layer1.forward(length+5)
    UKflag_layer1.left(26.50)
    UKflag_layer1.forward((length/10)+1)
    UKflag_layer1.end_fill()

    UKflag_layer1.up()
    UKflag_layer1.backward(length)
    UKflag_layer1.left(26.6)
    if length < 600:
        UKflag_layer1.forward(length + 35.25)
    else:
        UKflag_layer1.forward(length + 70)
    UKflag_layer1.down()
    UKflag_layer1.begin_fill()
    UKflag_layer1.fillcolor("white")
    UKflag_layer1.left(180 - 26.50)
    UKflag_layer1.forward(length/10)
    UKflag_layer1.left(26.50)
    UKflag_layer1.forward(length+5)
    UKflag_layer1.left(63.50)
    UKflag_layer1.forward((length/20)-1)
    UKflag_layer1.left(90)
    UKflag_layer1.forward(length/10)
    UKflag_layer1.left(26.50)
    UKflag_layer1.forward(length+3.31)
    UKflag_layer1.left(63.50)
    UKflag_layer1.forward(length/20)
    UKflag_layer1.end_fill()

    '''
       This step to prepare for drawing AUS flag which contain the small UK flag (the size of a quarter)
            at the left up corner
       Next step to check the if the length of the flag = 600 draw the red cross line and white cross line
            and if the length of the flag = 600 then draw the diagonal lines = length + 70
    '''

    if length == 600:
        UKflag_layer2.up()
        UKflag_layer2.goto(x-300, y+150)
        UKflag_layer2.right(90)
        UKflag_layer2.forward(150)
        UKflag_layer2.down()
        UKflag_layer2.right(90)
        UKflag_layer2.begin_fill()
        UKflag_layer2.color("white", "white")
        UKflag_layer2.fillcolor("white")
        for i in range(2):
            UKflag_layer2.forward(50)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(100)
            UKflag_layer2.left(90)
            UKflag_layer2.forward(250)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(100)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(250)
            UKflag_layer2.left(90)
            UKflag_layer2.forward(100)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(50)
        UKflag_layer2.end_fill()

        UKflag_layer2.begin_fill()
        UKflag_layer2.color("white", "white")
        UKflag_layer2.fillcolor("red")
        for i in range(2):
            UKflag_layer2.forward(30)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(120)
            UKflag_layer2.left(90)
            UKflag_layer2.forward(270)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(60)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(270)
            UKflag_layer2.left(90)
            UKflag_layer2.forward(120)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(30)
        UKflag_layer2.end_fill()

        UKflag_layer2.up()
        UKflag_layer2.forward(300)
        UKflag_layer2.down()
        UKflag_layer2.right(90)
        for i in range(2):
            UKflag_layer2.begin_fill()
            UKflag_layer2.fillcolor("red")

            UKflag_layer2.right(63.50)
            UKflag_layer2.forward(225)
            UKflag_layer2.right(26.50)
            UKflag_layer2.forward(40)
            UKflag_layer2.right(180-26.50)
            UKflag_layer2.forward(225)
            UKflag_layer2.right(26.50)
            UKflag_layer2.forward(40)
            UKflag_layer2.end_fill()
            UKflag_layer2.backward(600)
            UKflag_layer2.begin_fill()
            UKflag_layer2.fillcolor("red")
            UKflag_layer2.right(26.5)
            UKflag_layer2.forward(225)
            UKflag_layer2.right(180-26.50)
            UKflag_layer2.forward(40)
            UKflag_layer2.right(26.5)
            UKflag_layer2.forward(180)
            UKflag_layer2.right(63.5)
            UKflag_layer2.forward(20)
            UKflag_layer2.end_fill()
            UKflag_layer2.backward(300)
    elif length == 300:
        UKflag_layer2.up()
        UKflag_layer2.goto(x - 150, y + 75)
        UKflag_layer2.right(90)
        UKflag_layer2.forward(75)
        UKflag_layer2.down()
        UKflag_layer2.right(90)
        UKflag_layer2.begin_fill()
        UKflag_layer2.fillcolor("white")
        for i in range(2):
            UKflag_layer2.up()
            UKflag_layer2.forward(25)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(50)
            UKflag_layer2.left(90)
            UKflag_layer2.forward(125)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(50)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(125)
            UKflag_layer2.left(90)
            UKflag_layer2.forward(50)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(25)
            UKflag_layer2.down()
        UKflag_layer2.end_fill()

        UKflag_layer2.begin_fill()
        UKflag_layer2.fillcolor("red")
        for i in range(2):
            UKflag_layer2.up()
            UKflag_layer2.forward(15)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(60)
            UKflag_layer2.left(90)
            UKflag_layer2.forward(270/2)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(60/2)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(270/2)
            UKflag_layer2.left(90)
            UKflag_layer2.forward(120/2)
            UKflag_layer2.right(90)
            UKflag_layer2.forward(30/2)
            UKflag_layer2.down()
        UKflag_layer2.end_fill()

        UKflag_layer2.up()
        UKflag_layer2.forward(300/2)
        UKflag_layer2.down()
        UKflag_layer2.right(90)
        UKflag_layer2.begin_fill()
        UKflag_layer2.fillcolor("red")
        for i in range(2):
            UKflag_layer2.up()
            UKflag_layer2.right(63.50)
            UKflag_layer2.forward(225/2)
            UKflag_layer2.right(26.50)
            UKflag_layer2.forward(40/2)
            UKflag_layer2.right(180 - 26.50)
            UKflag_layer2.forward(225/2)
            UKflag_layer2.right(26.50)
            UKflag_layer2.forward(40/2)
            UKflag_layer2.end_fill()
            UKflag_layer2.backward(600/2)
            UKflag_layer2.begin_fill()
            UKflag_layer2.fillcolor("red")
            UKflag_layer2.right(26.5)
            UKflag_layer2.forward(225/2)
            UKflag_layer2.right(180 - 26.50)
            UKflag_layer2.forward(40/2)
            UKflag_layer2.right(26.5)
            UKflag_layer2.forward(180/2)
            UKflag_layer2.right(63.5)
            UKflag_layer2.forward(20/2)
            UKflag_layer2.backward(300/2)
            UKflag_layer2.down()
        UKflag_layer2.end_fill()


def draw_star_7_side(size):
    Star.begin_fill()
    Star.color("white", "white")
    Star.fillcolor("white")
    Star.left(90)
    Star.up()
    Star.forward(size)
    Star.down()

    Star.right(166)
    for i in range(7):
        Star.forward(size)
        Star.left(101.25)
        Star.forward(size)
        Star.right(152.70)
    Star.right(180 - 153)
    Star.end_fill()


def draw_AUSflag(x, y, length):
    AUSflag.goto(x - 300, y + 150)
    AUSflag.right(90)
    AUSflag.begin_fill()
    AUSflag.fillcolor("darkblue")
    for i in range(2):
        AUSflag.forward(300)
        AUSflag.left(90)
        AUSflag.forward(600)
        AUSflag.left(90)
    AUSflag.end_fill()
    draw_UKflag(x, y, 300)

    AUSflag.up()
    AUSflag.goto(x+300, y-150)
    AUSflag.down()
    AUSflag.color("white")
    AUSflag.left(180)
    for i in range(2):
        AUSflag.forward(length / 2)
        AUSflag.left(90)
        AUSflag.forward(length)
        AUSflag.left(90)

    Star.up()
    Star.goto(x - 150, y - 60)
    Star.down()
    draw_star_7_side(30)

    Star.up()
    Star.goto(x + 150, y + 100)
    Star.down()
    draw_star_7_side(15)

    Star.up()
    Star.goto(x + 145, y - 100)
    Star.down()
    draw_star_7_side(15)

    Star.up()
    Star.goto(x + 75, y + 45/2)
    Star.down()
    draw_star_7_side(15)

    Star.up()
    Star.goto(x + 225, y + 75/2)
    Star.down()
    draw_star_7_side(15)

# small star 5 sides
    Star5.up()
    Star5.goto(x + 180.5, y-10)
    Star5.down()
    Star5.begin_fill()
    Star5.color("white", "white")
    Star5.fillcolor("white")
    Star5.left(90)
    Star5.up()
    Star5.forward(10)
    Star5.down()
    Star5.right(162)
    for i in range(5):
        Star5.forward(10)
        Star5.left(72)
        Star5.forward(10)
        Star5.right(144)
    Star5.end_fill()


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
    draw_UKflag(300, -150, 600)
elif n == "2":
    draw_AUSflag(0, 0, 600)
elif n == "3":
    print("Program exits. Have a nice day!")
    exit()
window.exitonclick()
