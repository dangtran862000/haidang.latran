messanges = str(input("Input your message: "))

output_file = open("messages.txt", "w")

for i in range(0,101):
    output_messages = messanges + '\n'
    output_file.write(output_messages)

output_file.close()

