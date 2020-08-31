import turtle

mystery = turtle.Turtle()
window = turtle.Screen()

input_file = open("mystery.txt", "r")

line = input_file.readline()
while line:
    for i in line:
        if line == "UP\n":
            mystery.up()
        elif line == "DOWN\n":
            mystery.down()
        else:
            values = line.split()
            x = int(values[0])
            y = int(values[1])
            mystery.goto(x, y)
    line = input_file.readline()

input_file.close()
window.exitonclick()
