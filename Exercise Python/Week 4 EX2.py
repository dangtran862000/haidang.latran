import turtle
square=turtle.Turtle()
window = turtle.Screen()
size=40
def draw_function(square,size):
    for i in range(4):
        square.forward(size)
        square.left(90)
x=0
y=0
for i in range(5):
    draw_function(square,size)
    x = x - 10
    y = y - 10
    square.up()
    square.goto(x,y)
    square.down()
    size=size+20


window.exitonclick()