filename = str(input("Entering the name of the file: "))

output_file = open(filename, "w")

source_code = """
import turtle
turtle = turtle.Turtle()
turtle.circle(360)
"""

output_file.write(source_code)

output_file.close()
