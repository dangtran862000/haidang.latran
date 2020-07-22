import turtle
equilTriangle = turtle.Turtle()
square=turtle.Turtle()
hexagon=turtle.Turtle()
octagon=turtle.Turtle()
window = turtle.Screen()

equilTriangle.up()
equilTriangle.left(90)
equilTriangle.forward(100)
equilTriangle.down()
equilTriangle.right(150) #start drawing equil Triangle
equilTriangle.forward(100)
for i in range(2):
    equilTriangle.right(120)
    equilTriangle.forward(100)

square.forward(80)
for i in range (4):
    square.left(90)
    square.forward(160)

hexagon.up()
hexagon.right(90)
hexagon.forward(20)
hexagon.down()
hexagon.left(60)
hexagon.forward(120)
for i in range(5):
    hexagon.right(60)
    hexagon.forward(120)

octagon.up()
octagon.forward(181)
octagon.down()
octagon.left(90)
octagon.forward(150)
for i in range(7):
    octagon.left(45)
    octagon.forward(150)

window.exitonclick()
