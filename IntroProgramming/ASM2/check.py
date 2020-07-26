import turtle
UKflag = turtle.Turtle()
UKflag_layer2 = turtle.Turtle()
AUSflag = turtle.Turtle()
Star = turtle.Turtle()
Star5 = turtle.Turtle()
window = turtle.Screen()



x = 0
y = 0


length=600

if length == 600:

    UKflag_layer2.goto(x-300, y+150)
    UKflag_layer2.right(90)
    UKflag_layer2.forward(150)

    UKflag_layer2.right(90)
    UKflag_layer2.begin_fill()
    UKflag_layer2.color("black", "black")
    UKflag_layer2.fillcolor("white")
    for i in range(4):
        UKflag_layer2.forward(50)
        UKflag_layer2.right(90)
        UKflag_layer2.forward(100)
        UKflag_layer2.left(90)
        UKflag_layer2.forward(250)
        UKflag_layer2.right(90)
        UKflag_layer2.forward(50)

    UKflag_layer2.end_fill()

    UKflag_layer2.begin_fill()
    UKflag_layer2.color("black", "black")
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


    UKflag_layer2.backward(300)
    UKflag_layer2.right(90)
    UKflag_layer2.forward(300)
    UKflag_layer2.left(180)

    for i in range(4):
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
     



window.exitonclick()
