# set a variable name to the value of your first and last name
# print the substring counting just your first name, without counting the letters in your first name

name = "Loc Nguyen "
# get index of the single space between first name and last name
firstSpaceIndex = name.index(" ")

print(name[0:firstSpaceIndex])

