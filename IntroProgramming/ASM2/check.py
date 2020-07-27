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

color=["red","green","blue","pink","purple","yellow","darkred","darkblue","darkgreen"]

def write_num(a):
    pieChart.up()
    pieChart.goto(0, 0)
    pieChart.left(90)
    pieChart.right(angle/2)
    pieChart.forward(100)
    pieChart.down()
    pieChart.write(a)
    pieChart.up()
    pieChart.backward(100)
    pieChart.left(90)
    pieChart.forward(200)
    pieChart.right(90)
    pieChart.down()

pieChart.goto(0,200)
def draw_piechart(angle):
    pieChart.begin_fill()
    pieChart.fillcolor(random.choice(color))
    pieChart.circle(-200, angle)
    pieChart.goto(0, 0)
    pieChart.end_fill()
    pieChart.left(90)
    pieChart.forward(200)
    pieChart.right(90)




for c in listAngle:
    draw_piechart(c)

for a in listPhanTram:
    write_num(a)

window.exitonclick()
