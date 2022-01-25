numList = []
i = 0
isPlaying = True

while (isPlaying == True):
    num = int(input("Enter an integer: "))

    # test if the entered number is -1, quit the program
    if (num == -1):
        isPlaying = False

    # add the number to the list
    numList.append(num)
    i += 1

#find the sum of all elements
sum = 0
for num in numList:
    sum += num

#find the average
avg = sum / i

print("Average:", avg)