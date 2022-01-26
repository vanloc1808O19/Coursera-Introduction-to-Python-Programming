# a string is a sequence of characters \approx a list of characters
# unlike list, strings are immutable
# for example, if we have a list
myMenuChoices = ["burger", "fries", "coke"]
# we can get a single value
mainCourse = myMenuChoices[0]
print(mainCourse)

# we can also update a single value
myMenuChoices[0] = "cheese burger"
print(myMenuChoices)

# however, if we have a string:
myRestaurantChoice = "McDonalds"

# we can get a single value
thirdLetter = myRestaurantChoice[2]
print(thirdLetter)

# but we cannot directly update a single value
# myRestaurantChoice[2] = "t" --> error
# print(myRestaurantChoice)