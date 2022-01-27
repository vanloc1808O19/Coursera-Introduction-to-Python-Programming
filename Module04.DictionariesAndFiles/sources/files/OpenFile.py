stream = open("a.txt", "r")

# read an entire file as a string
lines = stream.read()  # read all text in the file
print(lines)

# read a file line by line. Each line is read as a string
line = stream.readline()  # read one line in the file
print(line)

# read all lines in a file as a list.
# each line in the list will be a string.
linesList = stream.readlines()
print(linesList)

stream.close()
