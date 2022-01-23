"""By default, the input command returns a string"""
favMovie = input("What is your favorite movie? ")
#print(favMovie)

favSinger = input("Who is your favorite singer? ")
#print(favSinger)

favs = "Your favorite movie is " + favMovie + " and your favorite singer is " + favSinger
print(favs)

age = (int)(input("How old are you? "))
print("After 3 years, you will be", age + 3, "years old.")
