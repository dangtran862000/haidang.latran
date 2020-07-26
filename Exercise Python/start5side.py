import turtle
Star = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("red")

Star.begin_fill()
Star.color("yellow", "yellow")
Star.fillcolor("yellow")

def draw_star_7_side(size):
    Star.left(90)
    Star.up()
    Star.forward(size)
    Star.down()

    Star.right(162)
    for i in range(5):
        Star.forward(size)
        Star.left(72)
        Star.forward(size)
        Star.right(144)

draw_star_7_side(40)
Star.end_fill()
window.exitonclick()