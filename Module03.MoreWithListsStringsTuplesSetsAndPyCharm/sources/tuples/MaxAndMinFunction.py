def maxAndMin(list):
    maxValue = list[0]
    minValue = list[0]

    for i in range(1, len(list), 1):
        if (list[i] > maxValue):
            maxValue = list[i]
        elif (list[i] < minValue):
            minValue = list[i]

    return (maxValue, minValue)

def main():
    ls = [-1, 2, -10, 100, 40, 209]

    maxValue = maxAndMin(ls)[0]
    minValue = maxAndMin(ls)[1]
    print(maxValue)
    print(minValue)

if __name__ == "__main__":
    main()