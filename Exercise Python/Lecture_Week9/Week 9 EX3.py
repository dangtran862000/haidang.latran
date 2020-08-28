name_file = str(input("Input the name of the new file: "))

new_file = open("new_"+name_file, "w")
print("new_"+name_file, "has created successful !!!")

input_file = open("simple.txt", "r")

count = 1
for line in input_file:
    new_file.write(str(count) + line)
    count = count + 1

new_file.close()
input_file.close()
