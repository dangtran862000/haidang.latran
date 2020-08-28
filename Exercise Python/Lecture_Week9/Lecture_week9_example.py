input_file = open("quiz_scores.txt", "r")
output_file = open("average_scores.txt", "w")

count = 0
sum = 0
line = input_file.readline()
while line:
    for i in line:
        values = line.split(", ")
        if i == " ":
            count += 1
    count += 1
    values = line.split(", ")
    for i in range(1, count):
        sum = sum + int(values[i])
    average = round(sum / (count - 1), 1)
    average_line = values[0] + ', ' + str(average) + '\n'
    output_file.write(average_line)
    count = 0
    line = input_file.readline()

output_file.close()
input_file.close()
