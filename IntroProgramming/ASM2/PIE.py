import turtle
pieChart = turtle.Turtle()

window = turtle.Screen()
# creating an empty list
listNumber = []
listPhanTram=[]
listAngle=[]

n = int(input("Enter number of elements : "))
sum=0


for i in range(0, n):
    element = float(input())
    sum = sum + element
    listNumber.append(element)  # adding the element
a=float()

for a in listNumber:
    phanTram=round(((a/sum)*100),1)
    print(phanTram)
    listPhanTram.append(phanTram)

for b in listPhanTram:
    angle=round(((b*360)/100),1)
    print(angle)
    listAngle.append(angle)

def draw_piechart(angle):
    pieChart.begin_fill()
    pieChart.fillcolor("red")
    pieChart.right(angle)
    pieChart.forward(200)

    pieChart.backward(200)
    pieChart.end_fill()

pieChart.goto(0, 200)
pieChart.circle(-200, 360)
pieChart.goto(0, 0)
pieChart.left(90)
for c in listAngle:
    draw_piechart(c)

window.exitonclick()
