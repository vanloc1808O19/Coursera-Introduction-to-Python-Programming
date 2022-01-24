#Form: range(start, up_to, step)
#start and step are both optional
#up_to means "up to but not including" the value
#can only use integers (no float)!

#iterate over sequence of 10 numbers: 0 - 9
for x in range(10):
    print(x, end = " ")
print("")

#iterate over sequence of 10 numbers: 0 - 9
for x in range(0, 10):
    print(x, end = " ")
print("")

#iterate over sequence of 6 numbers: 1 - 6
for x in range(1, 7):
    print(x, end = " ")
print("")

#iterate over sequence of 5 numbers: 0 - 28, skip every 6 numbers
for x in range(0, 30, 7):
    print(x, end = " ")
print("")

#iterate over sequence of 6 numbers, counting down from 5 to 0
for x in range(5, -1, -1):
    print(x, end = " ")
print("")

#find the odd numbers between 1 and 1200
odd = []
for x in range(1, 1201, 1):
    if (x % 2 == 1) :
        odd.append(x)
print(odd)