import turtle
poly=turtle.Turtle()
window = turtle.Screen()
sides=int(input("Input sides: "))
length=int(input("Input length: "))
a=sides

def draw_poly(poly, a, length):
    angle = 180-((1 - (2 / sides)) * 180)
    for i in range(a):
        poly.forward(length)
        poly.right(angle)
x=0
y=0
for i in range(10):
    draw_poly(poly,a,length)
    length=length+20

window.exitonclick()