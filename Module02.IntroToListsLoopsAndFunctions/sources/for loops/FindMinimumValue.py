#initialize the list
numbers = [-5, -3, -8, 1, 2, -2, 0]

minValue = numbers[0]

for number in numbers:
    if (number < minValue):
        minValue = number

print("The minimum value is", minValue)

#Use another way of for loop, check by index
minIndex = 0
for i in range(0, len(numbers)):
    if (numbers[i] < numbers[minIndex]):
        minIndex = i
print("The minimum value counted by index way is", numbers[minIndex])