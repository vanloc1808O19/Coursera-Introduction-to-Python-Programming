# exit a loop using "continue"

x = 1

while (x <= 100):
    if (x % 3 == 0):
        x += 1
        continue
    elif (x % 2 == 1):
        print(x)

    x += 1