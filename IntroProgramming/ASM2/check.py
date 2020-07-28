import turtle
import random
pieChart = turtle.Turtle()

window = turtle.Screen()
# creating an empty list
listNumber = []
listAngle=[]
listPhanTram=[]
n = int(input("Enter number of elements : "))
sum=0

for i in range(0, n):
    element = float(input())
    sum = sum + element
    listNumber.append(element)  # adding the element

for i in listNumber:
    phanTram=round(((i/sum)*100),1)
    listPhanTram.append(phanTram)

for i in listPhanTram:
    angle = round(((i * 360) / 100), 1)
    listAngle.append(angle)

color=["red","green","blue","pink","purple","grey","darkred",
       "darkblue","darkgreen","darkgrey","lightgrey","cyan","magenta","violet",
       "navy","coral","maroon","orange","darkseagreen","steelblue","tan","seagreen"]

pieChart.pensize(2)
pieChart.goto(0,200)
def draw_piechart(angle):
    PT=round(((angle*100)/360),1)
    pieChart.begin_fill()
    pieChart.fillcolor(random.choice(color))
    pieChart.circle(-200, angle)
    pieChart.goto(0, 0)
    pieChart.left(90+angle/2)
    pieChart.up()
    pieChart.forward(150)
    pieChart.down()
    pieChart.color("white")
    pieChart.write(  PT, font=("bold",12),align="right")
    pieChart.write("%",font=("bold",12),align="left")
    pieChart.up()
    pieChart.backward(150)
    pieChart.down()
    pieChart.color("black")
    pieChart.fillcolor(random.choice(color))
    pieChart.right(angle/2)
    pieChart.end_fill()
    pieChart.forward(200)
    pieChart.right(90)


for c in listAngle:
    draw_piechart(c)


window.exitonclick()
