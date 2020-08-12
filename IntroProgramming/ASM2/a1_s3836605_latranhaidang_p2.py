# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: La Tran Hai Dang (s3836605)
# Created date: 01/08/2020
# Last modified date: 12/08/2020

import turtle
import random  # this library to use choosing randomly the color

# creat a turtle with the name pieChart

pieChart = turtle.Turtle()

window = turtle.Screen()
# creating an empty list
listElement = []  # this is the list of element values, which are inputted by user
listAngle = []  # this is the list of angles, which are calculated from the element value
# This is a list of color to choose randomly
color = ["red", "green", "blue", "pink", "purple", "grey", "darkred", "darkblue",
         "darkgrey", "lightgrey", "cyan", "magenta", "violet", "navy",
         "coral", "maroon", "orange", "darkseagreen", "steelblue", "tan", "seagreen", "rosybrown"]

'''
This step is to check and ask the user how many elements corresponds to 
the number of parts of the circle and use the loop to enter each value of each part
'''
sum_element = 0  # The original value of sum
while True:  # This while loop infinitely to check the value of (the number of element) input by user
    try:  # Run the code into "try" first - if the block in try has an error, the program will find the except below
        num = int(input("Enter the number of elements: "))
        for i in range(1, num + 1):
            while True:  # Then this while loop infinitely to check the value of (the number of element) input by user
                try:  # if the block in try has an error, the program will find the except below
                    print("Input the value of number", i, end=": ")
                    element = float(input())  # input each element value
                    listElement.append(element)  # adding the new element into the list (listElement[])
                    # calculating the sum of elements by adding up the newly imported elements
                    sum_element = sum_element + element
                    break   # break if user input correct value
                except ValueError:  # if user input the error value (ValueError) run this code until correct value
                    print("Invalid number !!! PLEASE TRY AGAIN")
                    continue  # # continue run this code until correct value
        print("ENOUGH ELEMENTS !!!")  # notifying when the user has entered enough the number of elements
        break  # break if user input correct value
    except ValueError:  # if user input the error value (ValueError) run this code until correct value
        print("Invalid number !!! PLEASE TRY AGAIN")
        continue  # continue run this code until correct value

'''
This step using loop to calculate: 
    The percentage of each element by dividing the value by the total value of all elements
    The angle of each element by multiplying the percentage by 360 degrees then dividing by 100.
'''
for element in listElement:
    Percentage = round(((element / sum_element) * 100), 1)  # calculate the percentage and round to 1 decimal place
    angle = round(((Percentage * 360) / 100), 1)  # calculate the angle and round to 1 decimal place
    listAngle.append(angle)  # storing the new value of angle to the list (listAngle[])


# Creating the function to draw the pie chart (draw_pie_chart)
def draw_pie_chart():
    pieChart.begin_fill()
    for chooseColor in color:  # Choosing color in the list (color[]) above
        pieChart.fillcolor(chooseColor)
    # Drawing the circle with the radius = 200px and draw an angle (in the listAngle[]) in the opposite direction
    pieChart.circle(-200, angle)
    pieChart.goto(0, 0)
    pieChart.left(90 + angle / 2)
    # Writing the percentage digits on each part of the pie chart
    pieChart.up()
    pieChart.forward(150)
    pieChart.down()
    pieChart.color("white")
    pieChart.write(round(((angle * 100) / 360), 1), font=('Arial', 12, 'normal'), align="right")
    pieChart.write("%", font=('Arial', 12, 'normal'), align="left", )
    pieChart.up()
    pieChart.backward(150)
    pieChart.down()
    # returning the next position to continue draw the next part
    pieChart.color("black")
    pieChart.fillcolor(random.choice(color))  # randomly selects a color from the color list
    pieChart.right(angle / 2)
    pieChart.end_fill()
    pieChart.forward(200)
    pieChart.right(90)


# Drawing the pie chart
pieChart.goto(0, 200)  # setting the first position
for angle in listAngle:  # using loop to draw each part in listAngle[]
    draw_pie_chart()  # drawing an part of pie chart

window.exitonclick()
