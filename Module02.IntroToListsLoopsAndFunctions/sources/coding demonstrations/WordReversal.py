word = input("Enter a word: ")
rev = ""

for i in range(len(word) - 1, -1, -1):
    rev += word[i]

print("The reversed word is:", rev)