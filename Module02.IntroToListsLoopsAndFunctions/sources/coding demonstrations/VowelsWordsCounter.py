def vowelsCount(string):
    cnt = 0

    for s in string:
        if s in "aeiou":
            cnt += 1
    
    return cnt

def wordCount(sentence):
    #remove the whitespaces from beginning and end of the sentence
    sentence = sentence.strip()

    spaceCount = 0

    for s in sentence:
        if (s == " "):
            spaceCount += 1

    return spaceCount + 1

def main():
    string = input("Input a string: ")
    print("The number of vowels in the string is:", vowelsCount(string))

    sentence = input("Input a sentence: ")
    print("The number of words in the sentence is:", wordCount(sentence))

# to execute main function
if __name__ == "__main__":
    main()