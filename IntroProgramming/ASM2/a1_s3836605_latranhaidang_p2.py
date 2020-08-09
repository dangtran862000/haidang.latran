# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: La Tran Hai Dang (s3836605)
# Created date: 01/08/2020
# Last modified date: 09/08/2020

import turtle
import random

# creat a turtle with the name pieChart
pieChart = turtle.Turtle()

window = turtle.Screen()
# creating an empty list
listElement = []    # this is the list of element values, which are inputted by user
listAngle = []  # this is the list of angles, which are calculated from the element value
# This is a list of color to choose randomly
color = ["red", "green", "blue", "pink", "purple", "grey", "darkred", "darkblue",
         "darkgrey", "lightgrey", "cyan", "magenta", "violet", "navy",
         "coral", "maroon", "orange", "darkseagreen", "steelblue", "tan", "seagreen", "rosybrown"]

'''
This step is to ask the user how many elements corresponds to 
the number of parts of the circle and use the loop to enter each value of each part
'''
Sum = 0
n = int(input("Enter number of elements : "))
for i in range(0, n):
    element = float(input())    # input each element value
    listElement.append(element)  # adding the new element into the list (listElement[])
    Sum = Sum + element     # calculating the sum of elements by adding up the newly imported elements
print("ENOUGH ELEMENTS !!!")    # notifying when the user has entered enough the number of elements


'''
This step using loop to calculate: 
    The percentage of each element by dividing the value by the total value of all elements
    The angle of each element by multiplying the percentage by 360 degrees then dividing by 100.
'''
for element in listElement:
    Percentage = round(((element/Sum)*100), 1)  # calculate the percentage and round to 1 decimal place
    angle = round(((Percentage * 360) / 100), 1)    # calculate the angle and round to 1 decimal place
    listAngle.append(angle)     # storing the new value of angle to the list (listAngle[])


# Creating the function to draw the pie chart (draw_piechart)
def draw_piechart():
    pieChart.begin_fill()
    for chooseColor in color:  # Choosing color in the list (color[]) above
        pieChart.fillcolor(chooseColor)
    # Drawing the circle with the radius = 200px and draw an angle (in the listAngle[]) in the opposite direction
    pieChart.circle(-200, angle)
    pieChart.goto(0, 0)
    pieChart.left(90+angle/2)
    # Writing the percentage digits on each part of the pie chart
    pieChart.up()
    pieChart.forward(150)
    pieChart.down()
    pieChart.color("white")
    pieChart.write(round(((angle*100)/360), 1), font=('Arial', 12, 'normal'), align="right")
    pieChart.write("%", font=('Arial', 12, 'normal'), align="left", )
    pieChart.up()
    pieChart.backward(150)
    pieChart.down()
    # returning the next position to continue draw the next part
    pieChart.color("black")
    pieChart.fillcolor(random.choice(color))    # randomly selects a color from the color list
    pieChart.right(angle/2)
    pieChart.end_fill()
    pieChart.forward(200)
    pieChart.right(90)


# Drawing the pie chart
pieChart.goto(0, 200)   # setting the first position
for angle in listAngle:    # using loop to draw each part in listAngle[]
    draw_piechart()     # drawing an part


window.exitonclick()
