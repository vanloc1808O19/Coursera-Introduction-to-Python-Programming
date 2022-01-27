# split is a string method to split a single string into a list of multiple strings
colors = "blue,red,green"
colorsList = colors.split(',')   # split string into a list of strings using comma separator
print(colorsList)
print(colorsList[2])

# join is a string method to create a single string from a list of strings
separator = ','
newColors = separator.join(colorsList)  # join list of strings using seperator value
print(newColors)

# if we want to update a character in a string
# we can first convert the string to an actual list
# NOTE: call the split function with an empty string ('') will throw an error
# instead, we can use Python's built-in list function to convert the string to a list
myRestaurantChoice = "McDonalds"
myRestaurantChoiceList = list(myRestaurantChoice)

# now, we can update the letters
myRestaurantChoiceList[2] = "d"

# then, we convert back to a string using join
myRestaurantChoice = ''.join(myRestaurantChoiceList)
print(myRestaurantChoice)