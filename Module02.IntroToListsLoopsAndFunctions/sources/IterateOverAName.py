name = input("What is your first name? ")

print(name, "is spelled as:")

letterCount = 0
for x in name:
    print(x, end = " ")
    letterCount += 1
print("\n")
print("There are", letterCount, "letters in", name)