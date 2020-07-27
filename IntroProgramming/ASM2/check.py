import turtle
pieChart = turtle.Turtle()

window = turtle.Screen()



pieChart.right(90)
pieChart.goto(0,0)
pieChart.left(180)
pieChart.left(90-30)
pieChart.forward(200)
pieChart.left(90)
pieChart.circle(200,60)
pieChart.goto(0,0)
pieChart.right(90)
pieChart.forward(200)
pieChart.left(90)
pieChart.circle(200,45)

window.exitonclick()
