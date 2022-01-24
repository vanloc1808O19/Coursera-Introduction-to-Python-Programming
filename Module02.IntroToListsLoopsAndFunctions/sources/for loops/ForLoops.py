numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    print(number, end = " ")
print("\n")

#to store even numbers
evenNumbers = []
evenCount = 0
for number in numbers:
    #check even number
    if (number % 2 == 0):
        evenNumbers.append(number)
        evenCount += 1
print(evenNumbers)
print("There are" , evenCount, "even numbers.")
print("There are" , len(evenNumbers), "even numbers.")