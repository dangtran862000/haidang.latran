import turtle
Star = turtle.Turtle()
window = turtle.Screen()

Star.begin_fill()
Star.color("yellow", "yellow")
Star.fillcolor("yellow")


for i in range(5):
    Star.forward(300)
    Star.right(144)

Star.end_fill()
window.exitonclick()