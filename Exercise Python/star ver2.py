import turtle
Star = turtle.Turtle()
window = turtle.Screen()
window.bgcolor("red")

Star.begin_fill()
Star.color("yellow", "yellow")
Star.fillcolor("yellow")

Star.circle(100,180)

Star.up()
Star.backward(150)
Star.down()

for i in range(5):
    Star.forward(300)
    Star.right(144)

Star.end_fill()
window.exitonclick()