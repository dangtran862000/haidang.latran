import turtle
Star = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("red")

Star.begin_fill()
Star.color("yellow", "yellow")
Star.fillcolor("yellow")

Star.left(90)
Star.up()
Star.forward(120)
Star.down()

Star.right(162)
for i in range(7):
    Star.forward(120)
    Star.left(12.875)
    Star.forward(120)
    Star.right(154.25)

Star.end_fill()
window.exitonclick()
