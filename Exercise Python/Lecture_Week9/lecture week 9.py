infile = open("qbdata.txt", "r")
for line in infile: # traverse file by line using for loop
    values = line.split() # split line by whitespace to a list of strings
    print('QB ', values[0], values[1], 'had a rating of ', values[10])
infile.close()

print("")
infile = open("qbdata.txt","r")
line = infile.readline()
# read the 1st line
# traverse file by line using while loop
# split line by whitespace into a list of strings
while line:
    values = line.split()
    print('QB ', values[0], values[1], 'had a rating of ', values[10])
    line = infile.readline() # read the next line
infile.close()

infile = open("qbdata.txt","r")
outfile = open("qbnames.txt","w")
line = infile.readline()
while line:
    items = line.split()
    data_line = items[1] + ',' + items[0] + '\n'
    outfile.write(data_line)
line = infile.readline()
infile.close()
outfile.close()