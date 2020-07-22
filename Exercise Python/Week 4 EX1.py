import turtle
square=turtle.Turtle()
window = turtle.Screen()

def draw_function():
    for i in range(4):
        square.forward(40)
        square.left(90)

for i in range(5):
    draw_function()
    square.up()
    square.forward(80)
    square.down()
window.exitonclick()