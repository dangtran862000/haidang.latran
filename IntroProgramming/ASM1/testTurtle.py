
import turtle
Flower1=turtle.Turtle()
window = turtle.Screen()

Flower1.goto(-100,0)


originalAngle=90
lengthFlower=0       #This is the length of a petal. Starting draw the flower1 with the length = 0 pixel
for times in range(4):
    for i in range(20):          #looping draw 20 times to change the size of the flower1
        lengthFlower=lengthFlower+3  #adding 3 pixel to lengthFlower of each loop
        for color in ["green","blue","red","pink"]: #looping to change 4 colors: green, blue, red, pink
            Flower1.pencolor(color) #using the color in the list of 4 colors in the loop
            Flower1.left(45)  #turn left the turtle 45 degrees
            Flower1.forward(lengthFlower) #Turtle draw the petal with the lengthFlower
            Flower1.right(originalAngle-1) #Turtle turn right an angle = originalAngle - 1 degree
            Flower1.speed(100) #increasing the speed of turtle
#Draw the flower2
angleFlower=0       #This is the length of a petal. Starting draw the flower2 with the length = 0 pixel
for i in range(30):     #looping draw 15 times to change the size of the flower2
    angleFlower=angleFlower+3   #adding 3 pixel to lengthFlower of each loop
    for color in ["green","blue","red","pink"]:  #looping to change 4 colors: green, blue, red, pink
        Flower2.pencolor(color)     #using the color in the list of 4 colors in the loop
        Flower2.left(45)    #turn left the turtle 45 degrees
        Flower2.forward(angleFlower)    #Turtle turn right an angle = originalAngle - 1 degree
        Flower2.right(originalAngle-1)  #Turtle turn right an angle = originalAngle - 1 degree
        Flower2.speed(1200)  #increasing the speed of turtle

#Draw the flower3
angleFlower=0       #This is the length of a petal. Starting draw the flower3 with the length = 0 pixel
for i in range(30):     #looping draw 25 times to change the size of the flower3
    angleFlower=angleFlower+3   #adding 3 pixel to lengthFlower of each loop
    for color in ["green","blue","red","pink"]: #looping to change 4 colors: green, blue, red, pink
        Flower3.pencolor(color)     #using the color in the list of 4 colors in the loop
        Flower3.left(45)    #turn left the turtle 45 degrees
        Flower3.forward(angleFlower)    #Turtle turn right an angle = originalAngle - 1 degree
        Flower3.right(originalAngle-1)  #Turtle turn right an angle = originalAngle - 1 degree
        Flower3.speed(1200)  #increasing the speed of turtle

#Draw the flower4
angleFlower=0       #This is the length of a petal. Starting draw the flower4 with the length = 0 pixel
for i in range(30):     #looping draw 10 times to change the size of the flower4
    angleFlower=angleFlower+3   #adding 3 pixel to lengthFlower of each loop
    for color in ["green","blue","red","pink"]: #looping to change 4 colors: green, blue, red, pink
        Flower4.pencolor(color)     #using the color in the list of 4 colors in the loop
        Flower4.left(45)    #turn left the turtle 45 degrees
        Flower4.forward(angleFlower)    #Turtle turn right an angle = originalAngle - 1 degree
        Flower4.right(originalAngle-1) #Turtle turn right an angle = originalAngle - 1 degree
        Flower4.speed(1200)  #increasing the speed of turtle
