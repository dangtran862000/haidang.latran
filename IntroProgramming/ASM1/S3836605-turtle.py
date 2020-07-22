# RMIT University Vietnam
# Course: COSC2429 Introduction to Programming
# Semester: 2020B
# Assignment: 1
# Author: LA TRAN HAI DANG (s3836605)
# Created date: 14/07/2020
# Last modified date: 16/07/2020

import turtle

window = turtle.Screen()

#Create 4 turtle to draw 4 flower from left to right orderly
Flower1=turtle.Turtle()
Flower2=turtle.Turtle()
Flower3=turtle.Turtle()
Flower4=turtle.Turtle()
logoRMIT=turtle.Turtle()  # Creat the turtle to draw the Logo of RMIT university


#hidden the icon of turtle
Flower1.hideturtle()
Flower2.hideturtle()
Flower3.hideturtle()
Flower4.hideturtle()
logoRMIT.hideturtle()

originalAngle=90 #This is an original to change the angle of the flower

Flower1.up() #no drawing when moving up
Flower1.goto(200,200) #this is the position of the Flower1 x=200,y=200
Flower1.down() #no drawing when moving down
Flower2.up()  #no drawing when moving up
Flower2.goto(-200,-200) #this is the position of the Flower2 x=-200,y=-200
Flower2.down() #no drawing when moving down
Flower3.up()  #no drawing when moving up
Flower3.goto(200,-200)  #this is the position of the Flower3 x=200,y=-200
Flower3.down()  #no drawing when moving down
Flower4.up()  #no drawing when moving up
Flower4.goto(-200,200)  #this is the position of the Flower4 x=-200,y=200
Flower4.down()  #no drawing when moving down

#Draw the flower1
lengthFlower=0       #This is the length of a petal. Starting draw the flower1 with the length = 0 pixel
for i in range(30):          #looping draw 30 times to change the size of the flower1
    lengthFlower=lengthFlower+3  #adding 3 pixel to lengthFlower of each loop
    for color in ["green","blue","red","pink"]: #looping to change 4 colors: green, blue, red, pink
        Flower1.pencolor(color) #using the color in the list of 4 colors in the loop
        Flower1.left(45)  #turn left the turtle 45 degrees
        Flower1.forward(lengthFlower) #Turtle draw the petal with the lengthFlower
        Flower1.right(originalAngle-1) #Turtle turn right an angle = originalAngle - 1 degree
        Flower1.speed(120) #increasing the speed of turtle

#Draw the flower2
lengthFlower=0       #This is the length of a petal. Starting draw the flower2 with the length = 0 pixel
for i in range(30):     #looping draw 30 times to change the size of the flower2
    lengthFlower=lengthFlower+3   #adding 3 pixel to lengthFlower of each loop
    for color in ["green","blue","red","pink"]:  #looping to change 4 colors: green, blue, red, pink
        Flower2.pencolor(color)     #using the color in the list of 4 colors in the loop
        Flower2.left(45)    #turn left the turtle 45 degrees
        Flower2.forward(lengthFlower)    #Turtle turn right an angle = originalAngle - 1 degree
        Flower2.right(originalAngle-1)  #Turtle turn right an angle = originalAngle - 1 degree
        Flower2.speed(120)  #increasing the speed of turtle

#Draw the flower3
lengthFlower=0       #This is the length of a petal. Starting draw the flower3 with the length = 0 pixel
for i in range(30):     #looping draw 30 times to change the size of the flower3
    lengthFlower=lengthFlower+3   #adding 3 pixel to lengthFlower of each loop
    for color in ["green","blue","red","pink"]: #looping to change 4 colors: green, blue, red, pink
        Flower3.pencolor(color)     #using the color in the list of 4 colors in the loop
        Flower3.left(45)    #turn left the turtle 45 degrees
        Flower3.forward(lengthFlower)    #Turtle turn right an angle = originalAngle - 1 degree
        Flower3.right(originalAngle-1)  #Turtle turn right an angle = originalAngle - 1 degree
        Flower3.speed(120)  #increasing the speed of turtle

#Draw the flower4
lengthFlower=0       #This is the length of a petal. Starting draw the flower4 with the length = 0 pixel
for i in range(30):     #looping draw 30 times to change the size of the flower4
    lengthFlower=lengthFlower+3   #adding 3 pixel to lengthFlower of each loop
    for color in ["green","blue","red","pink"]: #looping to change 4 colors: green, blue, red, pink
        Flower4.pencolor(color)     #using the color in the list of 4 colors in the loop
        Flower4.left(45)    #turn left the turtle 45 degrees
        Flower4.forward(lengthFlower)    #Turtle turn right an angle = originalAngle - 1 degree
        Flower4.right(originalAngle-1) #Turtle turn right an angle = originalAngle - 1 degree
        Flower4.speed(120)  #increasing the speed of turtle

#drawing the logo of RMIT University
logoRMIT.up()
logoRMIT.goto(0,-80) #star drawing the RMIT logo at the position with x=0,y=-80
logoRMIT.down()

logoRMIT.begin_fill() #starting fill
logoRMIT.color("red", "red") #fill the color of RMIT University logo

logoRMIT.circle(90,180) #drawing the circle with the radius = 90 pixel and draw 180 degrees

#start drawing the left half of the logo
logoRMIT.forward(20)
logoRMIT.left(90)
logoRMIT.forward(20)
logoRMIT.right(90)
logoRMIT.forward(40)
logoRMIT.left(90)
logoRMIT.forward(40)
logoRMIT.right(90)
logoRMIT.forward(30)
logoRMIT.left(90)
logoRMIT.forward(30)
logoRMIT.forward(30)
logoRMIT.left(90)
logoRMIT.forward(30)
logoRMIT.right(90)
logoRMIT.forward(40)
logoRMIT.left(90)
logoRMIT.forward(40)
logoRMIT.right(90)
logoRMIT.forward(20)
logoRMIT.left(90)
logoRMIT.forward(20)

logoRMIT.end_fill()  #ending fill

window.exitonclick()