stream = open("b.txt", "w")

# write a single string to a file
stream.write("Hello ")

# write a list of strings to a file
stream.writelines("This is a file to write")

stream.close()
