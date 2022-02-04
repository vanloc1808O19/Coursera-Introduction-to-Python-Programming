# create a tuple
direction = ("north", "south", "east", "west")
print(type(direction))  # <class 'tuple'>
print(direction)

# update a tuple will get an error
# direction[0] = "N" -> error
# direction[4] = "abcxyz" -> error

possibleGrades = "A", "B", "C", "D", "F"
print(type(possibleGrades))  # <class 'tuple'>
print(possibleGrades)

# create a tuple from a string (even a list)
possibleGrades = tuple("ABCDF")
print(possibleGrades)

# tuples are very useful when we want to return multiple things from a function

